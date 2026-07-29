from __future__ import annotations

import argparse
import asyncio
import json
import socket
import sys
from collections.abc import Callable
from typing import Any

from websockets import connect

from bci_jsonl_to_unity_commands import (
    build_message,
    emit_stdout,
    emit_udp,
    log_nonaccepted,
    normalize_command,
)


Command = dict[str, Any]
CommandHandler = Callable[[Command], None]


def decode_websocket_event(raw_message: str | bytes) -> dict[str, Any]:
    """Converte exatamente uma mensagem WebSocket em um evento do interpretador."""
    if isinstance(raw_message, bytes):
        try:
            text = raw_message.decode("utf-8")
        except UnicodeDecodeError:
            return {
                "type": "invalid",
                "reason": "invalid_utf8:websocket_message",
            }
    elif isinstance(raw_message, str):
        text = raw_message
    else:
        return {
            "type": "invalid",
            "reason": "invalid_type:websocket_message",
        }

    try:
        event = json.loads(text)
    except json.JSONDecodeError as exc:
        return {
            "type": "invalid",
            "reason": f"invalid_json:websocket_message:{exc.msg}",
        }

    if not isinstance(event, dict):
        return {
            "type": "invalid",
            "reason": "invalid_json_root:websocket_message",
        }

    return event


def interpret_websocket_message(raw_message: str | bytes) -> Command | None:
    """Encaminha uma mensagem WebSocket ao mesmo núcleo usado pelo replay JSONL."""
    return normalize_command(decode_websocket_event(raw_message))


def disconnected_message(reason: str) -> Command:
    """Gera o comando seguro usado quando a fonte WebSocket deixa de responder."""
    return build_message(
        {},
        command="no_move",
        status="error",
        reason=reason,
    )


class CommandEmitter:
    """Emite comandos no terminal e, opcionalmente, por UDP para a Unity."""

    def __init__(
        self,
        *,
        udp_host: str = "",
        udp_port: int = 5005,
        dedupe: bool = False,
        output: CommandHandler = emit_stdout,
    ) -> None:
        self.udp_host = udp_host
        self.udp_port = udp_port
        self.dedupe = dedupe
        self.output = output
        self.last_command: str | None = None
        self._socket = (
            socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            if udp_host
            else None
        )

    def emit(self, message: Command) -> bool:
        log_nonaccepted(message)

        command = str(message["command"])
        if self.dedupe and command == self.last_command:
            return False

        self.output(message)
        if self._socket is not None:
            emit_udp(message, self._socket, self.udp_host, self.udp_port)

        self.last_command = command
        return True

    def close(self) -> None:
        if self._socket is not None:
            self._socket.close()
            self._socket = None

    def __enter__(self) -> CommandEmitter:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


async def receive_once(
    uri: str,
    on_command: CommandHandler,
    *,
    open_timeout: float = 10.0,
    ping_interval: float = 20.0,
    ping_timeout: float = 20.0,
    max_message_bytes: int = 1_048_576,
) -> int:
    """Abre uma conexão e processa as mensagens até o servidor encerrá-la."""
    received = 0

    async with connect(
        uri,
        open_timeout=open_timeout,
        ping_interval=ping_interval,
        ping_timeout=ping_timeout,
        max_size=max_message_bytes,
    ) as websocket:
        print(
            json.dumps(
                {"level": "info", "status": "websocket_connected", "uri": uri},
                ensure_ascii=False,
            ),
            file=sys.stderr,
            flush=True,
        )

        async for raw_message in websocket:
            received += 1
            command = interpret_websocket_message(raw_message)
            if command is not None:
                on_command(command)

    return received


async def run_receiver(
    uri: str,
    emitter: CommandEmitter,
    *,
    reconnect: bool = True,
    reconnect_delay: float = 2.0,
    open_timeout: float = 10.0,
    ping_interval: float = 20.0,
    ping_timeout: float = 20.0,
    max_message_bytes: int = 1_048_576,
) -> int:
    """Mantém o receptor ativo e aplica parada segura a cada desconexão."""
    while True:
        reason = "websocket_disconnected"
        try:
            await receive_once(
                uri,
                emitter.emit,
                open_timeout=open_timeout,
                ping_interval=ping_interval,
                ping_timeout=ping_timeout,
                max_message_bytes=max_message_bytes,
            )
        except asyncio.CancelledError:
            raise
        except KeyboardInterrupt:
            reason = "websocket_interrupted"
            emitter.emit(disconnected_message(reason))
            return 0
        except Exception as exc:
            reason = f"websocket_connection_error:{type(exc).__name__}"
            print(
                json.dumps(
                    {
                        "level": "error",
                        "status": "websocket_connection_error",
                        "reason": str(exc),
                        "uri": uri,
                    },
                    ensure_ascii=False,
                ),
                file=sys.stderr,
                flush=True,
            )

        emitter.emit(disconnected_message(reason))

        if not reconnect:
            return 0

        await asyncio.sleep(reconnect_delay)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Recebe JSONs da LM-CNN por WebSocket, interpreta cada mensagem "
            "e emite comandos para a Unity."
        )
    )
    parser.add_argument(
        "--uri",
        required=True,
        help="Endpoint WebSocket da LM-CNN (ws:// ou wss://).",
    )
    parser.add_argument(
        "--udp-host",
        default="",
        help="Host UDP opcional da Unity. Sem este argumento, mostra no terminal.",
    )
    parser.add_argument(
        "--udp-port",
        type=int,
        default=5005,
        help="Porta UDP da Unity (padrao: 5005).",
    )
    parser.add_argument(
        "--dedupe",
        action="store_true",
        help="Emite somente quando o comando left/right/no_move mudar.",
    )
    parser.add_argument(
        "--no-reconnect",
        action="store_true",
        help="Encerra depois da primeira desconexao.",
    )
    parser.add_argument(
        "--reconnect-delay",
        type=float,
        default=2.0,
        help="Espera entre reconexoes, em segundos (padrao: 2).",
    )
    parser.add_argument(
        "--open-timeout",
        type=float,
        default=10.0,
        help="Limite para abrir a conexao, em segundos (padrao: 10).",
    )
    parser.add_argument(
        "--ping-interval",
        type=float,
        default=20.0,
        help="Intervalo do ping WebSocket, em segundos (padrao: 20).",
    )
    parser.add_argument(
        "--ping-timeout",
        type=float,
        default=20.0,
        help="Limite da resposta ao ping, em segundos (padrao: 20).",
    )
    parser.add_argument(
        "--max-message-bytes",
        type=int,
        default=1_048_576,
        help="Tamanho maximo de uma mensagem recebida (padrao: 1 MiB).",
    )
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> str | None:
    if args.udp_port < 1 or args.udp_port > 65535:
        return "--udp-port deve estar entre 1 e 65535"
    if args.reconnect_delay < 0:
        return "--reconnect-delay nao pode ser negativo"
    if args.open_timeout <= 0:
        return "--open-timeout deve ser positivo"
    if args.ping_interval <= 0:
        return "--ping-interval deve ser positivo"
    if args.ping_timeout <= 0:
        return "--ping-timeout deve ser positivo"
    if args.max_message_bytes <= 0:
        return "--max-message-bytes deve ser positivo"
    return None


def main() -> int:
    args = parse_args()
    validation_error = validate_args(args)
    if validation_error is not None:
        print(validation_error, file=sys.stderr)
        return 2

    with CommandEmitter(
        udp_host=args.udp_host,
        udp_port=args.udp_port,
        dedupe=args.dedupe,
    ) as emitter:
        try:
            return asyncio.run(
                run_receiver(
                    args.uri,
                    emitter,
                    reconnect=not args.no_reconnect,
                    reconnect_delay=args.reconnect_delay,
                    open_timeout=args.open_timeout,
                    ping_interval=args.ping_interval,
                    ping_timeout=args.ping_timeout,
                    max_message_bytes=args.max_message_bytes,
                )
            )
        except KeyboardInterrupt:
            emitter.emit(disconnected_message("websocket_interrupted"))
            return 0


if __name__ == "__main__":
    raise SystemExit(main())

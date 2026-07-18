from __future__ import annotations

import argparse
import json
import socket
import sys
import time
from pathlib import Path
from typing import Any


DEFAULT_INPUT_PATH = Path(__file__).with_name("bci_stream_example.jsonl")


COMMAND_MAP = {
    "SEM MOVIMENTO": "no_move",
    "ESQUERDA": "left",
    "DIREITA": "right",
}


def normalize_command(event: dict[str, Any]) -> dict[str, Any] | None:
    if event.get("type") != "inference":
        return None

    if event.get("rejected") is True:
        return None

    label_text = str(event.get("label_text", "")).strip().upper()
    if not label_text:
        return None

    command = COMMAND_MAP.get(label_text, "no_move")
    is_mi = bool(event.get("is_mi", False))
    p_move = float(event.get("p_move", 0.0))
    tau = float(event.get("tau", 0.0))

    # Para comandos ativos, exigimos imagetica motora detectada.
    if command in {"left", "right"} and not is_mi:
        command = "no_move"

    # Se o movimento nao passa do limiar, mantemos o estado neutro.
    if command in {"left", "right"} and p_move <= tau:
        command = "no_move"

    return {
        "command": command,
        "source_label": event.get("label"),
        "source_label_text": label_text,
        "is_mi": is_mi,
        "p_move": p_move,
        "tau": tau,
        "group_id": event.get("group_id"),
        "timestamp": time.time(),
    }


def iter_jsonl(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError as exc:
                print(
                    f"Linha {line_number} ignorada por JSON invalido: {exc}",
                    file=sys.stderr,
                )
    return events


def emit_stdout(message: dict[str, Any]) -> None:
    print(json.dumps(message, ensure_ascii=False), flush=True)


def emit_udp(message: dict[str, Any], sock: socket.socket, host: str, port: int) -> None:
    payload = json.dumps(message, ensure_ascii=False).encode("utf-8")
    sock.sendto(payload, (host, port))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Traduz eventos JSONL da CNN em comandos simplificados para Unity."
    )
    parser.add_argument(
        "--input",
        default=str(DEFAULT_INPUT_PATH),
        help="Arquivo JSONL de entrada. Por padrao, usa bci_stream_example.jsonl ao lado deste script.",
    )
    parser.add_argument(
        "--udp-host",
        default="",
        help="Host UDP opcional para envio dos comandos.",
    )
    parser.add_argument(
        "--udp-port",
        type=int,
        default=5005,
        help="Porta UDP opcional para envio dos comandos.",
    )
    parser.add_argument(
        "--dedupe",
        action="store_true",
        help="Emite apenas quando o comando mudar.",
    )
    parser.add_argument(
        "--sleep-ms",
        type=int,
        default=0,
        help="Atraso opcional entre comandos emitidos, em milissegundos.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Arquivo nao encontrado: {input_path}", file=sys.stderr)
        return 1

    events = iter_jsonl(input_path)
    sock: socket.socket | None = None
    if args.udp_host:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    last_command: str | None = None

    for event in events:
        message = normalize_command(event)
        if message is None:
            continue

        if args.dedupe and message["command"] == last_command:
            continue

        emit_stdout(message)
        if sock is not None:
            emit_udp(message, sock, args.udp_host, args.udp_port)

        last_command = str(message["command"])

        if args.sleep_ms > 0:
            time.sleep(args.sleep_ms / 1000.0)

    if sock is not None:
        sock.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

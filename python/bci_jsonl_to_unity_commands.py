from __future__ import annotations

import argparse
import json
import math
import socket
import sys
import time
from collections.abc import Iterator
from pathlib import Path
from typing import Any


DEFAULT_INPUT_PATH = Path(__file__).with_name("bci_stream_example.jsonl")


LABEL_TEXT_BY_ID = {
    0: "SEM MOVIMENTO",
    1: "ESQUERDA",
    2: "DIREITA",
}

COMMAND_BY_LABEL = {
    0: "no_move",
    1: "left",
    2: "right",
}


def build_message(
    event: dict[str, Any],
    *,
    command: str,
    status: str,
    reason: str = "",
) -> dict[str, Any]:
    raw_label_text = event.get("label_text")
    source_label_text = (
        raw_label_text.strip().upper()
        if isinstance(raw_label_text, str)
        else raw_label_text
    )
    return {
        "command": command,
        "status": status,
        "reason": reason,
        "source_label": event.get("label"),
        "source_label_text": source_label_text,
        "is_mi": event.get("is_mi"),
        "p_move": event.get("p_move"),
        "tau": event.get("tau"),
        "group_id": event.get("group_id"),
        "timestamp": time.time(),
    }


def invalid_message(event: dict[str, Any], reason: str) -> dict[str, Any]:
    return build_message(
        event,
        command="no_move",
        status="invalid",
        reason=reason,
    )


def is_finite_number(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
    )


def validate_optional_fields(event: dict[str, Any]) -> str | None:
    if "is_mi" in event and type(event["is_mi"]) is not bool:
        return "invalid_type:is_mi"

    for field in ("p_move", "tau"):
        if field in event and not is_finite_number(event[field]):
            return f"invalid_type:{field}"

    for field in ("raw_pred", "consecutive_rejected", "group_id"):
        if field in event and type(event[field]) is not int:
            return f"invalid_type:{field}"

    for field in ("p_combined", "ema"):
        if field not in event:
            continue
        values = event[field]
        if (
            not isinstance(values, list)
            or len(values) != 3
            or not all(is_finite_number(value) for value in values)
        ):
            return f"invalid_type:{field}"

    if "reason" in event and not isinstance(event["reason"], str):
        return "invalid_type:reason"

    return None


def normalize_command(event: dict[str, Any]) -> dict[str, Any] | None:
    if not isinstance(event, dict):
        return invalid_message({}, "invalid_type:event")

    if "type" not in event:
        return invalid_message(event, "missing_field:type")

    event_type_value = event["type"]
    if not isinstance(event_type_value, str):
        return invalid_message(event, "invalid_type:type")

    event_type = event_type_value.strip().lower()

    if event_type in {"started", "threshold"}:
        return None

    if event_type == "error":
        reason = event.get("message", event.get("reason", "classifier_error"))
        if not isinstance(reason, str):
            return invalid_message(event, "invalid_type:message")
        return build_message(
            event,
            command="no_move",
            status="error",
            reason=reason.strip() or "classifier_error",
        )

    if event_type == "invalid":
        reason = event.get("reason", "invalid_event")
        if not isinstance(reason, str):
            reason = "invalid_event"
        return invalid_message(event, reason)

    if event_type != "inference":
        return invalid_message(event, f"unknown_event_type:{event_type}")

    if "rejected" not in event:
        return invalid_message(event, "missing_field:rejected")

    if type(event["rejected"]) is not bool:
        return invalid_message(event, "invalid_type:rejected")

    if event["rejected"]:
        reason = event.get("reason", "inference_rejected")
        if not isinstance(reason, str):
            return invalid_message(event, "invalid_type:reason")
        return build_message(
            event,
            command="no_move",
            status="rejected",
            reason=reason.strip() or "inference_rejected",
        )

    for field in ("label", "label_text"):
        if field not in event:
            return invalid_message(event, f"missing_field:{field}")

    label = event["label"]
    if type(label) is not int:
        return invalid_message(event, "invalid_type:label")

    raw_label_text = event["label_text"]
    if not isinstance(raw_label_text, str):
        return invalid_message(event, "invalid_type:label_text")

    label_text = raw_label_text.strip().upper()
    if not label_text:
        return invalid_message(event, "empty_field:label_text")

    expected_label_text = LABEL_TEXT_BY_ID.get(label)
    if expected_label_text is None:
        return invalid_message(
            event,
            f"unknown_class:label={label}:label_text={label_text}",
        )

    if label_text != expected_label_text:
        return invalid_message(
            event,
            "label_label_text_mismatch:"
            f"label={label}:expected={expected_label_text}:received={label_text}",
        )

    validation_error = validate_optional_fields(event)
    if validation_error is not None:
        return invalid_message(event, validation_error)

    return build_message(
        event,
        command=COMMAND_BY_LABEL[label],
        status="accepted",
    )


def iter_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                yield {
                    "type": "invalid",
                    "reason": f"invalid_json:line={line_number}:{exc.msg}",
                }
                continue

            if not isinstance(event, dict):
                yield {
                    "type": "invalid",
                    "reason": f"invalid_json_root:line={line_number}",
                }
                continue

            yield event


def emit_stdout(message: dict[str, Any]) -> None:
    print(json.dumps(message, ensure_ascii=False), flush=True)


def emit_udp(message: dict[str, Any], sock: socket.socket, host: str, port: int) -> None:
    payload = json.dumps(message, ensure_ascii=False).encode("utf-8")
    sock.sendto(payload, (host, port))


def log_nonaccepted(message: dict[str, Any]) -> None:
    if message["status"] == "accepted":
        return

    log_entry = {
        "level": "error" if message["status"] == "error" else "warning",
        "status": message["status"],
        "reason": message["reason"],
        "command": message["command"],
        "source_label": message["source_label"],
        "source_label_text": message["source_label_text"],
        "timestamp": message["timestamp"],
    }
    print(json.dumps(log_entry, ensure_ascii=False), file=sys.stderr, flush=True)


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

        log_nonaccepted(message)

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

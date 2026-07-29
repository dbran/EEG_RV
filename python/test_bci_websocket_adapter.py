from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from typing import Any

PYTHON_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PYTHON_ROOT.parent
if str(PYTHON_ROOT) not in sys.path:
    sys.path.insert(0, str(PYTHON_ROOT))

from websockets import serve

from bci_websocket_to_unity import (
    CommandEmitter,
    decode_websocket_event,
    interpret_websocket_message,
    receive_once,
    run_receiver,
)

REAL_JSONL = PYTHON_ROOT / "bci_stream_example.jsonl"


def inference_event(**overrides: Any) -> dict[str, Any]:
    event: dict[str, Any] = {
        "type": "inference",
        "label": 1,
        "label_text": "ESQUERDA",
        "p_combined": [0.05, 0.9, 0.05],
        "ema": [0.255, 0.706, 0.039],
        "raw_pred": 1,
        "rejected": False,
        "reason": "",
        "is_mi": True,
        "p_move": 0.831,
        "tau": 0.45,
        "consecutive_rejected": 0,
        "group_id": 0,
        "hand": None,
    }
    event.update(overrides)
    return event


class WebSocketMessageTests(unittest.TestCase):
    def test_text_json_is_forwarded_to_interpreter(self) -> None:
        message = json.dumps(inference_event())

        result = interpret_websocket_message(message)

        self.assertIsNotNone(result)
        self.assertEqual("left", result["command"])
        self.assertEqual("accepted", result["status"])

    def test_binary_utf8_json_is_supported(self) -> None:
        message = json.dumps(
            inference_event(label=2, label_text="DIREITA")
        ).encode("utf-8")

        result = interpret_websocket_message(message)

        self.assertIsNotNone(result)
        self.assertEqual("right", result["command"])
        self.assertEqual("accepted", result["status"])

    def test_started_message_does_not_emit_command(self) -> None:
        result = interpret_websocket_message(
            json.dumps({"type": "started", "mode": "screen"})
        )

        self.assertIsNone(result)

    def test_malformed_json_becomes_safe_no_move(self) -> None:
        result = interpret_websocket_message('{"type":"inference",')

        self.assertIsNotNone(result)
        self.assertEqual("no_move", result["command"])
        self.assertEqual("invalid", result["status"])
        self.assertIn("invalid_json:websocket_message", result["reason"])

    def test_non_object_json_becomes_safe_no_move(self) -> None:
        result = interpret_websocket_message("[1, 2, 3]")

        self.assertIsNotNone(result)
        self.assertEqual("no_move", result["command"])
        self.assertEqual("invalid", result["status"])
        self.assertEqual(
            "invalid_json_root:websocket_message",
            result["reason"],
        )

    def test_invalid_utf8_becomes_safe_no_move(self) -> None:
        event = decode_websocket_event(b"\xff\xfe")
        result = interpret_websocket_message(b"\xff\xfe")

        self.assertEqual("invalid", event["type"])
        self.assertIsNotNone(result)
        self.assertEqual("no_move", result["command"])
        self.assertEqual("invalid_utf8:websocket_message", result["reason"])


class CommandEmitterTests(unittest.TestCase):
    def test_dedupe_emits_only_command_transitions(self) -> None:
        output: list[dict[str, Any]] = []
        emitter = CommandEmitter(dedupe=True, output=output.append)

        try:
            for label, label_text in [
                (0, "SEM MOVIMENTO"),
                (0, "SEM MOVIMENTO"),
                (1, "ESQUERDA"),
                (1, "ESQUERDA"),
                (2, "DIREITA"),
            ]:
                message = interpret_websocket_message(
                    json.dumps(
                        inference_event(label=label, label_text=label_text)
                    )
                )
                self.assertIsNotNone(message)
                emitter.emit(message)
        finally:
            emitter.close()

        self.assertEqual(
            ["no_move", "left", "right"],
            [message["command"] for message in output],
        )


class WebSocketIntegrationTests(unittest.IsolatedAsyncioTestCase):
    async def test_server_messages_reach_same_interpreter(self) -> None:
        outbound = [
            json.dumps({"type": "started", "mode": "screen"}),
            json.dumps(inference_event()),
            '{"type":"inference",',
            json.dumps(
                inference_event(label=2, label_text="DIREITA")
            ).encode("utf-8"),
        ]

        async def handler(websocket: Any, *_: Any) -> None:
            for message in outbound:
                await websocket.send(message)

        received_commands: list[dict[str, Any]] = []
        async with serve(handler, "127.0.0.1", 0) as server:
            port = server.sockets[0].getsockname()[1]
            count = await receive_once(
                f"ws://127.0.0.1:{port}",
                received_commands.append,
            )

        self.assertEqual(4, count)
        self.assertEqual(
            ["left", "no_move", "right"],
            [message["command"] for message in received_commands],
        )
        self.assertEqual(
            ["accepted", "invalid", "accepted"],
            [message["status"] for message in received_commands],
        )

    async def test_real_jsonl_replay_over_websocket(self) -> None:
        source_messages = [
            line
            for line in REAL_JSONL.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        async def handler(websocket: Any, *_: Any) -> None:
            for message in source_messages:
                await websocket.send(message)

        received_commands: list[dict[str, Any]] = []
        async with serve(handler, "127.0.0.1", 0) as server:
            port = server.sockets[0].getsockname()[1]
            count = await receive_once(
                f"ws://127.0.0.1:{port}",
                received_commands.append,
            )

        commands = [message["command"] for message in received_commands]
        self.assertEqual(15, count)
        self.assertEqual(14, len(commands))
        self.assertEqual(6, commands.count("no_move"))
        self.assertEqual(5, commands.count("left"))
        self.assertEqual(3, commands.count("right"))

    async def test_disconnect_emits_safe_no_move(self) -> None:
        async def handler(websocket: Any, *_: Any) -> None:
            await websocket.send(json.dumps(inference_event()))

        output: list[dict[str, Any]] = []
        emitter = CommandEmitter(output=output.append)

        try:
            async with serve(handler, "127.0.0.1", 0) as server:
                port = server.sockets[0].getsockname()[1]
                result = await run_receiver(
                    f"ws://127.0.0.1:{port}",
                    emitter,
                    reconnect=False,
                )
        finally:
            emitter.close()

        self.assertEqual(0, result)
        self.assertEqual(["left", "no_move"], [item["command"] for item in output])
        self.assertEqual("error", output[-1]["status"])
        self.assertEqual("websocket_disconnected", output[-1]["reason"])


if __name__ == "__main__":
    unittest.main()

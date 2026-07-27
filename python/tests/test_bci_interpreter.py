from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from bci_jsonl_to_unity_commands import iter_jsonl, normalize_command


REAL_JSONL = PROJECT_ROOT / "bci_stream_example.jsonl"


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


class NormalizeCommandTests(unittest.TestCase):
    def test_started_does_not_emit_movement(self) -> None:
        result = normalize_command(
            {
                "type": "started",
                "sim": True,
                "mode": "screen",
                "modality": "mi",
                "threshold": 0.45,
            }
        )

        self.assertIsNone(result)

    def test_valid_label_pairs_map_to_expected_commands(self) -> None:
        cases = [
            (0, "SEM MOVIMENTO", "no_move"),
            (1, "ESQUERDA", "left"),
            (2, "DIREITA", "right"),
        ]

        for label, label_text, expected_command in cases:
            with self.subTest(label=label, label_text=label_text):
                result = normalize_command(
                    inference_event(label=label, label_text=label_text)
                )

                self.assertIsNotNone(result)
                self.assertEqual(expected_command, result["command"])
                self.assertEqual("accepted", result["status"])

    def test_final_label_is_not_recalculated_from_p_move(self) -> None:
        result = normalize_command(
            inference_event(
                label=1,
                label_text="ESQUERDA",
                raw_pred=0,
                is_mi=True,
                p_move=0.32,
                tau=0.45,
            )
        )

        self.assertIsNotNone(result)
        self.assertEqual("left", result["command"])
        self.assertEqual("accepted", result["status"])

    def test_rejected_inference_emits_safe_command_and_reason(self) -> None:
        result = normalize_command(
            {
                "type": "inference",
                "rejected": True,
                "reason": "baixa confiança",
            }
        )

        self.assertIsNotNone(result)
        self.assertEqual("no_move", result["command"])
        self.assertEqual("rejected", result["status"])
        self.assertEqual("baixa confiança", result["reason"])

    def test_inconsistent_label_pair_is_invalid(self) -> None:
        result = normalize_command(
            inference_event(label=1, label_text="DIREITA")
        )

        self.assertIsNotNone(result)
        self.assertEqual("no_move", result["command"])
        self.assertEqual("invalid", result["status"])
        self.assertIn("label_label_text_mismatch", result["reason"])

    def test_unknown_class_is_invalid(self) -> None:
        result = normalize_command(
            inference_event(label=99, label_text="NOVA CLASSE")
        )

        self.assertIsNotNone(result)
        self.assertEqual("no_move", result["command"])
        self.assertEqual("invalid", result["status"])
        self.assertIn("unknown_class", result["reason"])

    def test_missing_required_field_is_invalid(self) -> None:
        event = inference_event()
        del event["label_text"]

        result = normalize_command(event)

        self.assertIsNotNone(result)
        self.assertEqual("no_move", result["command"])
        self.assertEqual("invalid", result["status"])
        self.assertEqual("missing_field:label_text", result["reason"])

    def test_wrong_field_types_are_invalid_instead_of_crashing(self) -> None:
        cases = [
            ("rejected", "true"),
            ("label", "1"),
            ("label_text", 1),
            ("is_mi", "false"),
            ("p_move", "abc"),
            ("tau", []),
        ]

        for field, invalid_value in cases:
            with self.subTest(field=field, invalid_value=invalid_value):
                result = normalize_command(
                    inference_event(**{field: invalid_value})
                )

                self.assertIsNotNone(result)
                self.assertEqual("no_move", result["command"])
                self.assertEqual("invalid", result["status"])
                self.assertIn(f"invalid_type:{field}", result["reason"])

    def test_error_event_emits_safe_command(self) -> None:
        result = normalize_command(
            {
                "type": "error",
                "message": "classificador indisponível",
            }
        )

        self.assertIsNotNone(result)
        self.assertEqual("no_move", result["command"])
        self.assertEqual("error", result["status"])
        self.assertEqual("classificador indisponível", result["reason"])

    def test_threshold_event_does_not_emit_movement(self) -> None:
        result = normalize_command(
            {
                "type": "threshold",
                "threshold": 0.5,
            }
        )

        self.assertIsNone(result)

    def test_unknown_event_type_is_invalid(self) -> None:
        result = normalize_command({"type": "mystery"})

        self.assertIsNotNone(result)
        self.assertEqual("no_move", result["command"])
        self.assertEqual("invalid", result["status"])
        self.assertEqual("unknown_event_type:mystery", result["reason"])


class JsonlReplayTests(unittest.TestCase):
    def test_malformed_json_becomes_safe_invalid_event(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "invalid.jsonl"
            path.write_text(
                '{"type":"started"}\n{"type":"inference",\n',
                encoding="utf-8",
            )

            events = list(iter_jsonl(path))

        self.assertEqual(2, len(events))
        result = normalize_command(events[1])
        self.assertIsNotNone(result)
        self.assertEqual("no_move", result["command"])
        self.assertEqual("invalid", result["status"])
        self.assertIn("invalid_json:line=2", result["reason"])

    def test_real_jsonl_produces_expected_command_sequence(self) -> None:
        messages = [
            normalize_command(event)
            for event in iter_jsonl(REAL_JSONL)
        ]
        commands = [
            message["command"]
            for message in messages
            if message is not None
        ]

        self.assertEqual(
            [
                "no_move",
                "no_move",
                "left",
                "left",
                "left",
                "left",
                "left",
                "no_move",
                "no_move",
                "no_move",
                "no_move",
                "right",
                "right",
                "right",
            ],
            commands,
        )


if __name__ == "__main__":
    unittest.main()

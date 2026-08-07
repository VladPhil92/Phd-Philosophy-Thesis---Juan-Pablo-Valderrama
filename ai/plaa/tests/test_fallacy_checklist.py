"""Tests for plaa.fallacy_checklist — the closed catalogue and vocabulary guard."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from plaa.fallacy_checklist import Confidence, FallacyVerdict, is_known_fallacy, is_valid_confidence  # noqa: E402


class CatalogueTests(unittest.TestCase):
    def test_known_fallacy_recognized(self) -> None:
        self.assertTrue(is_known_fallacy("circularity"))

    def test_unknown_fallacy_rejected(self) -> None:
        self.assertFalse(is_known_fallacy("made_up_fallacy"))

    def test_confidence_vocabulary_matches_specification(self) -> None:
        self.assertEqual(
            {item.value for item in Confidence}, {"POSSIBLE", "LIKELY", "UNLIKELY", "NOT_DETECTED"}
        )

    def test_arbitrary_certainty_language_is_invalid(self) -> None:
        self.assertFalse(is_valid_confidence("DEFINITELY_A_FALLACY"))


class FallacyVerdictTests(unittest.TestCase):
    def test_not_detected_requires_no_justification(self) -> None:
        verdict = FallacyVerdict("circularity", "NOT_DETECTED")
        self.assertEqual(verdict.verdict, "NOT_DETECTED")

    def test_possible_requires_justification(self) -> None:
        with self.assertRaises(ValueError):
            FallacyVerdict("circularity", "POSSIBLE", justification="")

    def test_possible_with_justification_is_accepted(self) -> None:
        verdict = FallacyVerdict(
            "circularity", "POSSIBLE", justification="La premisa 2 repite la conclusión (ARG-000#Inferencia)."
        )
        self.assertEqual(verdict.verdict, "POSSIBLE")

    def test_unknown_fallacy_name_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            FallacyVerdict("made_up_fallacy", "NOT_DETECTED")

    def test_invalid_confidence_value_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            FallacyVerdict("circularity", "DEFINITELY")


if __name__ == "__main__":
    unittest.main()

"""Tests for quote_audit.schema_check — structural validation only, no
real philosophical judgment. The 10 cases below are the exact list
requested when this component was specified."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from quote_audit import schema_check  # noqa: E402

KNOWN_KEYS = {"derrida-2023-hospitality", "derrida-2008-animal", "derrida-2010-bestia-soberano-1"}


def _valid_record(**overrides: object) -> dict[str, object]:
    record: dict[str, object] = {
        "quote_id": "derrida-2023-hospitality#c56",
        "source": "derrida-2023-hospitality",
        "locator": "p. 232",
        "recommended_status": "SOURCE_LOCATED",
    }
    record.update(overrides)
    return record


class RequiredFieldsTests(unittest.TestCase):
    def test_minimal_valid_record_passes(self) -> None:
        self.assertEqual(schema_check.validate_quote_audit_record(_valid_record()), [])

    def test_1_quote_without_locator_is_rejected(self) -> None:
        record = _valid_record()
        del record["locator"]
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("locator" in error for error in errors))

    def test_2_quote_without_source_is_rejected(self) -> None:
        record = _valid_record()
        del record["source"]
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("source" in error for error in errors))


class Apa7Tests(unittest.TestCase):
    def test_3_forty_plus_word_quote_requires_block_type(self) -> None:
        long_quote = " ".join(["palabra"] * 45)
        record = _valid_record(apa7_quote_type="short")
        errors = schema_check.validate_quote_audit_record(record, quoted_text=long_quote)
        self.assertTrue(any("BLOCK_QUOTE_REQUIRED" in error for error in errors))

    def test_3b_forty_plus_word_quote_with_block_type_passes(self) -> None:
        long_quote = " ".join(["palabra"] * 45)
        record = _valid_record(apa7_quote_type="block")
        errors = schema_check.validate_quote_audit_record(record, quoted_text=long_quote)
        self.assertEqual(errors, [])

    def test_10_invalid_apa7_status_is_rejected(self) -> None:
        record = _valid_record(apa7_compliant="mostly")
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("apa7_compliant inválido" in error for error in errors))

    def test_10b_invalid_apa7_quote_type_is_rejected(self) -> None:
        record = _valid_record(apa7_quote_type="medium")
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("apa7_quote_type inválido" in error for error in errors))


class BibliographyResolutionTests(unittest.TestCase):
    def test_4_quote_linked_to_nonexistent_bibtex_key_is_rejected(self) -> None:
        record = _valid_record(source="derrida-1999-inexistente")
        errors = schema_check.validate_quote_audit_record(record, known_bibliography_keys=KNOWN_KEYS)
        self.assertTrue(any("no corresponde a ninguna clave" in error for error in errors))

    def test_4b_quote_linked_to_real_bibtex_key_passes(self) -> None:
        record = _valid_record(source="derrida-2008-animal")
        errors = schema_check.validate_quote_audit_record(record, known_bibliography_keys=KNOWN_KEYS)
        self.assertEqual(errors, [])


class HumanMarkerTests(unittest.TestCase):
    def test_5_human_verified_status_without_marker_is_rejected(self) -> None:
        record = _valid_record(recommended_status="HUMAN_VERIFIED")
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("human_verified: true explícito" in error for error in errors))

    def test_5b_human_verified_status_with_explicit_marker_passes(self) -> None:
        record = _valid_record(recommended_status="HUMAN_VERIFIED", human_verified=True)
        errors = schema_check.validate_quote_audit_record(record)
        self.assertEqual(errors, [])

    def test_6_ready_for_argument_use_without_context_audit_is_rejected(self) -> None:
        record = _valid_record(recommended_status="READY_FOR_ARGUMENT_USE", human_verified=True)
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("requiere 'context_status'" in error for error in errors))
        self.assertTrue(any("requiere 'philosophical_function'" in error for error in errors))

    def test_7_context_audited_without_philosophical_function_is_rejected(self) -> None:
        record = _valid_record(recommended_status="CONTEXT_AUDITED", context_status="SELF_CONTAINED")
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("requiere 'philosophical_function'" in error for error in errors))


class ArgumentativeSupportConflictTests(unittest.TestCase):
    def test_8_no_support_used_as_primary_evidence_is_rejected(self) -> None:
        record = _valid_record(
            recommended_status="RELEVANCE_AUDITED",
            context_status="SELF_CONTAINED",
            philosophical_function="TEXTUAL_EVIDENCE",
            relevance_status="LOW",
            reasoning_summary="No respalda la premisa 2.",
            related_ARG=["ARG-001"],
            argumentative_support="NO_SUPPORT",
            primary_evidence=True,
        )
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("CONFLICT" in error for error in errors))

    def test_8b_no_support_as_illustrative_only_does_not_conflict(self) -> None:
        record = _valid_record(
            recommended_status="RELEVANCE_AUDITED",
            context_status="SELF_CONTAINED",
            philosophical_function="TEXTUAL_EVIDENCE",
            relevance_status="LOW",
            reasoning_summary="Solo ilustrativa, no respalda la premisa.",
            related_ARG=["ARG-001"],
            argumentative_support="NO_SUPPORT",
            primary_evidence=False,
        )
        errors = schema_check.validate_quote_audit_record(record)
        self.assertEqual(errors, [])

    def test_related_arg_without_argumentative_support_is_rejected(self) -> None:
        record = _valid_record(related_ARG=["ARG-001"])
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("no declara 'argumentative_support'" in error for error in errors))


class ClassificationTests(unittest.TestCase):
    def test_9_invalid_classification_is_rejected(self) -> None:
        record = _valid_record(classification="PROBABLY_FINE")
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("classification inválida" in error for error in errors))

    def test_9b_valid_classification_passes(self) -> None:
        record = _valid_record(classification="VERIFIED_RELEVANT")
        errors = schema_check.validate_quote_audit_record(record)
        self.assertEqual(errors, [])

    def test_invalid_recommended_status_is_rejected(self) -> None:
        record = _valid_record(recommended_status="ALMOST_READY")
        errors = schema_check.validate_quote_audit_record(record)
        self.assertTrue(any("recommended_status inválido" in error for error in errors))


class RejectedForUseIsTerminalTests(unittest.TestCase):
    def test_rejected_for_use_does_not_require_context_audit(self) -> None:
        record = _valid_record(recommended_status="REJECTED_FOR_USE")
        errors = schema_check.validate_quote_audit_record(record)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()

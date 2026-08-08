"""Tests for plaa.schema_check — structural validation only, no real ARG-* content."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from plaa import schema_check  # noqa: E402

FIXTURE = Path(__file__).parent / "fixtures" / "ARG-EXAMPLE-000.md"


class ValidateArgumentFrontmatterTests(unittest.TestCase):
    def test_fixture_is_structurally_valid(self) -> None:
        self.assertEqual(schema_check.validate_argument_file(FIXTURE), [])

    def test_missing_required_field_is_reported(self) -> None:
        errors = schema_check.validate_argument_frontmatter({"argument_id": "ARG-001", "status": "IDEA"})
        self.assertTrue(any("human_validation" in error for error in errors))

    def test_invalid_status_is_reported(self) -> None:
        errors = schema_check.validate_argument_frontmatter(
            {"argument_id": "ARG-001", "status": "NOT_A_STATUS", "human_validation": "pending"}
        )
        self.assertTrue(any("status inválido" in error for error in errors))

    def test_validated_without_human_validation_marker_is_rejected(self) -> None:
        errors = schema_check.validate_argument_frontmatter(
            {"argument_id": "ARG-001", "status": "VALIDATED", "human_validation": "pending"}
        )
        self.assertTrue(any("VALIDATED" in error for error in errors))

    def test_validated_with_explicit_marker_passes(self) -> None:
        errors = schema_check.validate_argument_frontmatter(
            {"argument_id": "ARG-001", "status": "VALIDATED", "human_validation": "validated"}
        )
        self.assertEqual(errors, [])

    def test_malformed_argument_id_is_rejected(self) -> None:
        errors = schema_check.validate_argument_frontmatter(
            {"argument_id": "banana", "status": "IDEA", "human_validation": "pending"}
        )
        self.assertTrue(any("argument_id con formato inválido" in error for error in errors))

    def test_well_formed_argument_id_passes(self) -> None:
        errors = schema_check.validate_argument_frontmatter(
            {"argument_id": "ARG-042", "status": "IDEA", "human_validation": "pending"}
        )
        self.assertEqual(errors, [])


class ValidateAnalysisReportFrontmatterTests(unittest.TestCase):
    def _valid_report(self) -> dict[str, str]:
        return {
            "argument_id": "ARG-001",
            "module": "fallacy_analyzer",
            "logical_status": "INCOMPLETE",
            "confidence": "UNLIKELY",
            "human_review_required": "true",
            "report_status": "DEVELOPMENT_REQUIRED",
        }

    def test_valid_report_has_no_errors(self) -> None:
        self.assertEqual(schema_check.validate_analysis_report_frontmatter(self._valid_report()), [])

    def test_report_status_validated_is_always_rejected(self) -> None:
        report = self._valid_report()
        report["report_status"] = "VALIDATED"
        errors = schema_check.validate_analysis_report_frontmatter(report)
        self.assertTrue(any("VALIDATED" in error for error in errors))

    def test_human_review_required_false_is_rejected(self) -> None:
        report = self._valid_report()
        report["human_review_required"] = "false"
        errors = schema_check.validate_analysis_report_frontmatter(report)
        self.assertTrue(any("human_review_required" in error for error in errors))

    def test_unknown_module_is_rejected(self) -> None:
        report = self._valid_report()
        report["module"] = "made_up_module"
        errors = schema_check.validate_analysis_report_frontmatter(report)
        self.assertTrue(any("module inválido" in error for error in errors))


class ValidateAnalysisReportBodyTests(unittest.TestCase):
    def test_missing_headings_are_reported(self) -> None:
        errors = schema_check.validate_analysis_report_body({})
        self.assertTrue(any("Problemas detectados" in error for error in errors))
        self.assertTrue(any("Referencias del repositorio" in error for error in errors))

    def test_references_heading_without_list_items_is_rejected(self) -> None:
        sections = {
            "Problemas detectados": "Sin problemas detectados en este análisis.",
            "Referencias del repositorio": "(sin referencias todavía)",
        }
        errors = schema_check.validate_analysis_report_body(sections)
        self.assertTrue(any("repository_references no puede estar vacío" in error for error in errors))

    def test_references_heading_with_list_items_passes(self) -> None:
        sections = {
            "Problemas detectados": "Sin problemas detectados en este análisis.",
            "Referencias del repositorio": "- research/argument-ledger/ARG-900001.md",
        }
        self.assertEqual(schema_check.validate_analysis_report_body(sections), [])


class ValidateAnalysisReportFileEndToEndTests(unittest.TestCase):
    def test_report_without_references_section_fails_even_with_valid_frontmatter(self) -> None:
        content = (
            "---\n"
            "argument_id: ARG-900001\n"
            "module: fallacy_analyzer\n"
            "logical_status: INCOMPLETE\n"
            "confidence: UNLIKELY\n"
            "human_review_required: true\n"
            "report_status: DEVELOPMENT_REQUIRED\n"
            "---\n\n"
            "# Informe incompleto (sin secciones obligatorias del cuerpo)\n"
        )
        import tempfile

        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as handle:
            handle.write(content)
            path = handle.name
        try:
            errors = schema_check.validate_analysis_report_file(path)
        finally:
            Path(path).unlink()
        self.assertTrue(any("Problemas detectados" in error for error in errors))
        self.assertTrue(any("Referencias del repositorio" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

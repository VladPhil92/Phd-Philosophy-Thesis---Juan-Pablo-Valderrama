"""Tests for plaa.report — structural validation and rendering only."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from plaa.report import AnalysisReport, DetectedProblem, FormalizationRecord  # noqa: E402
from plaa.fallacy_checklist import FallacyVerdict  # noqa: E402
from plaa.schema_check import validate_analysis_report_body, validate_analysis_report_frontmatter  # noqa: E402
from plaa.miner import parse_frontmatter, parse_sections  # noqa: E402


def _valid_report() -> AnalysisReport:
    return AnalysisReport(
        argument_id="ARG-900001",
        module="fallacy_analyzer",
        logical_status="INCOMPLETE",
        confidence="UNLIKELY",
        repository_references=["research/argument-ledger/ARG-900001.md"],
    )


class AnalysisReportValidationTests(unittest.TestCase):
    def test_minimal_valid_report_has_no_errors(self) -> None:
        self.assertEqual(_valid_report().validate(), [])

    def test_report_status_validated_is_rejected(self) -> None:
        report = _valid_report()
        report.report_status = "VALIDATED"
        self.assertTrue(any("VALIDATED" in error for error in report.validate()))

    def test_human_review_required_must_be_true(self) -> None:
        report = _valid_report()
        report.human_review_required = False
        self.assertTrue(any("human_review_required" in error for error in report.validate()))

    def test_empty_repository_references_is_rejected(self) -> None:
        report = _valid_report()
        report.repository_references = []
        self.assertTrue(any("repository_references" in error for error in report.validate()))

    def test_detected_problem_without_evidence_location_is_rejected(self) -> None:
        report = _valid_report()
        report.detected_problems = [
            DetectedProblem(
                description="posible circularidad",
                evidence_location="",
                confidence="POSSIBLE",
                reviewed_as_possible_aporia=True,
            )
        ]
        self.assertTrue(any("evidence_location" in error for error in report.validate()))

    def test_well_formed_detected_problem_passes(self) -> None:
        report = _valid_report()
        report.detected_problems = [
            DetectedProblem(
                description="posible circularidad",
                evidence_location="research/argument-ledger/ARG-900001.md#Inferencia",
                confidence="POSSIBLE",
                reviewed_as_possible_aporia=True,
            )
        ]
        self.assertEqual(report.validate(), [])

    def test_formalizer_module_without_formalization_is_rejected(self) -> None:
        report = _valid_report()
        report.module = "formalizer"
        self.assertTrue(any("formalizer" in error for error in report.validate()))

    def test_formalizer_module_with_formalization_passes(self) -> None:
        report = _valid_report()
        report.module = "formalizer"
        report.formalization = FormalizationRecord(level="propositional", notation="P1, P2 |- C")
        self.assertEqual(report.validate(), [])

    def test_non_provisional_formalization_is_rejected(self) -> None:
        # Principle 5: every formalization remains provisional until a human approves it.
        report = _valid_report()
        report.module = "formalizer"
        report.formalization = FormalizationRecord(
            level="propositional", notation="P1, P2 |- C", provisional=False
        )
        self.assertTrue(any("provisional" in error for error in report.validate()))

    def test_invalid_formalization_level_is_rejected(self) -> None:
        report = _valid_report()
        report.module = "formalizer"
        report.formalization = FormalizationRecord(level="astrology", notation="whatever")
        self.assertTrue(any("formalization.level" in error for error in report.validate()))

    def test_possible_fallacies_reuses_fallacy_verdict_validation(self) -> None:
        # FallacyVerdict validates itself at construction: an AnalysisReport can never
        # hold a malformed fallacy finding, so report.validate() needs no extra check.
        with self.assertRaises(ValueError):
            FallacyVerdict("not_a_real_fallacy", "POSSIBLE", "irrelevant")

    def test_well_formed_possible_fallacy_passes(self) -> None:
        report = _valid_report()
        report.possible_fallacies = [
            FallacyVerdict(
                "begging_the_question",
                "POSSIBLE",
                "La premisa 2 presupone la conclusión (ARG-900001.md#Inferencia).",
            )
        ]
        self.assertEqual(report.validate(), [])


class AnalysisReportRenderingTests(unittest.TestCase):
    def test_rendered_markdown_round_trips_through_frontmatter_parser(self) -> None:
        report = _valid_report()
        rendered = report.to_markdown()
        frontmatter = parse_frontmatter(rendered)
        self.assertEqual(frontmatter["argument_id"], "ARG-900001")
        self.assertEqual(frontmatter["module"], "fallacy_analyzer")
        self.assertEqual(validate_analysis_report_frontmatter(frontmatter), [])

    def test_rendered_markdown_never_contains_validated_report_status(self) -> None:
        report = _valid_report()
        rendered = report.to_markdown()
        self.assertNotIn("report_status: VALIDATED", rendered)

    def test_rendered_markdown_satisfies_body_section_validation(self) -> None:
        # Regression check: schema_check validates detected_problems/repository_references
        # from the Markdown body, not just the frontmatter — a rendered report must
        # actually satisfy that, not just look complete.
        report = _valid_report()
        rendered = report.to_markdown()
        self.assertEqual(validate_analysis_report_body(parse_sections(rendered)), [])

    def test_rendered_formalizer_report_satisfies_module_conditional_body_validation(self) -> None:
        report = _valid_report()
        report.module = "formalizer"
        report.formalization = FormalizationRecord(level="propositional", notation="P1, P2 |- C")
        rendered = report.to_markdown()
        self.assertEqual(validate_analysis_report_body(parse_sections(rendered), module="formalizer"), [])

    def test_rendered_report_includes_concept_ambiguity_references(self) -> None:
        report = _valid_report()
        report.module = "concept_consistency"
        report.concept_ambiguity = ["research/sources/notes/derrida-1997-hospitalite.md#Conceptos"]
        rendered = report.to_markdown()
        self.assertIn("research/sources/notes/derrida-1997-hospitalite.md#Conceptos", rendered)
        self.assertEqual(validate_analysis_report_body(parse_sections(rendered), module="concept_consistency"), [])

    def test_rendered_report_includes_possible_fallacies_table(self) -> None:
        report = _valid_report()
        report.possible_fallacies = [
            FallacyVerdict("equivocation", "UNLIKELY", "El término se usa de forma consistente en el pasaje.")
        ]
        rendered = report.to_markdown()
        self.assertIn("equivocation", rendered)
        self.assertIn("UNLIKELY", rendered)


if __name__ == "__main__":
    unittest.main()

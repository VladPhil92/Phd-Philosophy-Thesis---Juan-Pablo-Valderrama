"""Tests for plaa.report — structural validation and rendering only."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from plaa.report import AnalysisReport, DetectedProblem  # noqa: E402
from plaa.schema_check import validate_analysis_report_frontmatter  # noqa: E402
from plaa.miner import parse_frontmatter  # noqa: E402


def _valid_report() -> AnalysisReport:
    return AnalysisReport(
        argument_id="ARG-EXAMPLE-000",
        module="fallacy_analyzer",
        logical_status="INCOMPLETE",
        confidence="UNLIKELY",
        repository_references=["research/argument-ledger/ARG-EXAMPLE-000.md"],
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
                evidence_location="research/argument-ledger/ARG-EXAMPLE-000.md#Inferencia",
                confidence="POSSIBLE",
                reviewed_as_possible_aporia=True,
            )
        ]
        self.assertEqual(report.validate(), [])


class AnalysisReportRenderingTests(unittest.TestCase):
    def test_rendered_markdown_round_trips_through_frontmatter_parser(self) -> None:
        report = _valid_report()
        rendered = report.to_markdown()
        frontmatter = parse_frontmatter(rendered)
        self.assertEqual(frontmatter["argument_id"], "ARG-EXAMPLE-000")
        self.assertEqual(frontmatter["module"], "fallacy_analyzer")
        self.assertEqual(validate_analysis_report_frontmatter(frontmatter), [])

    def test_rendered_markdown_never_contains_validated_report_status(self) -> None:
        report = _valid_report()
        rendered = report.to_markdown()
        self.assertNotIn("report_status: VALIDATED", rendered)


if __name__ == "__main__":
    unittest.main()

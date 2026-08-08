"""Tests for plaa.validator_interfaces — confirms the null engine is honest,
never a disguised guess."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from plaa.validator_interfaces import (  # noqa: E402
    FormalArgument,
    LogicalStatus,
    LogicalValidatorEngine,
    NullValidatorEngine,
)


class NullValidatorEngineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = NullValidatorEngine()
        self.argument = FormalArgument(premises=("P1", "P2"), conclusion="C", level="propositional")

    def test_satisfies_the_protocol(self) -> None:
        self.assertIsInstance(self.engine, LogicalValidatorEngine)

    def test_never_reports_valid_or_invalid(self) -> None:
        verdict = self.engine.check(self.argument)
        self.assertEqual(verdict.status, LogicalStatus.INCOMPLETE)
        self.assertNotIn(verdict.status, {LogicalStatus.VALID, LogicalStatus.INVALID})

    def test_explanation_names_the_missing_engine(self) -> None:
        verdict = self.engine.check(self.argument)
        self.assertIn("no hay motor", verdict.explanation.lower())


class FakeEngine:
    """Minimal stand-in proving a third-party engine can satisfy the protocol
    without modifying plaa itself (Open/Closed, Liskov substitution)."""

    name = "fake-sat"

    def check(self, argument: FormalArgument):  # noqa: ANN201 - test double
        from plaa.validator_interfaces import ValidatorVerdict

        return ValidatorVerdict(status=LogicalStatus.SATISFIABLE, explanation="stub", engine_name=self.name)


class SubstitutabilityTests(unittest.TestCase):
    def test_any_conforming_engine_is_substitutable(self) -> None:
        engine: LogicalValidatorEngine = FakeEngine()
        argument = FormalArgument(premises=("P1",), conclusion="C", level="propositional")
        verdict = engine.check(argument)
        self.assertEqual(verdict.status, LogicalStatus.SATISFIABLE)


if __name__ == "__main__":
    unittest.main()

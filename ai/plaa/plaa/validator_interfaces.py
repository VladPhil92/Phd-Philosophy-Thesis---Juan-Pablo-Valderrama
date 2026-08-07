"""Module 4 — Logical Validator interface.

Defines the contract future symbolic-reasoning engines (SAT/SMT solvers,
Prolog, Lean, Coq, Z3...) must implement. No engine is hardcoded or
bundled: the only implementation shipped today is ``NullValidatorEngine``,
which honestly reports that no symbolic verification happened, instead of
faking one with a heuristic. See ROADMAP.md for when integrating a real
engine would be justified.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Protocol, runtime_checkable


class LogicalStatus(str, Enum):
    """The closed vocabulary a validator engine may report."""

    VALID = "VALID"
    INVALID = "INVALID"
    SATISFIABLE = "SATISFIABLE"
    UNSATISFIABLE = "UNSATISFIABLE"
    UNKNOWN = "UNKNOWN"
    INCOMPLETE = "INCOMPLETE"
    MISSING_PREMISE = "MISSING_PREMISE"
    NOT_APPLICABLE = "NOT_APPLICABLE"


@dataclass(frozen=True)
class FormalArgument:
    """The minimal input a validator engine needs: premises and a conclusion.

    ``notation`` is free text (e.g. an SMT-LIB string, a Prolog clause
    list); this package does not parse or interpret it — a concrete engine
    implementation is responsible for that.
    """

    premises: tuple[str, ...]
    conclusion: str
    level: str  # "propositional" | "predicate" | "modal" | "deontic"
    notation: str = ""


@dataclass(frozen=True)
class ValidatorVerdict:
    """The result a LogicalValidatorEngine must return."""

    status: LogicalStatus
    explanation: str
    engine_name: str


@runtime_checkable
class LogicalValidatorEngine(Protocol):
    """Contract every future symbolic engine integration must satisfy.

    Deliberately minimal (Interface Segregation): one method, one
    responsibility. Any concrete implementation (SAT, SMT, Prolog, Lean,
    Coq, Z3...) is a drop-in replacement wherever this protocol is
    expected (Liskov substitution) — see DEVELOPER-GUIDE.md for how to add
    one.
    """

    name: str

    def check(self, argument: FormalArgument) -> ValidatorVerdict:
        """Evaluate a formalized argument and return a verdict."""
        ...


class NullValidatorEngine:
    """Default engine: always honest about not performing real verification.

    This is not a placeholder pretending to work — it is the correct
    behavior when ``CONFIG.yaml: symbolic_engine`` is ``none``. Returning
    ``INCOMPLETE`` here (rather than guessing) is what keeps Module 4 from
    becoming exactly the kind of "AI magic" this component must avoid.
    """

    name = "none"

    def check(self, argument: FormalArgument) -> ValidatorVerdict:
        return ValidatorVerdict(
            status=LogicalStatus.INCOMPLETE,
            explanation=(
                "No hay motor de validación simbólica configurado "
                "(CONFIG.yaml: symbolic_engine: none). Véase ai/plaa/ROADMAP.md."
            ),
            engine_name=self.name,
        )

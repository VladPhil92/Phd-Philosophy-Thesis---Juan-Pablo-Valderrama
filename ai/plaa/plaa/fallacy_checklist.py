"""Module 5 support — the closed fallacy catalogue and confidence vocabulary.

This module holds no detection logic. Detecting a fallacy requires reading
and judgment, which belongs to a human-reviewed Claude Code session guided
by ``prompts/05-fallacy-analyzer.md``, never to keyword matching dressed up
as semantic analysis (see ARCHITECTURE.md). What this module *does*
enforce, mechanically, is that any fallacy-analysis output only uses the
closed catalogue and the closed confidence vocabulary.
"""

from __future__ import annotations

from enum import Enum


class Confidence(str, Enum):
    """The only vocabulary a PLAA judgment module may use for a verdict."""

    POSSIBLE = "POSSIBLE"
    LIKELY = "LIKELY"
    UNLIKELY = "UNLIKELY"
    NOT_DETECTED = "NOT_DETECTED"


# Closed catalogue, matching the PLAA specification exactly. Extending it
# is a documentation change (this file + fallacy-checklist.md +
# analysis-report schema), not a runtime configuration option.
FALLACY_CATALOGUE: tuple[str, ...] = (
    "ad_hominem",
    "strawman",
    "false_dilemma",
    "begging_the_question",
    "affirming_the_consequent",
    "denying_the_antecedent",
    "equivocation",
    "false_cause",
    "composition",
    "division",
    "circularity",
    "hasty_generalization",
    "appeal_to_authority",
)


def is_known_fallacy(name: str) -> bool:
    return name in FALLACY_CATALOGUE


def is_valid_confidence(value: str) -> bool:
    return value in {item.value for item in Confidence}


class FallacyVerdict:
    """A single row of a completed fallacy-checklist.md, validated structurally."""

    __slots__ = ("fallacy", "verdict", "justification")

    def __init__(self, fallacy: str, verdict: str, justification: str = "") -> None:
        if not is_known_fallacy(fallacy):
            raise ValueError(f"Falacia no reconocida en el catálogo cerrado: {fallacy!r}")
        if not is_valid_confidence(verdict):
            raise ValueError(
                f"Veredicto fuera del vocabulario permitido {sorted(c.value for c in Confidence)}: {verdict!r}"
            )
        if verdict != Confidence.NOT_DETECTED.value and not justification.strip():
            raise ValueError(
                f"El veredicto {verdict!r} para {fallacy!r} requiere justificación textual "
                "(Principio 6: la evidencia precede a la inferencia)."
            )
        self.fallacy = fallacy
        self.verdict = verdict
        self.justification = justification

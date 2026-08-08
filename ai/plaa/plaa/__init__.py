"""PLAA — Philosophical Logic & Argument Auditor.

Deterministic, dependency-free helpers that support (but never replace)
the human-reviewed audit prompts in ``ai/plaa/prompts/``. See
``ai/plaa/ARCHITECTURE.md`` for the design rationale: this package only
implements tasks that are mechanically verifiable. Anything requiring
semantic judgment (fallacy detection, formalization, stress-testing,
concept-drift judgment) lives in prompt templates, not in code.
"""

from __future__ import annotations

__version__ = "0.1.0"

__all__ = ["__version__"]

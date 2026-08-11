"""Quote Audit — deterministic structural layer for citation audits.

See ../README.md and ../ARCHITECTURE.md for what this package is and is
not. It validates form (fields, enums, locks); it never judges whether a
quote is philosophically relevant, contextually faithful, or genuinely
supports an argument — that judgment lives in ../prompts/*.md and always
requires human review.
"""

from __future__ import annotations

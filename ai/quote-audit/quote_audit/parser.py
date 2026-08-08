"""Deterministic parsing: extract quote-audit blocks from a ficha-fuente.md
and resolve BibTeX keys from research/sources/bibliography.bib.

Mirrors ai/plaa/plaa/miner.py's approach: only flat ``key: value`` lines
already delimited by a heading are parsed. No inference of structure that
is not already explicit in the Markdown.
"""

from __future__ import annotations

import re
from pathlib import Path

_QUOTE_AUDIT_HEADING = re.compile(r"^#{3,6}\s+Auditoría de citas\b.*$", re.MULTILINE)
_ANY_HEADING = re.compile(r"^#{1,6}\s+\S", re.MULTILINE)
_FLAT_FIELD = re.compile(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)$", re.MULTILINE)
_LIST_SEP = re.compile(r"\s*,\s*")

# BibTeX entry keys, e.g. "@book{derrida-2023-hospitality," -> "derrida-2023-hospitality"
_BIBTEX_KEY = re.compile(r"^@\w+\{\s*([^,\s]+)\s*,", re.MULTILINE)

LIST_FIELDS = frozenset({"related_PI", "related_ARG", "risks"})


def parse_quote_audit_blocks(content: str) -> list[dict[str, str | list[str]]]:
    """Return one dict per "Auditoría de citas" block found in ``content``.

    Each block is the flat ``key: value`` region between a heading matching
    ``_QUOTE_AUDIT_HEADING`` and the next heading of any level (or end of
    document). List-valued fields (``related_PI``, ``related_ARG``,
    ``risks``) are split on commas; every other field stays a string.
    """
    blocks: list[dict[str, str | list[str]]] = []
    heading_matches = list(_QUOTE_AUDIT_HEADING.finditer(content))
    for index, heading_match in enumerate(heading_matches):
        region_start = heading_match.end()
        next_heading = _ANY_HEADING.search(content, region_start)
        region_end = next_heading.start() if next_heading else len(content)
        region = content[region_start:region_end]
        fields: dict[str, str | list[str]] = {}
        for key, raw_value in _FLAT_FIELD.findall(region):
            value = raw_value.strip()
            if key in LIST_FIELDS:
                fields[key] = [item for item in _LIST_SEP.split(value) if item] if value else []
            else:
                fields[key] = value
        blocks.append(fields)
    return blocks


def resolve_bibliography_keys(bibliography_path: Path) -> set[str]:
    """Return the set of BibTeX entry keys declared in ``bibliography_path``."""
    if not bibliography_path.is_file():
        return set()
    content = bibliography_path.read_text(encoding="utf-8")
    return set(_BIBTEX_KEY.findall(content))

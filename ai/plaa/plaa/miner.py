"""Module 1 — Argument Miner (deterministic part).

Extracts already-delimited sections from an ``ARG-*.md`` file (following
``templates/ficha-argumento.md``) into typed nodes. This module never
infers content that is not already separated by a Markdown heading or a
list item: segmenting free-form prose within a single section (e.g.
telling an OBJECTION apart from its REBUTTAL inside one paragraph) is a
judgment task and belongs to ``prompts/01-argument-miner.md``, not here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path


class NodeType(str, Enum):
    """Canonical node types requested by the PLAA specification."""

    CLAIM = "CLAIM"
    PREMISE = "PREMISE"
    CONCLUSION = "CONCLUSION"
    OBJECTION = "OBJECTION"
    REBUTTAL = "REBUTTAL"
    DEFINITION = "DEFINITION"
    ASSUMPTION = "ASSUMPTION"
    COUNTEREXAMPLE = "COUNTEREXAMPLE"
    QUESTION = "QUESTION"
    DISTINCTION = "DISTINCTION"


# Spanish section headings used by templates/ficha-argumento.md, mapped to
# the canonical node type they mechanically correspond to. Sections not
# listed here are still returned in ``ArgumentDocument.sections`` (raw
# text) but are not force-classified into one of the ten node types,
# because doing so would require interpretation this module deliberately
# does not perform.
SECTION_HEADINGS: dict[str, NodeType] = {
    "Afirmación (claim)": NodeType.CLAIM,
    "Premisas": NodeType.PREMISE,
    "Objeciones y respuestas": NodeType.OBJECTION,
    "Interpretaciones alternativas": NodeType.DISTINCTION,
}

_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_FLAT_FIELD = re.compile(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)$", re.MULTILINE)
_HEADING = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
_NUMBERED_ITEM = re.compile(r"^\s*(?:\d+\.|[-*])\s+(.+)$", re.MULTILINE)


@dataclass(frozen=True)
class Node:
    """A single mined unit of argumentative content."""

    type: NodeType
    text: str
    section: str


@dataclass
class ArgumentDocument:
    """Parsed representation of one ``ARG-*.md`` file."""

    path: str
    frontmatter: dict[str, str]
    sections: dict[str, str] = field(default_factory=dict)
    nodes: list[Node] = field(default_factory=list)

    @property
    def argument_id(self) -> str | None:
        return self.frontmatter.get("argument_id")

    @property
    def status(self) -> str | None:
        return self.frontmatter.get("status")


def parse_frontmatter(content: str) -> dict[str, str]:
    """Parse the flat YAML frontmatter block used by ARG-* files.

    Deliberately supports only flat ``key: value`` pairs, matching the
    actual shape of ``templates/ficha-argumento.md``. Does not depend on
    PyYAML (see ARCHITECTURE.md, "Sin dependencias nuevas").
    """
    match = _FRONTMATTER.match(content)
    if not match:
        return {}
    return {key: value.strip() for key, value in _FLAT_FIELD.findall(match.group(1))}


def parse_sections(content: str) -> dict[str, str]:
    """Split the body (after frontmatter) into ``## heading`` -> text."""
    body = content[_FRONTMATTER.match(content).end():] if _FRONTMATTER.match(content) else content
    headings = list(_HEADING.finditer(body))
    sections: dict[str, str] = {}
    for index, match in enumerate(headings):
        start = match.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        sections[match.group(1)] = body[start:end].strip()
    return sections


def mine_sections(sections: dict[str, str]) -> list[Node]:
    """Turn known sections into typed nodes without adding interpretation."""
    nodes: list[Node] = []
    for heading, node_type in SECTION_HEADINGS.items():
        text = sections.get(heading, "").strip()
        if not text:
            continue
        if node_type is NodeType.PREMISE:
            items = _NUMBERED_ITEM.findall(text)
            if items:
                nodes.extend(Node(type=NodeType.PREMISE, text=item.strip(), section=heading) for item in items)
                continue
        nodes.append(Node(type=node_type, text=text, section=heading))
    return nodes


def mine_argument_text(content: str, path: str = "<string>") -> ArgumentDocument:
    """Mine an in-memory ARG-*.md document."""
    frontmatter = parse_frontmatter(content)
    sections = parse_sections(content)
    return ArgumentDocument(path=path, frontmatter=frontmatter, sections=sections, nodes=mine_sections(sections))


def mine_argument_file(path: str | Path) -> ArgumentDocument:
    """Mine an ARG-*.md file from disk."""
    file_path = Path(path)
    return mine_argument_text(file_path.read_text(encoding="utf-8"), path=str(file_path))

"""Module 2 — Argument Graph (deterministic part).

Builds a graph strictly from relations that are already declared: ARG-*
frontmatter, the mined nodes of each argument (module 1), and the
relation table in ``research/argument-map.md``. This module never infers
a relation that is not already written down somewhere in the repository;
proposing a new relation is a judgment task for
``prompts/02-argument-graph.md``, not for this code.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .miner import ArgumentDocument

ALLOWED_RELATIONS = frozenset(
    {"supports", "depends-on", "objects-to", "revises", "contradicts", "distinguishes", "applies-to"}
)

_TABLE_ROW = re.compile(
    r"^\|\s*(?P<source>[^|]+?)\s*\|\s*(?P<relation>[^|]+?)\s*\|\s*(?P<target>[^|]+?)\s*\|\s*(?P<note>[^|]*?)\s*\|\s*$",
    re.MULTILINE,
)
_ARG_ID = re.compile(r"^ARG-\d{3,}$")


@dataclass(frozen=True)
class GraphNode:
    """A node in the argument graph: an argument or one of its mined parts."""

    id: str
    kind: str  # "argument" | one of miner.NodeType values, lowercased
    label: str


@dataclass(frozen=True)
class GraphEdge:
    """A directed, typed edge between two graph nodes."""

    source: str
    relation: str
    target: str
    note: str = ""


@dataclass
class ArgumentGraph:
    """The full graph: argument nodes, their mined sub-nodes, and declared relations."""

    nodes: list[GraphNode] = field(default_factory=list)
    edges: list[GraphEdge] = field(default_factory=list)

    def node_ids(self) -> set[str]:
        return {node.id for node in self.nodes}


def parse_argument_map_relations(content: str) -> list[GraphEdge]:
    """Parse the relation table of research/argument-map.md.

    Skips the header row, the separator row, and placeholder rows (the
    literal "—" used when no arguments are registered yet, and the
    explicitly-fictional example rows below the "Ejemplo" heading are
    parsed too — callers should slice ``content`` to the real table if
    they want to exclude the fictional example).
    """
    edges: list[GraphEdge] = []
    for match in _TABLE_ROW.finditer(content):
        source, relation, target, note = (
            match.group("source"),
            match.group("relation"),
            match.group("target"),
            match.group("note"),
        )
        if source in {"Origen", "—", ""} or relation in {"Relación", "---", ""}:
            continue
        relation_normalized = relation.strip("`")
        if relation_normalized not in ALLOWED_RELATIONS:
            continue
        edges.append(
            GraphEdge(
                source=source.strip("`"),
                relation=relation_normalized,
                target=target.strip("`"),
                note=note,
            )
        )
    return edges


def _argument_nodes(documents: list[ArgumentDocument]) -> list[GraphNode]:
    nodes: list[GraphNode] = []
    for document in documents:
        if not document.argument_id:
            continue
        nodes.append(GraphNode(id=document.argument_id, kind="argument", label=document.status or "UNKNOWN"))
        for index, mined_node in enumerate(document.nodes):
            nodes.append(
                GraphNode(
                    id=f"{document.argument_id}:{mined_node.type.value}:{index}",
                    kind=mined_node.type.value.lower(),
                    label=mined_node.text[:80],
                )
            )
    return nodes


def _containment_edges(documents: list[ArgumentDocument]) -> list[GraphEdge]:
    edges: list[GraphEdge] = []
    for document in documents:
        if not document.argument_id:
            continue
        for index, mined_node in enumerate(document.nodes):
            edges.append(
                GraphEdge(
                    source=document.argument_id,
                    relation="contains",
                    target=f"{document.argument_id}:{mined_node.type.value}:{index}",
                )
            )
    return edges


def build_graph(documents: list[ArgumentDocument], argument_map_content: str) -> ArgumentGraph:
    """Build the graph. Relations whose endpoints are not known ARG-* ids are dropped."""
    nodes = _argument_nodes(documents)
    node_ids = {node.id for node in nodes}
    edges = _containment_edges(documents)
    for edge in parse_argument_map_relations(argument_map_content):
        if edge.source in node_ids and edge.target in node_ids:
            edges.append(edge)
    return ArgumentGraph(nodes=nodes, edges=edges)


def to_dot(graph: ArgumentGraph) -> str:
    """Optional Graphviz DOT export, for visual inspection once the corpus grows."""
    lines = ["digraph plaa_argument_graph {"]
    for node in graph.nodes:
        safe_label = node.label.replace('"', "'")
        lines.append(f'  "{node.id}" [label="{safe_label}" shape=box];')
    for edge in graph.edges:
        lines.append(f'  "{edge.source}" -> "{edge.target}" [label="{edge.relation}"];')
    lines.append("}")
    return "\n".join(lines)

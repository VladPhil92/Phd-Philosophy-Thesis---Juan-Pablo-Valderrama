"""Tests for plaa.graph — uses only fictional data, never real ARG-* content."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from plaa.graph import build_graph, parse_argument_map_relations  # noqa: E402
from plaa.miner import mine_argument_text  # noqa: E402

FICTIONAL_ARG_A = (
    "---\nargument_id: ARG-A\nstatus: DEVELOPING\nhuman_validation: pending\n---\n\n"
    "## Afirmación (claim)\nAfirmación ficticia A.\n"
)
FICTIONAL_ARG_B = (
    "---\nargument_id: ARG-B\nstatus: IDEA\nhuman_validation: pending\n---\n\n"
    "## Afirmación (claim)\nAfirmación ficticia B.\n"
)


class ParseArgumentMapRelationsTests(unittest.TestCase):
    def test_parses_a_valid_relation_row(self) -> None:
        content = "| Origen | Relación | Destino | Nota |\n|---|---|---|---|\n| ARG-A | supports | ARG-B | nota |\n"
        edges = parse_argument_map_relations(content)
        self.assertEqual(len(edges), 1)
        self.assertEqual((edges[0].source, edges[0].relation, edges[0].target), ("ARG-A", "supports", "ARG-B"))

    def test_skips_header_and_placeholder_rows(self) -> None:
        content = "| Origen | Relación | Destino | Nota |\n|---|---|---|---|\n| — | — | — | Sin argumentos. |\n"
        self.assertEqual(parse_argument_map_relations(content), [])

    def test_rejects_relation_outside_allowed_vocabulary(self) -> None:
        content = "| ARG-A | invents | ARG-B | nota |\n"
        self.assertEqual(parse_argument_map_relations(content), [])


class BuildGraphTests(unittest.TestCase):
    def test_drops_relations_with_unknown_endpoints(self) -> None:
        documents = [mine_argument_text(FICTIONAL_ARG_A)]
        argument_map = "| ARG-A | supports | ARG-UNKNOWN | nota |\n"
        graph = build_graph(documents, argument_map)
        self.assertNotIn("ARG-UNKNOWN", graph.node_ids())
        self.assertFalse(any(edge.target == "ARG-UNKNOWN" for edge in graph.edges))

    def test_keeps_relations_between_known_arguments(self) -> None:
        documents = [mine_argument_text(FICTIONAL_ARG_A), mine_argument_text(FICTIONAL_ARG_B)]
        argument_map = "| ARG-A | supports | ARG-B | nota ficticia |\n"
        graph = build_graph(documents, argument_map)
        supports_edges = [edge for edge in graph.edges if edge.relation == "supports"]
        self.assertEqual(len(supports_edges), 1)
        self.assertEqual((supports_edges[0].source, supports_edges[0].target), ("ARG-A", "ARG-B"))

    def test_argument_nodes_are_present_for_every_document(self) -> None:
        documents = [mine_argument_text(FICTIONAL_ARG_A), mine_argument_text(FICTIONAL_ARG_B)]
        graph = build_graph(documents, "")
        self.assertEqual(graph.node_ids() & {"ARG-A", "ARG-B"}, {"ARG-A", "ARG-B"})


if __name__ == "__main__":
    unittest.main()

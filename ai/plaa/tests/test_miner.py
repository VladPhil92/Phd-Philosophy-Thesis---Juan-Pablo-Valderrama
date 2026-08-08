"""Tests for plaa.miner — uses only the fictional fixture ARG-EXAMPLE-000.md."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from plaa.miner import NodeType, mine_argument_file, parse_frontmatter, parse_sections  # noqa: E402

FIXTURE = Path(__file__).parent / "fixtures" / "ARG-EXAMPLE-000.md"


class ParseFrontmatterTests(unittest.TestCase):
    def test_extracts_flat_fields(self) -> None:
        content = "---\nargument_id: ARG-001\nstatus: IDEA\nhuman_validation: pending\n---\n\nbody"
        frontmatter = parse_frontmatter(content)
        self.assertEqual(frontmatter["argument_id"], "ARG-001")
        self.assertEqual(frontmatter["status"], "IDEA")
        self.assertEqual(frontmatter["human_validation"], "pending")

    def test_missing_frontmatter_returns_empty_dict(self) -> None:
        self.assertEqual(parse_frontmatter("# no frontmatter here"), {})


class ParseSectionsTests(unittest.TestCase):
    def test_splits_on_level_two_headings(self) -> None:
        content = "---\nargument_id: ARG-001\n---\n\n## Uno\ntexto uno\n\n## Dos\ntexto dos\n"
        sections = parse_sections(content)
        self.assertEqual(sections["Uno"], "texto uno")
        self.assertEqual(sections["Dos"], "texto dos")


class MineArgumentFileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.document = mine_argument_file(FIXTURE)

    def test_reads_frontmatter(self) -> None:
        self.assertEqual(self.document.argument_id, "ARG-900001")
        self.assertEqual(self.document.status, "DEVELOPING")

    def test_extracts_claim_node(self) -> None:
        claims = [node for node in self.document.nodes if node.type is NodeType.CLAIM]
        self.assertEqual(len(claims), 1)
        self.assertIn("hospitalidad ficticia F", claims[0].text)

    def test_extracts_two_numbered_premises(self) -> None:
        premises = [node for node in self.document.nodes if node.type is NodeType.PREMISE]
        self.assertEqual(len(premises), 2)
        self.assertTrue(all(premise.section == "Premisas" for premise in premises))

    def test_extracts_objection_section_as_single_node(self) -> None:
        objections = [node for node in self.document.nodes if node.type is NodeType.OBJECTION]
        self.assertEqual(len(objections), 1)
        self.assertIn("Objeción ficticia", objections[0].text)

    def test_unlisted_sections_are_preserved_but_not_forced_into_a_node_type(self) -> None:
        self.assertIn("Alcance y límites", self.document.sections)
        node_sections = {node.section for node in self.document.nodes}
        self.assertNotIn("Alcance y límites", node_sections)

    def test_does_not_invent_content_for_empty_sections(self) -> None:
        empty_content = "---\nargument_id: ARG-002\nstatus: IDEA\nhuman_validation: pending\n---\n\n## Afirmación (claim)\n\n## Premisas\n"
        from plaa.miner import mine_argument_text

        document = mine_argument_text(empty_content)
        self.assertEqual(document.nodes, [])


if __name__ == "__main__":
    unittest.main()

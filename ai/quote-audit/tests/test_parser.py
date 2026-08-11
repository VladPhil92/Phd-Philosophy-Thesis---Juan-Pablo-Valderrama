"""Tests for quote_audit.parser — deterministic extraction only."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from quote_audit import parser  # noqa: E402

FIXTURE = Path(__file__).parent / "fixtures" / "sample-ficha-fragment.md"


class ParseQuoteAuditBlocksTests(unittest.TestCase):
    def test_extracts_exactly_one_block_from_fixture(self) -> None:
        content = FIXTURE.read_text(encoding="utf-8")
        blocks = parser.parse_quote_audit_blocks(content)
        self.assertEqual(len(blocks), 1)

    def test_block_stops_before_next_heading(self) -> None:
        content = FIXTURE.read_text(encoding="utf-8")
        block = parser.parse_quote_audit_blocks(content)[0]
        # The fixture's trailing "## Paráfrasis e interpretación" section
        # has no key: value lines of its own, so if the block leaked past
        # its heading boundary it would still add no *extra* fields here —
        # the real regression this guards is a block that swallows the
        # next "Auditoría de citas" heading's fields in a multi-quote
        # ficha. 20 is the exact field count declared in the fixture.
        self.assertEqual(len(block), 20)

    def test_flat_fields_are_parsed(self) -> None:
        content = FIXTURE.read_text(encoding="utf-8")
        block = parser.parse_quote_audit_blocks(content)[0]
        self.assertEqual(block["quote_id"], "derrida-2023-hospitality#c56")
        self.assertEqual(block["source"], "derrida-2023-hospitality")
        self.assertEqual(block["recommended_status"], "RELEVANCE_AUDITED")

    def test_list_fields_are_split_on_commas(self) -> None:
        content = FIXTURE.read_text(encoding="utf-8")
        block = parser.parse_quote_audit_blocks(content)[0]
        self.assertEqual(block["related_PI"], ["PI-07"])
        self.assertEqual(block["related_ARG"], ["ARG-001"])

    def test_no_blocks_in_content_without_audit_heading(self) -> None:
        blocks = parser.parse_quote_audit_blocks("## Citas verificadas\n\n1. Texto sin auditar.\n")
        self.assertEqual(blocks, [])


class ResolveBibliographyKeysTests(unittest.TestCase):
    def test_resolves_real_bibliography_keys(self) -> None:
        real_bib = Path(__file__).resolve().parents[3] / "research" / "sources" / "bibliography.bib"
        keys = parser.resolve_bibliography_keys(real_bib)
        self.assertIn("derrida-2023-hospitality", keys)
        self.assertIn("derrida-2008-animal", keys)
        self.assertIn("derrida-2010-bestia-soberano-1", keys)

    def test_missing_file_returns_empty_set(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            keys = parser.resolve_bibliography_keys(Path(tmp) / "no-existe.bib")
        self.assertEqual(keys, set())


if __name__ == "__main__":
    unittest.main()

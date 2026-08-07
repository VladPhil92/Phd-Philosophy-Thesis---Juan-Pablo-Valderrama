# Doctoral Research Library

This directory is the canonical public research layer for source identities, provenance, verification records, notes, indexes, and copyright-permitted transcriptions. No `/corpus` directory existed when this system was created; consequently `/library` is canonical rather than a duplicate or wrapper. If a corpus is later introduced, it must point here or be a private/local store keyed by `source_id`, not a second public copy.

> **A Markdown transcription is a computational research representation of the source. It is not the authoritative source itself.**

The verified edition remains the citation authority. Start with [methodology](LIBRARY-METHODOLOGY.md), [OCR protocol](OCR-PROTOCOL.md), [verification gate](SOURCE-VERIFICATION-PROTOCOL.md), [copyright policy](COPYRIGHT-POLICY.md), and [AI rules](AI-LIBRARY-ACCESS-RULES.md). The [source register](library-index.md) contains records supported by the proposal; editions remain `TODO — VERIFY`.

## Architecture

- `primary/`: proposal-defined primary works; records contain no book text.
- `secondary/` and `jurisprudence/`: acquisition/indexing areas.
- `indexes/`: cross-source navigation and controlled statuses.
- `templates/`: reusable source scaffold outside this directory.
- `tools/library/`: future local automation, never an authority.

## Dissertation map

- **Part I:** Genealogy of the human exception.
- **Part II:** Collapse of the criteria: animal and machine.
- **Part III:** Construction of Sovereignty of Hospitality.

Use chapter IDs such as `CHAPTER-05`; connect claims through the provenance chain documented in the methodology.

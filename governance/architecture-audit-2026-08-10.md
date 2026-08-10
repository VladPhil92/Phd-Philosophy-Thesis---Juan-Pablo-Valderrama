# Architecture audit — 2026-08-10

**Decision:** infrastructure freeze after canonical-registry migration.

The former `research/sources/corpus-map.md` has been superseded by
`research/sources/library-manifest.md`; all candidate records were migrated,
with the known `SRC-037`/`SRC-185` duplicate consolidated under `SRC-037`.
The concept registry and quote ledger are indexes, not parallel stores.

During the freeze, do not create another manifest, concept registry, quote
ledger, background system, or competing source architecture. Substantive
research decisions, questions, hypotheses, and PLAA remain unchanged.

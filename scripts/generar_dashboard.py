#!/usr/bin/env python3
"""Genera research/dashboard.md: estado mecánico de la investigación.

Cada número es un conteo determinista sobre archivos existentes (fuentes,
citas, argumentos, objeciones, decisiones humanas pendientes) — nunca una
estimación ni un juicio sobre calidad o avance real. No reemplaza la
lectura de las fichas ni del `MASTER_EXECUTION_PLAN.md`; solo evita tener
que grepear a mano para saber "cuántos hay".

Reutiliza los patrones y `ROOT` ya definidos en auditar_repositorio.py en
vez de duplicarlos.
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import auditar_repositorio as base  # noqa: E402

ROOT = base.ROOT
LIBRARY_MANIFEST = ROOT / "research" / "sources" / "library-manifest.md"
NOTES_DIR = ROOT / "research" / "sources" / "notes"
LEDGER_DIR = ROOT / "research" / "argument-ledger"
CHAPTERS_DIR = ROOT / "thesis" / "chapters"
METHODOLOGY = ROOT / "research" / "methodology.md"
OUTPUT = ROOT / "research" / "dashboard.md"

CITATION_ITEM_NUMBERED = re.compile(r"^\d+\.\s", re.MULTILINE)
CITATION_ITEM_BULLET = re.compile(r"^-\s", re.MULTILINE)
TOP_LEVEL_BULLET = re.compile(r"^-\s", re.MULTILINE)
PENDING_DECISION = re.compile(r"DECISIÓN HUMANA REQUERIDA")


def extract_section(content: str, heading: str) -> str:
    """Return the body text under a "## <heading>" line, up to the next
    "## " heading or end of file. Mirrors the heading-bounded scanning
    already used in ai/quote-audit/quote_audit/parser.py."""
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\b.*?\n(.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(content)
    return match.group(1) if match else ""


def count_corpus_states() -> tuple[int, int, int]:
    """Return (total candidatas, CITED, IDENTITY_VERIFIED) from library-manifest.md.

    Counts by substring match on the row text, not a fixed column index,
    because section G's table has a different column layout than A-F.
    """
    if not LIBRARY_MANIFEST.is_file():
        return (0, 0, 0)
    content = LIBRARY_MANIFEST.read_text(encoding="utf-8")
    total = len(set(base.SRC_ID_TABLE_CELL.findall(content)))
    cited = identity_verified = 0
    for line in content.splitlines():
        if not base.SRC_ID_TABLE_CELL.match(line):
            continue
        if re.search(r"\bCITED\b", line):
            cited += 1
        elif re.search(r"\bIDENTITY_VERIFIED\b", line):
            identity_verified += 1
    return (total, cited, identity_verified)


def count_verified_citations() -> tuple[int, list[tuple[str, int]]]:
    """Return (total, [(clave_bibtex, conteo), ...]) across ficha-fuente
    files whose stem matches a real bibliography.bib key — excludes
    README.md and second-order documents like sintesis-*.md."""
    known_keys = base.bibliography_keys()
    per_source: list[tuple[str, int]] = []
    if NOTES_DIR.is_dir():
        for path in sorted(NOTES_DIR.glob("*.md")):
            if path.stem not in known_keys:
                continue
            section = extract_section(path.read_text(encoding="utf-8"), "Citas verificadas")
            # Fichas use either continuous numbering ("1. ... 2. ...") or a
            # flat bullet list ("- ... - ..."), never both for citations in
            # the same ficha — take whichever pattern actually matches more.
            count = max(len(CITATION_ITEM_NUMBERED.findall(section)), len(CITATION_ITEM_BULLET.findall(section)))
            per_source.append((path.stem, count))
    return (sum(count for _, count in per_source), per_source)


def count_arguments() -> dict[str, object]:
    """Tally research/argument-ledger/*.md by status and human_validation."""
    by_status: dict[str, int] = {}
    pending_validation = 0
    total_objections = 0
    if LEDGER_DIR.is_dir():
        for path in sorted(LEDGER_DIR.glob("*.md")):
            if path.name == "README.md":
                continue
            content = path.read_text(encoding="utf-8")
            frontmatter_match = base.ARG_FRONTMATTER.match(content)
            frontmatter = frontmatter_match.group(1) if frontmatter_match else ""
            status_match = base.ARG_STATUS_FIELD.search(frontmatter)
            status = status_match.group(1) if status_match else "SIN_ESTADO"
            by_status[status] = by_status.get(status, 0) + 1
            validation_match = base.ARG_VALIDATION_FIELD.search(frontmatter)
            if (validation_match.group(1) if validation_match else None) != "validated":
                pending_validation += 1
            objections_section = extract_section(content, "Objeciones y respuestas")
            total_objections += len(TOP_LEVEL_BULLET.findall(objections_section))
    return {
        "total": sum(by_status.values()),
        "by_status": by_status,
        "pending_validation": pending_validation,
        "objections": total_objections,
    }


def count_manuscript_sections() -> int:
    if not CHAPTERS_DIR.is_dir():
        return 0
    return sum(1 for path in CHAPTERS_DIR.rglob("*.md") if path.name != "README.md")


def count_pending_methodology_decisions() -> int:
    if not METHODOLOGY.is_file():
        return 0
    return len(PENDING_DECISION.findall(METHODOLOGY.read_text(encoding="utf-8")))


def render(
    corpus_states: tuple[int, int, int],
    citations: tuple[int, list[tuple[str, int]]],
    arguments: dict[str, object],
    manuscript_sections: int,
    pending_methodology: int,
) -> str:
    total_candidates, cited, identity_verified = corpus_states
    total_citations, per_source = citations
    lines = [
        "# Dashboard de investigación",
        "",
        f"**Generado automáticamente:** {date.today().isoformat()} "
        "— por `python3 scripts/generar_dashboard.py`. No editar a mano: los "
        "cambios se pierden en la próxima ejecución. Cada número es un conteo "
        "mecánico, no una evaluación de calidad ni de avance real — para eso, "
        "lea `MASTER_EXECUTION_PLAN.md` y las fichas mismas.",
        "",
        "## Fuentes",
        "",
        f"- Candidatas registradas en `library-manifest.md`: **{total_candidates}**",
        f"- Con edición verificada, leídas y citadas (`CITED`): **{cited}**",
        f"- Con identidad confirmada por búsqueda, sin leer (`IDENTITY_VERIFIED`): **{identity_verified}** "
        "— este conteo busca la palabra literal por fila; la sección G "
        "(SRC-151–200) la declara una sola vez en su preámbulo, no por fila, "
        "así que este número la subestima. Ver `library-manifest.md` directamente.",
        "- Lectura parcial (`READING`): no se distingue todavía como estado "
        "propio en `library-manifest.md` — ver `research/methodology.md` §4.",
        "",
        "## Citas verificadas",
        "",
        f"- Total: **{total_citations}**",
        "",
    ]
    for clave, count in per_source:
        lines.append(f"  - `{clave}`: {count}")
    lines += [
        "",
        "## Argumentos (`research/argument-ledger/`)",
        "",
        f"- Total: **{arguments['total']}**",
    ]
    for status, count in sorted(arguments["by_status"].items()):
        lines.append(f"  - `{status}`: {count}")
    lines += [
        f"- Pendientes de `human_validation: validated`: **{arguments['pending_validation']}**",
        f"- Objeciones registradas (todas las fichas): **{arguments['objections']}**",
        "",
        "## Manuscrito",
        "",
        f"- Secciones en `thesis/chapters/`: **{manuscript_sections}**",
        "",
        "## Decisiones humanas pendientes",
        "",
        f"- Marcadas `DECISIÓN HUMANA REQUERIDA` en `research/methodology.md`: "
        f"**{pending_methodology}**",
        f"- Argumentos sin `human_validation: validated`: **{arguments['pending_validation']}**",
        "",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    content = render(
        count_corpus_states(),
        count_verified_citations(),
        count_arguments(),
        count_manuscript_sections(),
        count_pending_methodology_decisions(),
    )
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Dashboard generado: {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

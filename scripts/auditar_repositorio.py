#!/usr/bin/env python3
"""Comprueba invariantes estructurales del repositorio doctoral."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = (
    "README.md",
    "CONTRIBUTING.md",
    "PROJECT.md",
    "METHODOLOGY.md",
    "RESEARCH-WORKFLOW.md",
    "AI-RESEARCH-PROTOCOL.md",
    "CITATION.cff",
    "LICENSE",
    "governance/architecture.md",
    "governance/initial-audit.md",
    "governance/decision-log.md",
    "ai/policy.md",
    "research/questions.md",
    "research/methodology.md",
    "research/sources/bibliography.bib",
    "research/sources/notes/README.md",
    "research/analysis/README.md",
    "research/argument-ledger/README.md",
    "library/README.md",
    "library/LIBRARY-METHODOLOGY.md",
    "library/OCR-PROTOCOL.md",
    "library/TRANSCRIPTION-PROTOCOL.md",
    "library/SOURCE-VERIFICATION-PROTOCOL.md",
    "library/COPYRIGHT-POLICY.md",
    "library/AI-LIBRARY-ACCESS-RULES.md",
    "library/library-index.md",
    "library/indexes/README.md",
    "library/templates/source-metadata-template.md",
    "library/templates/reading-note-template.md",
    "library/templates/quotation-record-template.md",
    "library/templates/source-record-scaffold.md",
    "thesis/outline.md",
    "thesis/chapters/README.md",
    "thesis/review/checklist.md",
    "templates/ficha-fuente.md",
    "templates/ficha-argumento.md",
    "templates/registro-ia.md",
)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
SOURCE_ID = re.compile(r"^LIB-[A-Z]+-\d{3}$")
OBSOLETE_ROOTS = ("00-gobernanza", "01-investigacion", "04-escritura", "plantillas")
FORBIDDEN_SUFFIXES = {".pdf", ".epub", ".djvu", ".djv", ".mobi"}


def markdown_files() -> list[Path]:
    """Return tracked-style Markdown documents, excluding Git internals."""
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def validate_required_paths() -> list[str]:
    return [f"Falta la ruta requerida: {path}" for path in REQUIRED_PATHS if not (ROOT / path).is_file()]


def validate_links() -> list[str]:
    errors: list[str] = []
    for document in markdown_files():
        content = document.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(content):
            clean_target = target.split("#", 1)[0].strip()
            if not clean_target or re.match(r"^[a-z][a-z0-9+.-]*:", clean_target):
                continue
            resolved = (document.parent / clean_target).resolve()
            if not resolved.exists() or ROOT not in (resolved, *resolved.parents):
                location = document.relative_to(ROOT)
                errors.append(f"Enlace local inválido en {location}: {target}")
    return errors


def validate_readmes() -> list[str]:
    errors: list[str] = []
    governed_directories = [
        path for path in ROOT.iterdir() if path.is_dir() and not path.name.startswith(".")
    ]
    for directory in governed_directories:
        if not (directory / "README.md").is_file() and directory.name not in {"scripts"}:
            errors.append(f"El directorio {directory.name} no define su alcance en README.md")
    return errors


def validate_consolidation() -> list[str]:
    errors = [f"Permanece una arquitectura obsoleta: {name}/" for name in OBSOLETE_ROOTS if (ROOT / name).exists()]
    records = sorted((ROOT / "library/records").glob("LIB-*/README.md"))
    ids = [record.parent.name for record in records]
    if len(ids) != 28:
        errors.append(f"Se esperaban 28 registros de fuente y se encontraron {len(ids)}")
    if len(ids) != len(set(ids)):
        errors.append("Hay IDs de fuente duplicados")
    errors.extend(f"ID de fuente inválido: {source_id}" for source_id in ids if not SOURCE_ID.fullmatch(source_id))
    index = (ROOT / "library/library-index.md").read_text(encoding="utf-8")
    errors.extend(f"El índice no contiene {source_id}" for source_id in ids if f"`{source_id}`" not in index)
    for chapter in range(1, 10):
        path = ROOT / f"thesis/chapters/{chapter:02d}/README.md"
        if not path.is_file():
            errors.append(f"Falta la ubicación del capítulo {chapter:02d}")
    return errors


def validate_safety() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"Binario documental presente: {path.relative_to(ROOT)}")
        if path.suffix.lower() in {".md", ".yml", ".yaml", ".py", ".bib", ".cff"}:
            text = path.read_text(encoding="utf-8")
            if "<" * 7 in text or ">" * 7 in text:
                errors.append(f"Marcador de conflicto presente: {path.relative_to(ROOT)}")
    return errors


def main() -> int:
    errors = (
        validate_required_paths()
        + validate_readmes()
        + validate_links()
        + validate_consolidation()
        + validate_safety()
    )
    if errors:
        print("Auditoría fallida:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Auditoría correcta: {len(markdown_files())} documentos Markdown comprobados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Comprueba invariantes estructurales del repositorio doctoral."""

from __future__ import annotations

import re
import subprocess
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
    "governance/architecture-audit-2026-08-10.md",
    "ai/policy.md",
    "research/questions.md",
    "research/methodology.md",
    "research/concept-registry.md",
    "research/background/README.md",
    "research/background/research-lineage.md",
    "research/background/masters-thesis/README.md",
    "research/background/masters-thesis/metadata.md",
    "research/background/masters-thesis/analytical-summary.md",
    "research/background/masters-thesis/concept-evolution.md",
    "research/background/masters-thesis/argument-evolution.md",
    "research/background/masters-thesis/critical-audit.md",
    "research/background/masters-thesis/continuity-with-phd.md",
    "research/background/masters-thesis/originals/README.md",
    "research/sources/bibliography.bib",
    "research/sources/library-manifest.md",
    "research/sources/quote-ledger.md",
    "research/sources/notes/README.md",
    "research/analysis/README.md",
    "research/argument-ledger/README.md",
    "thesis/outline.md",
    "thesis/chapters/README.md",
    "thesis/review/checklist.md",
    "templates/ficha-fuente.md",
    "templates/ficha-argumento.md",
    "templates/registro-ia.md",
)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
JUNK_NAMES = {
    ".DS_Store",
    "Desktop.ini",
    "Thumbs.db",
    ".eslintcache",
    ".stylelintcache",
}
JUNK_PARTS = {
    "__pycache__",
    ".cache",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "node_modules",
}
JUNK_SUFFIXES = (".bak", ".orig", ".pyc", ".rej", ".swp", ".swo", ".temp", ".tmp")
MERGE_MARKER_PATTERN = re.compile(r"^(?:<{7}|={7}|>{7})(?!\S)", re.MULTILINE)
PI_HEADING = re.compile(r"^#{2,6}\s+(PI-\d+)\b", re.MULTILINE)
ARG_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
ARG_ID_FIELD = re.compile(r"^argument_id:\s*(\S+)\s*$", re.MULTILINE)
ARG_ID_PATTERN = re.compile(r"^ARG-\d{3,}$")
SRC_ID_TABLE_CELL = re.compile(r"^\|\s*(SRC-(?:\d{3,}|PR-\d{3,}))\s*\|", re.MULTILINE)
ARG_STATUS_FIELD = re.compile(r"^status:\s*(\S+)\s*$", re.MULTILINE)
ARG_VALIDATION_FIELD = re.compile(r"^human_validation:\s*(\S+)\s*$", re.MULTILINE)
BIBTEX_KEY = re.compile(r"^@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
VALID_ARGUMENT_STATUSES = {
    "IDEA",
    "DEVELOPING",
    "SUPPORTED",
    "CONTESTED",
    "READY_FOR_HUMAN_REVIEW",
    "VALIDATED",
    "REJECTED",
}
OBSOLETE_ARCHITECTURE_ROOTS = {
    "00-gobernanza",
    "01-investigacion",
    "02-fuentes",
    "03-analisis",
    "04-escritura",
    "05-revision",
    "plantillas",
    "proposal",
    "cases",
    "outputs",
    "bibliography",
}


def markdown_files() -> list[Path]:
    """Return tracked-style Markdown documents, excluding Git internals."""
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def tracked_files() -> list[Path]:
    """Return paths known to Git, which are the files CI can reliably audit."""
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item]


def validate_tracked_files() -> list[str]:
    """Reject editor, operating-system, cache and merge leftovers in Git."""
    errors: list[str] = []
    for path in tracked_files():
        if (
            path.name in JUNK_NAMES
            or any(part in JUNK_PARTS for part in path.parts)
            or path.name.startswith("~$")
            or path.name.endswith(JUNK_SUFFIXES)
        ):
            errors.append(f"Archivo residual versionado: {path.as_posix()}")
    return errors


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


def validate_merge_markers() -> list[str]:
    """Reject unresolved Git conflict markers left in tracked text files."""
    errors: list[str] = []
    for path in tracked_files():
        full_path = ROOT / path
        if not full_path.is_file():
            continue
        try:
            content = full_path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if MERGE_MARKER_PATTERN.search(content):
            errors.append(f"Marcador de fusión sin resolver en {path.as_posix()}")
    return errors


def validate_obsolete_architecture_roots() -> list[str]:
    """Flag top-level directories from superseded numbered/parallel architectures."""
    errors: list[str] = []
    for path in ROOT.iterdir():
        if path.is_dir() and path.name in OBSOLETE_ARCHITECTURE_ROOTS:
            errors.append(
                f"Raíz de arquitectura obsoleta presente: {path.name}/ "
                "(superada por governance/decision-log.md DEC-001/DEC-002/DEC-003)"
            )
    return errors


def validate_research_questions() -> list[str]:
    """Detect duplicate PI-* identifiers in research/questions.md."""
    errors: list[str] = []
    questions_file = ROOT / "research" / "questions.md"
    if not questions_file.is_file():
        return errors
    content = questions_file.read_text(encoding="utf-8")
    seen: dict[str, int] = {}
    for match in PI_HEADING.finditer(content):
        identifier = match.group(1)
        seen[identifier] = seen.get(identifier, 0) + 1
    for identifier, count in seen.items():
        if count > 1:
            errors.append(f"Identificador duplicado en research/questions.md: {identifier} ({count} veces)")
    return errors


def validate_library_manifest() -> list[str]:
    """Check unique IDs, exclusive categories, and canonical reading stages."""
    errors: list[str] = []
    manifest = ROOT / "research" / "sources" / "library-manifest.md"
    if not manifest.is_file():
        return errors
    content = manifest.read_text(encoding="utf-8")
    seen: dict[str, int] = {}
    for match in SRC_ID_TABLE_CELL.finditer(content):
        identifier = match.group(1)
        seen[identifier] = seen.get(identifier, 0) + 1
    for identifier, count in seen.items():
        if count > 1:
            errors.append(f"Identificador duplicado en library-manifest.md: {identifier} ({count} veces)")

    categories = {
        "PRIMARY_PHILOSOPHICAL_SOURCE", "SECONDARY_LITERATURE",
        "CONTEXTUAL_LITERATURE", "HISTORICAL_BACKGROUND",
        "PREVIOUS_RESEARCH_BY_AUTHOR", "METHODOLOGICAL_SOURCE",
        "REFERENCE_WORK", "UNCLASSIFIED",
    }
    stages = {
        "NOT_REGISTERED", "REGISTERED", "ACQUIRED", "READING",
        "NOTES_CREATED", "QUOTES_VERIFIED", "CONCEPTS_INDEXED",
        "ARGUMENTS_IDENTIFIED", "READY_FOR_DOCTORAL_USE",
    }
    for line in content.splitlines():
        if not re.match(r"^\|\s*SRC-(?:\d{3,}|PR-\d{3,})\s*\|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 18:
            errors.append(f"Fila incompleta en library-manifest.md: {cells[0]}")
            continue
        if cells[8] not in categories:
            errors.append(f"Categoría no canónica en {cells[0]}: {cells[8]}")
        if cells[10] not in stages:
            errors.append(f"Etapa de lectura no canónica en {cells[0]}: {cells[10]}")
    return errors


def validate_bibliography() -> list[str]:
    """Detect duplicate BibTeX keys, including the prior-work record."""
    bibliography = ROOT / "research" / "sources" / "bibliography.bib"
    if not bibliography.is_file():
        return []
    content = bibliography.read_text(encoding="utf-8")
    seen: dict[str, int] = {}
    for key in BIBTEX_KEY.findall(content):
        normalized_key = key.casefold()
        seen[normalized_key] = seen.get(normalized_key, 0) + 1
    return [
        f"Clave BibTeX duplicada: {key} ({count} veces)"
        for key, count in seen.items()
        if count > 1
    ]


def validate_research_background_separation() -> list[str]:
    """Keep the master's thesis in lineage records and out of the live corpus/ledger."""
    errors: list[str] = []
    prior_work_key = "valderrama-pino-2020-animal"
    bibliography = ROOT / "research" / "sources" / "bibliography.bib"
    if bibliography.is_file():
        content = bibliography.read_text(encoding="utf-8")
        if len(re.findall(rf"^@mastersthesis\s*\{{\s*{prior_work_key}\s*,", content, re.MULTILINE)) != 1:
            errors.append(
                "La tesis de maestría debe tener una única entrada @mastersthesis "
                f"con clave {prior_work_key}"
            )
        for classification in ("PREVIOUS_RESEARCH_BY_AUTHOR", "AUTHOR_BACKGROUND"):
            if classification not in content:
                errors.append(f"Falta la clasificación {classification} en la entrada de trabajo previo")

    manifest = ROOT / "research" / "sources" / "library-manifest.md"
    if manifest.is_file():
        content = manifest.read_text(encoding="utf-8")
        matching = [line for line in content.splitlines() if line.startswith("| SRC-PR-001 ")]
        if len(matching) != 1 or "PREVIOUS_RESEARCH_BY_AUTHOR" not in matching[0]:
            errors.append("La tesis de maestría debe figurar una vez como PREVIOUS_RESEARCH_BY_AUTHOR")

    ledger_dir = ROOT / "research" / "argument-ledger"
    if ledger_dir.is_dir():
        forbidden_markers = (prior_work_key, "HIST-2020-", "PREVIOUS_RESEARCH")
        for path in sorted(ledger_dir.glob("*.md")):
            if path.name == "README.md":
                continue
            content = path.read_text(encoding="utf-8")
            if any(marker in content for marker in forbidden_markers):
                errors.append(
                    "Trabajo previo copiado al argument ledger sin reexamen doctoral: "
                    f"{path.relative_to(ROOT).as_posix()}"
                )
    return errors


def validate_argument_ledger() -> list[str]:
    """Check ARG-* frontmatter: duplicate IDs, valid status, and human_validation safeguard."""
    errors: list[str] = []
    ledger_dir = ROOT / "research" / "argument-ledger"
    if not ledger_dir.is_dir():
        return errors
    seen_ids: dict[str, list[str]] = {}
    for path in sorted(ledger_dir.glob("*.md")):
        if path.name == "README.md":
            continue
        content = path.read_text(encoding="utf-8")
        location = path.relative_to(ROOT).as_posix()
        frontmatter_match = ARG_FRONTMATTER.match(content)
        if not frontmatter_match:
            errors.append(f"Ficha de argumento sin cabecera YAML válida: {location}")
            continue
        frontmatter = frontmatter_match.group(1)

        id_match = ARG_ID_FIELD.search(frontmatter)
        argument_id = id_match.group(1) if id_match else None
        if not argument_id:
            errors.append(f"Ficha de argumento sin argument_id: {location}")
        else:
            if not ARG_ID_PATTERN.match(argument_id):
                errors.append(
                    f"argument_id con formato inválido en {location}: {argument_id!r} "
                    f"(se esperaba el patrón ARG-### tal como {ARG_ID_PATTERN.pattern})"
                )
            seen_ids.setdefault(argument_id, []).append(location)

        status_match = ARG_STATUS_FIELD.search(frontmatter)
        status = status_match.group(1) if status_match else None
        if not status or status not in VALID_ARGUMENT_STATUSES:
            errors.append(
                f"Estado epistémico ausente o inválido en {location}: {status!r} "
                f"(valores admitidos: {', '.join(sorted(VALID_ARGUMENT_STATUSES))})"
            )

        validation_match = ARG_VALIDATION_FIELD.search(frontmatter)
        human_validation = validation_match.group(1) if validation_match else None
        if status == "VALIDATED" and human_validation != "validated":
            errors.append(
                f"Argumento marcado VALIDATED sin human_validation: validated explícito en {location}"
            )

    for argument_id, locations in seen_ids.items():
        if len(locations) > 1:
            errors.append(
                f"Identificador de argumento duplicado: {argument_id} en {', '.join(locations)}"
            )
    return errors


def main() -> int:
    errors = (
        validate_required_paths()
        + validate_readmes()
        + validate_links()
        + validate_tracked_files()
        + validate_merge_markers()
        + validate_obsolete_architecture_roots()
        + validate_research_questions()
        + validate_argument_ledger()
        + validate_library_manifest()
        + validate_bibliography()
        + validate_research_background_separation()
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

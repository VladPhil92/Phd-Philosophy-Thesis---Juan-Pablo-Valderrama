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
    "ai/policy.md",
    "research/questions.md",
    "research/methodology.md",
    "research/sources/bibliography.bib",
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


def main() -> int:
    errors = (
        validate_required_paths()
        + validate_readmes()
        + validate_links()
        + validate_tracked_files()
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

"""Structural validation against schemas/argument.schema.* and
schemas/analysis-report.schema.*.

These constants mirror the schema files under ``schemas/`` by hand (see
DEVELOPER-GUIDE.md: no YAML/JSON schema engine dependency is added for two
small, stable object shapes). If you change one, change all three
(``*.schema.yaml``, ``*.schema.json``, and this file) together.

This module checks *form*, never content: it cannot and does not judge
whether a claim is true, an inference is sound, or a formalization is
faithful to the original text.
"""

from __future__ import annotations

from pathlib import Path

from .miner import parse_frontmatter

VALID_ARGUMENT_STATUSES = frozenset(
    {"IDEA", "DEVELOPING", "SUPPORTED", "CONTESTED", "READY_FOR_HUMAN_REVIEW", "VALIDATED", "REJECTED"}
)
VALID_HUMAN_VALIDATION_VALUES = frozenset({"pending", "validated"})
REQUIRED_ARGUMENT_FIELDS = ("argument_id", "status", "human_validation")

VALID_MODULES = frozenset(
    {"miner", "graph", "formalizer", "validator", "fallacy_analyzer", "concept_consistency", "stress_test"}
)
VALID_LOGICAL_STATUSES = frozenset(
    {"VALID", "INVALID", "SATISFIABLE", "UNSATISFIABLE", "UNKNOWN", "INCOMPLETE", "MISSING_PREMISE", "NOT_APPLICABLE"}
)
VALID_CONFIDENCE_VALUES = frozenset({"POSSIBLE", "LIKELY", "UNLIKELY", "NOT_DETECTED"})
VALID_REPORT_STATUSES = frozenset({"NOT_READY", "DEVELOPMENT_REQUIRED", "READY_FOR_HUMAN_REVIEW"})
REQUIRED_ANALYSIS_REPORT_FIELDS = ("argument_id", "module", "logical_status", "confidence", "human_review_required")


def validate_argument_frontmatter(frontmatter: dict[str, str]) -> list[str]:
    """Validate the frontmatter of an ARG-*.md file. Mirrors argument.schema.*."""
    errors: list[str] = []
    for field_name in REQUIRED_ARGUMENT_FIELDS:
        if not frontmatter.get(field_name):
            errors.append(f"Falta el campo obligatorio '{field_name}' en la cabecera.")

    status = frontmatter.get("status")
    if status is not None and status not in VALID_ARGUMENT_STATUSES:
        errors.append(f"status inválido: {status!r} (valores admitidos: {sorted(VALID_ARGUMENT_STATUSES)}).")

    human_validation = frontmatter.get("human_validation")
    if human_validation is not None and human_validation not in VALID_HUMAN_VALIDATION_VALUES:
        errors.append(
            f"human_validation inválido: {human_validation!r} "
            f"(valores admitidos: {sorted(VALID_HUMAN_VALIDATION_VALUES)})."
        )

    if status == "VALIDATED" and human_validation != "validated":
        errors.append("status es VALIDATED pero human_validation no es 'validated' explícitamente.")

    return errors


def validate_argument_file(path: str | Path) -> list[str]:
    content = Path(path).read_text(encoding="utf-8")
    return validate_argument_frontmatter(parse_frontmatter(content))


def validate_analysis_report_frontmatter(frontmatter: dict[str, str]) -> list[str]:
    """Validate the frontmatter of a PLAA analysis report. Mirrors analysis-report.schema.*."""
    errors: list[str] = []
    for field_name in REQUIRED_ANALYSIS_REPORT_FIELDS:
        if not frontmatter.get(field_name):
            errors.append(f"Falta el campo obligatorio '{field_name}' en el informe.")

    module = frontmatter.get("module")
    if module is not None and module not in VALID_MODULES:
        errors.append(f"module inválido: {module!r} (valores admitidos: {sorted(VALID_MODULES)}).")

    logical_status = frontmatter.get("logical_status")
    if logical_status is not None and logical_status not in VALID_LOGICAL_STATUSES:
        errors.append(
            f"logical_status inválido: {logical_status!r} (valores admitidos: {sorted(VALID_LOGICAL_STATUSES)})."
        )

    confidence = frontmatter.get("confidence")
    if confidence is not None and confidence not in VALID_CONFIDENCE_VALUES:
        errors.append(f"confidence inválido: {confidence!r} (valores admitidos: {sorted(VALID_CONFIDENCE_VALUES)}).")

    human_review_required = frontmatter.get("human_review_required")
    if human_review_required is not None and human_review_required.lower() != "true":
        errors.append(
            "human_review_required debe ser 'true' (Principio 4: todo hallazgo requiere revisión humana); "
            f"se encontró {human_review_required!r}."
        )

    report_status = frontmatter.get("report_status")
    if report_status == "VALIDATED":
        errors.append(
            "report_status no puede ser VALIDATED: esa palabra pertenece solo a la decisión del investigador "
            "sobre el ARG-*, nunca a un informe PLAA."
        )
    elif report_status is not None and report_status not in VALID_REPORT_STATUSES:
        errors.append(
            f"report_status inválido: {report_status!r} (valores admitidos: {sorted(VALID_REPORT_STATUSES)})."
        )

    return errors


def validate_analysis_report_file(path: str | Path) -> list[str]:
    content = Path(path).read_text(encoding="utf-8")
    return validate_analysis_report_frontmatter(parse_frontmatter(content))

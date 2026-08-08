"""AnalysisReport — the structured output object every PLAA judgment
module (3, 4, 5, 6, 7) must produce, per README.md "OUTPUT FORMAT" and
schemas/analysis-report.schema.*.

This module never fills in the judgment fields itself (``detected_problems``,
``counterargument``, etc. come from a prompt-guided session, see
prompts/*.md) — it only provides the shape and the structural validation,
and renders a filled report to Markdown for the researcher to read.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from . import schema_check


@dataclass(frozen=True)
class DetectedProblem:
    """One row of an analysis report's "problemas detectados" table."""

    description: str
    evidence_location: str
    confidence: str
    reviewed_as_possible_aporia: bool


@dataclass
class AnalysisReport:
    """A single PLAA module's output for one ARG-*."""

    argument_id: str
    module: str
    logical_status: str
    confidence: str
    repository_references: list[str]
    detected_problems: list[DetectedProblem] = field(default_factory=list)
    missing_premises: list[str] = field(default_factory=list)
    premises: list[str] = field(default_factory=list)
    conclusion: str = ""
    counterargument: str = ""
    source: str = ""
    human_review_required: bool = True
    report_status: str = "NOT_READY"

    def validate(self) -> list[str]:
        """Structural validation. Never judges whether the content is correct."""
        errors: list[str] = []

        if self.module not in schema_check.VALID_MODULES:
            errors.append(f"module inválido: {self.module!r}.")
        if self.logical_status not in schema_check.VALID_LOGICAL_STATUSES:
            errors.append(f"logical_status inválido: {self.logical_status!r}.")
        if self.confidence not in schema_check.VALID_CONFIDENCE_VALUES:
            errors.append(f"confidence inválido: {self.confidence!r}.")
        if self.report_status == "VALIDATED":
            errors.append("report_status no puede ser VALIDATED (pertenece solo al investigador).")
        elif self.report_status not in schema_check.VALID_REPORT_STATUSES:
            errors.append(f"report_status inválido: {self.report_status!r}.")
        if self.human_review_required is not True:
            errors.append("human_review_required debe ser True (Principio 4).")
        if not self.repository_references:
            errors.append("repository_references no puede estar vacío (Principio 7: no claim without traceability).")

        for index, problem in enumerate(self.detected_problems):
            if problem.confidence not in schema_check.VALID_CONFIDENCE_VALUES:
                errors.append(f"detected_problems[{index}].confidence inválido: {problem.confidence!r}.")
            if not problem.evidence_location.strip():
                errors.append(f"detected_problems[{index}] no cita evidence_location (Principio 6/7).")

        return errors

    def to_markdown(self) -> str:
        """Render following templates/analysis-report.md."""
        lines = [
            "---",
            f"argument_id: {self.argument_id}",
            f"module: {self.module}",
            f"logical_status: {self.logical_status}",
            f"confidence: {self.confidence}",
            f"human_review_required: {'true' if self.human_review_required else 'false'}",
            f"report_status: {self.report_status}",
            "---",
            "",
            f"# Informe de análisis PLAA — {self.argument_id}",
            "",
            f"**Módulo:** `{self.module}`",
        ]
        if self.source:
            lines.append(f"**Fuente:** `{self.source}`")
        lines += ["", "## Premisas consideradas", ""]
        if self.premises:
            lines += [f"{index + 1}. {premise}" for index, premise in enumerate(self.premises)]
        else:
            lines.append("(ninguna premisa citada en este informe)")
        if self.conclusion:
            lines += ["", "## Conclusión considerada", "", self.conclusion]
        lines += ["", "## Estado lógico", "", self.logical_status, "", "## Problemas detectados", ""]
        if self.detected_problems:
            lines.append("| Descripción | Ubicación de la evidencia | Confianza | ¿Revisado como posible aporía? |")
            lines.append("|---|---|---|---|")
            for problem in self.detected_problems:
                lines.append(
                    f"| {problem.description} | {problem.evidence_location} | {problem.confidence} | "
                    f"{'sí' if problem.reviewed_as_possible_aporia else 'no'} |"
                )
        else:
            lines.append("Sin problemas detectados en este análisis.")
        if self.missing_premises:
            lines += ["", "## Premisas faltantes", ""]
            lines += [f"- {premise}" for premise in self.missing_premises]
        if self.counterargument:
            lines += ["", "## Contraargumento", "", self.counterargument]
        lines += [
            "",
            "## Confianza global",
            "",
            self.confidence,
            "",
            "## Revisión humana requerida",
            "",
            "Sí (siempre).",
            "",
            "## Estado del informe",
            "",
            self.report_status,
            "",
            "## Referencias del repositorio",
            "",
        ]
        lines += [f"- {reference}" for reference in self.repository_references]
        return "\n".join(lines) + "\n"

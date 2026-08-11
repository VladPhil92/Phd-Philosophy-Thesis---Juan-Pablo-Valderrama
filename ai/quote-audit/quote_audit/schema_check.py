"""Structural validation against schemas/quote-audit.schema.*.

Mirrors ai/plaa/plaa/schema_check.py: these constants hand-mirror the
schema files under ``schemas/`` (see ARCHITECTURE.md, "Sin dependencias
nuevas"). If you change one, change all three (``.schema.yaml``,
``.schema.json``, and this file) together.

This module checks *form*, never content: it cannot and does not judge
whether a quote is philosophically relevant, contextually faithful, or
genuinely supports an argument's claim.
"""

from __future__ import annotations

import re

RECOMMENDED_STATUS_VALUES = frozenset(
    {
        "CANDIDATE",
        "SOURCE_LOCATED",
        "HUMAN_VERIFIED",
        "CONTEXT_AUDITED",
        "RELEVANCE_AUDITED",
        "APA7_READY",
        "READY_FOR_ARGUMENT_USE",
        "REJECTED_FOR_USE",
    }
)
# Statuses that assert a human already reviewed the quote; no AI session
# may produce these without the explicit human_verified: true marker.
STATUS_REQUIRES_HUMAN_MARKER = frozenset({"HUMAN_VERIFIED", "READY_FOR_ARGUMENT_USE"})

# Statuses at or beyond CONTEXT_AUDITED in the lifecycle, per CONFIG.yaml's
# recommended_status_vocabulary ordering.
_STATUS_ORDER = (
    "CANDIDATE",
    "SOURCE_LOCATED",
    "HUMAN_VERIFIED",
    "CONTEXT_AUDITED",
    "RELEVANCE_AUDITED",
    "APA7_READY",
    "READY_FOR_ARGUMENT_USE",
)


def _status_index(status: str | None) -> int:
    """Return the lifecycle position of ``status``, or -1 if unknown/None.

    REJECTED_FOR_USE is a terminal state outside the ladder, not "before
    CANDIDATE" — it never requires the context/relevance fields below.
    """
    if status in _STATUS_ORDER:
        return _STATUS_ORDER.index(status)
    return -1


CONTEXT_STATUS_VALUES = frozenset(
    {"SELF_CONTAINED", "CONTEXT_REQUIRED", "CONTEXT_CRITICAL", "POSSIBLY_MISLEADING"}
)
PHILOSOPHICAL_FUNCTION_VALUES = frozenset(
    {
        "DEFINITION",
        "TEXTUAL_EVIDENCE",
        "CONCEPTUAL_DISTINCTION",
        "AUTHOR_CLAIM",
        "ARGUMENT_PREMISE",
        "COUNTERARGUMENT",
        "INTERPRETIVE_SUPPORT",
        "HISTORICAL_CONTEXT",
        "EXAMPLE",
        "METHODOLOGICAL_STATEMENT",
        "RHETORICAL_ONLY",
        "UNDETERMINED",
    }
)
RELEVANCE_STATUS_VALUES = frozenset({"HIGH", "MEDIUM", "LOW", "NONE", "UNDETERMINED"})
ARGUMENTATIVE_SUPPORT_VALUES = frozenset(
    {
        "DIRECT_SUPPORT",
        "PARTIAL_SUPPORT",
        "CONTEXTUAL_SUPPORT",
        "ILLUSTRATIVE_ONLY",
        "NO_SUPPORT",
        "CONTRADICTS_CLAIM",
        "UNDETERMINED",
    }
)
# Support levels that do NOT justify using the quote as an ARG-*'s primary
# evidence — see rule_no_support_as_primary_evidence in the schema.
NON_SUPPORTING_VALUES = frozenset({"NO_SUPPORT", "CONTRADICTS_CLAIM"})
CLASSIFICATION_VALUES = frozenset(
    {
        "VERIFIED_RELEVANT",
        "VERIFIED_CONTEXT_NEEDED",
        "VERIFIED_WEAK_RELEVANCE",
        "CANDIDATE_ONLY",
        "MISLEADING_FRAGMENT",
        "UNVERIFIED",
        "APA_NONCOMPLIANT",
        "REJECTED_FOR_USE",
    }
)
CONFIDENCE_VALUES = frozenset({"POSSIBLE", "LIKELY", "UNLIKELY", "NOT_DETECTED"})
APA7_COMPLIANT_VALUES = frozenset({"true", "false", "partial"})
APA7_QUOTE_TYPE_VALUES = frozenset({"short", "block"})
APA7_BLOCK_QUOTE_WORD_THRESHOLD = 40

REQUIRED_FIELDS = ("quote_id", "source", "locator", "recommended_status")

_TRUE_STRINGS = frozenset({"true", "True", "TRUE", "1"})
_FALSE_STRINGS = frozenset({"false", "False", "FALSE", "0", ""})
_WORD = re.compile(r"\S+")


def _as_bool(value: object) -> bool | None:
    """Parse a flat-field string (or an already-bool value) as a boolean.

    Returns None if the value is absent or not recognizably boolean —
    callers must not conflate "false" with "field missing".
    """
    if isinstance(value, bool):
        return value
    if value is None:
        return None
    if value in _TRUE_STRINGS:
        return True
    if value in _FALSE_STRINGS:
        return False
    return None


def word_count(text: str) -> int:
    """Count words for the APA 7 40-word block-quote threshold."""
    return len(_WORD.findall(text or ""))


def validate_quote_audit_record(
    record: dict[str, object],
    *,
    known_bibliography_keys: set[str] | None = None,
    quoted_text: str | None = None,
    is_primary_evidence: bool | None = None,
) -> list[str]:
    """Validate one quote-audit record. Returns a list of error strings
    (empty means structurally valid).

    ``known_bibliography_keys``: if provided, ``source`` must be a member
    (test case: cita vinculada a BibTeX inexistente).
    ``quoted_text``: if provided, used to check the APA 7 40-word rule
    against ``apa7_quote_type`` (test case: cita de 40+ palabras).
    ``is_primary_evidence``: overrides record.get("primary_evidence") when
    the caller already knows how the quote is used in an ARG-*.
    """
    errors: list[str] = []

    for field_name in REQUIRED_FIELDS:
        if not record.get(field_name):
            errors.append(f"Falta el campo obligatorio '{field_name}' en el registro de auditoría.")

    quote_id = record.get("quote_id", "<sin quote_id>")

    status = record.get("recommended_status")
    if status is not None and status not in RECOMMENDED_STATUS_VALUES:
        errors.append(
            f"[{quote_id}] recommended_status inválido: {status!r} "
            f"(valores admitidos: {sorted(RECOMMENDED_STATUS_VALUES)})."
        )

    human_verified = _as_bool(record.get("human_verified"))
    if status in STATUS_REQUIRES_HUMAN_MARKER and human_verified is not True:
        errors.append(
            f"[{quote_id}] recommended_status={status!r} exige human_verified: true explícito "
            "(ninguna sesión de IA puede marcarlo por sí sola)."
        )

    source = record.get("source")
    if known_bibliography_keys is not None and source and source not in known_bibliography_keys:
        errors.append(
            f"[{quote_id}] source {source!r} no corresponde a ninguna clave de "
            "research/sources/bibliography.bib."
        )

    status_position = _status_index(status if isinstance(status, str) else None)
    context_required = status_position >= _status_index("CONTEXT_AUDITED") >= 0

    context_status = record.get("context_status")
    philosophical_function = record.get("philosophical_function")
    if context_required:
        if not context_status:
            errors.append(
                f"[{quote_id}] recommended_status={status!r} requiere 'context_status' "
                "(auditoría contextual) y no está presente."
            )
        if not philosophical_function:
            errors.append(
                f"[{quote_id}] recommended_status={status!r} requiere 'philosophical_function' "
                "y no está presente."
            )
    if context_status is not None and context_status not in CONTEXT_STATUS_VALUES:
        errors.append(
            f"[{quote_id}] context_status inválido: {context_status!r} "
            f"(valores admitidos: {sorted(CONTEXT_STATUS_VALUES)})."
        )
    if context_status == "POSSIBLY_MISLEADING" and _as_bool(record.get("human_review_required")) is not True:
        errors.append(
            f"[{quote_id}] context_status=POSSIBLY_MISLEADING exige human_review_required: true."
        )
    if philosophical_function is not None and philosophical_function not in PHILOSOPHICAL_FUNCTION_VALUES:
        errors.append(
            f"[{quote_id}] philosophical_function inválido: {philosophical_function!r} "
            f"(valores admitidos: {sorted(PHILOSOPHICAL_FUNCTION_VALUES)})."
        )

    relevance_required = status_position >= _status_index("RELEVANCE_AUDITED") >= 0
    relevance_status = record.get("relevance_status")
    if relevance_required and not relevance_status:
        errors.append(
            f"[{quote_id}] recommended_status={status!r} requiere 'relevance_status' y no está presente."
        )
    if relevance_status is not None and relevance_status not in RELEVANCE_STATUS_VALUES:
        errors.append(
            f"[{quote_id}] relevance_status inválido: {relevance_status!r} "
            f"(valores admitidos: {sorted(RELEVANCE_STATUS_VALUES)})."
        )
    if relevance_required and not record.get("reasoning_summary"):
        errors.append(
            f"[{quote_id}] recommended_status={status!r} requiere 'reasoning_summary' no vacío."
        )

    related_arg = record.get("related_ARG") or []
    argumentative_support = record.get("argumentative_support")
    if related_arg and not argumentative_support:
        errors.append(
            f"[{quote_id}] tiene related_ARG pero no declara 'argumentative_support'."
        )
    if argumentative_support is not None and argumentative_support not in ARGUMENTATIVE_SUPPORT_VALUES:
        errors.append(
            f"[{quote_id}] argumentative_support inválido: {argumentative_support!r} "
            f"(valores admitidos: {sorted(ARGUMENTATIVE_SUPPORT_VALUES)})."
        )

    primary_evidence = is_primary_evidence if is_primary_evidence is not None else _as_bool(record.get("primary_evidence"))
    if primary_evidence is True and argumentative_support in NON_SUPPORTING_VALUES:
        errors.append(
            f"[{quote_id}] argumentative_support={argumentative_support!r} pero la cita está marcada "
            "como evidencia principal (primary_evidence: true) — CONFLICT, no se puede usar así."
        )

    classification = record.get("classification")
    if classification is not None and classification not in CLASSIFICATION_VALUES:
        errors.append(
            f"[{quote_id}] classification inválida: {classification!r} "
            f"(valores admitidos: {sorted(CLASSIFICATION_VALUES)})."
        )

    confidence = record.get("confidence")
    if confidence is not None and confidence not in CONFIDENCE_VALUES:
        errors.append(
            f"[{quote_id}] confidence inválido: {confidence!r} (valores admitidos: {sorted(CONFIDENCE_VALUES)})."
        )

    errors.extend(
        _validate_apa7(
            record,
            quote_id=str(quote_id),
            quoted_text=quoted_text,
            known_bibliography_keys=known_bibliography_keys,
            source=source,
        )
    )

    return errors


def _validate_apa7(
    record: dict[str, object],
    *,
    quote_id: str,
    quoted_text: str | None,
    known_bibliography_keys: set[str] | None,
    source: object,
) -> list[str]:
    errors: list[str] = []
    compliant = record.get("apa7_compliant")
    if compliant is not None and str(compliant) not in APA7_COMPLIANT_VALUES:
        errors.append(
            f"[{quote_id}] apa7_compliant inválido: {compliant!r} "
            f"(valores admitidos: {sorted(APA7_COMPLIANT_VALUES)})."
        )

    quote_type = record.get("apa7_quote_type")
    if quote_type is not None and quote_type not in APA7_QUOTE_TYPE_VALUES:
        errors.append(
            f"[{quote_id}] apa7_quote_type inválido: {quote_type!r} "
            f"(valores admitidos: {sorted(APA7_QUOTE_TYPE_VALUES)})."
        )

    if quoted_text is not None:
        words = word_count(quoted_text)
        if words >= APA7_BLOCK_QUOTE_WORD_THRESHOLD and quote_type != "block":
            errors.append(
                f"[{quote_id}] la cita tiene {words} palabras (≥{APA7_BLOCK_QUOTE_WORD_THRESHOLD}): "
                "APA 7 exige apa7_quote_type: block (BLOCK_QUOTE_REQUIRED)."
            )

    locator_present = _as_bool(record.get("apa7_locator_present"))
    if locator_present is None:
        locator_present = bool(record.get("locator"))
    if locator_present is False:
        errors.append(f"[{quote_id}] apa7_locator_present es false: falta localizador exigido por APA 7.")

    bibliography_entry_found = _as_bool(record.get("apa7_bibliography_entry_found"))
    if bibliography_entry_found is None and known_bibliography_keys is not None and source:
        bibliography_entry_found = source in known_bibliography_keys
    if bibliography_entry_found is False:
        errors.append(
            f"[{quote_id}] apa7_bibliography_entry_found es false: no hay entrada bibliográfica "
            "correspondiente en research/sources/bibliography.bib."
        )

    return errors

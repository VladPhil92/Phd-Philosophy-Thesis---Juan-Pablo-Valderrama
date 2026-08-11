---
quote_id: derrida-CLAVE#cNN
source: derrida-CLAVE
locator: "p. 0"
recommended_status: CANDIDATE
human_verified: false
---

# Informe de auditoría de cita

> Sigue exactamente `../schemas/quote-audit.schema.yaml`. Un informe que
> omite un campo obligatorio no es válido (verificable con
> `quote_audit.schema_check.validate_quote_audit_record`).

**Fuente:** clave BibTeX en `research/sources/bibliography.bib`
**Ficha:** `research/sources/notes/<clave>.md`
**related_PI:** —
**related_ARG:** —

## Texto citado

> …

(Nunca reescrito. Cualquier corrección se hace en la ficha de fuente
original, no aquí.)

## Contexto mínimo

Párrafo anterior / posterior, o resumen suficiente para aplicar el test
de integridad contextual (`../prompts/01-context-integrity.md`).

## Autenticidad

Responsabilidad humana, ya resuelta en la ficha de fuente (localizador +
cotejo). Este informe no la re-verifica.

## Integridad contextual

`context_status`: `SELF_CONTAINED` | `CONTEXT_REQUIRED` | `CONTEXT_CRITICAL`
| `POSSIBLY_MISLEADING`

## Pertinencia filosófica

`philosophical_function`: (uno de los 12 valores, ver
`../prompts/02-philosophical-relevance.md`)
`relevance_status`: `HIGH` | `MEDIUM` | `LOW` | `NONE` | `UNDETERMINED`

## Riesgos

- `POSSIBLE_QUOTE_MINING` (si aplica, ver `../prompts/03-quote-mining-detection.md`)
- `INFERENTIAL_GAP` (si aplica, ver `../prompts/04-argumentative-support.md`)
- `APA7_HUMAN_REVIEW` (si aplica, ver `../prompts/05-apa7-structural.md`)

## Soporte argumentativo

Solo si `related_ARG` no está vacío.
`argumentative_support`: `DIRECT_SUPPORT` | `PARTIAL_SUPPORT` |
`CONTEXTUAL_SUPPORT` | `ILLUSTRATIVE_ONLY` | `NO_SUPPORT` |
`CONTRADICTS_CLAIM` | `UNDETERMINED`

## APA 7

```yaml
apa7:
  compliant: true/false/partial
  quote_type: short/block
  locator_present: true/false
  bibliography_entry_found: true/false
  issues:
    - …
```

## Nota interpretativa del investigador

(Espacio reservado, separado estrictamente del texto citado. La IA puede
proponer una `INTERPRETIVE QUESTION`, nunca fusionarla con la cita.)

## Resultado global

```yaml
classification: VERIFIED_RELEVANT | VERIFIED_CONTEXT_NEEDED |
  VERIFIED_WEAK_RELEVANCE | CANDIDATE_ONLY | MISLEADING_FRAGMENT |
  UNVERIFIED | APA_NONCOMPLIANT | REJECTED_FOR_USE

recommended_status: CANDIDATE | SOURCE_LOCATED | HUMAN_VERIFIED |
  CONTEXT_AUDITED | RELEVANCE_AUDITED | APA7_READY |
  READY_FOR_ARGUMENT_USE | REJECTED_FOR_USE

confidence: POSSIBLE | LIKELY | UNLIKELY | NOT_DETECTED

human_review_required: true/false

reasoning_summary: >
  Explicación breve, verificable y académicamente útil. No exponer
  razonamiento interno extenso.
```

## Decisión humana final

Ninguna de las siguientes se marca desde este informe — las escribe
exclusivamente Juan Pablo Valderrama Pino, fuera de este archivo:

- `APPROVED_FOR_INTERPRETIVE_USE`
- `APPROVED_FOR_ARGUMENTATIVE_USE`
- `APPROVED_FOR_MANUSCRIPT`

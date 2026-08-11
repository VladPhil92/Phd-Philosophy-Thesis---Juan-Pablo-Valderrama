# Ficha de fuente: [clave BibTeX]

**Estado:** idea
**Referencia verificada:** sí/no
**Tipo de lectura:** primaria/secundaria
**Fecha de consulta:** AAAA-MM-DD

## Registro de sesiones de lectura

> Una fila por sesión. Distingue **leído** (pasaje trabajado en su
> contexto argumentativo) de **consultado** (pasaje solo localizado, sin
> trabajar el argumento que lo rodea) — véase `research/methodology.md`
> §4. Las columnas de página y hora permiten calcular páginas leídas y
> ritmo de lectura; no se completan por estimación.

| Fecha | Hora inicio | Hora fin | Página inicial | Página final | Leído / consultado | Notas |
|---|---|---|---|---|---|---|
| | | | | | | |

## Tesis y propósito de la obra

## Conceptos relevantes

## Citas verificadas

> Incluir localizador exacto y distinguir la cita de la traducción propia.

## Auditoría de citas

> **Opcional.** No es necesario poblar esta sección para que una cita de
> «Citas verificadas» sea válida — autenticidad y localizador ya bastan
> para ese uso. Añade un bloque aquí solo cuando una cita concreta se
> somete a auditoría más profunda (típicamente antes de usarla como
> evidencia principal de un `ARG-*`, o antes de integrarla a un
> capítulo). Formato y vocabulario en
> [`ai/quote-audit/schemas/quote-audit.schema.yaml`](../ai/quote-audit/schemas/quote-audit.schema.yaml);
> criterios de juicio en `ai/quote-audit/prompts/`. Validable con
> `quote_audit.schema_check.validate_quote_audit_record`.

### Auditoría de citas: [quote_id, p. ej. clave-bibtex#cNN]

```text
quote_id: [clave-bibtex#cNN]
source: [clave BibTeX]
locator: [p. NN]
recommended_status: [CANDIDATE|SOURCE_LOCATED|HUMAN_VERIFIED|CONTEXT_AUDITED|RELEVANCE_AUDITED|APA7_READY|READY_FOR_ARGUMENT_USE|REJECTED_FOR_USE]
context_status: [SELF_CONTAINED|CONTEXT_REQUIRED|CONTEXT_CRITICAL|POSSIBLY_MISLEADING]
philosophical_function: [ver schema — 12 valores]
relevance_status: [HIGH|MEDIUM|LOW|NONE|UNDETERMINED]
related_PI: [PI-##, ...]
related_ARG: [ARG-###, ...]
argumentative_support: [solo si related_ARG no vacío — ver schema]
apa7_compliant: [true|false|partial]
apa7_quote_type: [short|block]
confidence: [POSSIBLE|LIKELY|UNLIKELY|NOT_DETECTED]
human_review_required: [true|false]
human_verified: [false — solo el investigador cambia esto a true]
classification: [ver schema — 8 valores]
reasoning_summary: [breve, verificable]
```

#### Texto citado

> (idéntico al de «Citas verificadas»; nunca reescrito aquí)

#### Contexto mínimo

#### Nota interpretativa del investigador

(separada estrictamente del texto citado — la IA puede sugerir una
pregunta interpretativa, nunca fusionarla con la cita)

#### Resultado de auditoría

(síntesis breve del bloque de campos de arriba, en prosa, para lectura
humana rápida)

## Paráfrasis e interpretación

## Relación con preguntas y argumentos

## Objeciones y límites

## Tareas pendientes

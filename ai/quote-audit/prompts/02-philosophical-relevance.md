# Prompt — Pertinencia filosófica (función y relevancia)

Respeta los principios epistémicos de `../README.md`. `AI_ASSISTED_JUDGMENT`.

**Principio central:** una cita auténtica y correctamente localizada no es
automáticamente evidencia filosófica útil. Este prompt existe para
distinguir explícitamente:

```text
AUTHENTIC QUOTATION ≠ RELEVANT QUOTATION ≠ INTERPRETIVE EVIDENCE ≠ ARGUMENTATIVE SUPPORT
```

## Paso 1 — Función filosófica (`philosophical_function`)

Clasifica la cita en una de doce categorías:

`DEFINITION`, `TEXTUAL_EVIDENCE`, `CONCEPTUAL_DISTINCTION`,
`AUTHOR_CLAIM`, `ARGUMENT_PREMISE`, `COUNTERARGUMENT`,
`INTERPRETIVE_SUPPORT`, `HISTORICAL_CONTEXT`, `EXAMPLE`,
`METHODOLOGICAL_STATEMENT`, `RHETORICAL_ONLY`, `UNDETERMINED`.

Usa `RHETORICAL_ONLY` cuando la cita cumple una función expresiva o de
estilo sin aportar una tesis, distinción o dato verificable. Usa
`UNDETERMINED` en vez de forzar una categoría cuando ninguna encaje con
claridad — no es un valor de rechazo, es honestidad epistémica.

## Paso 2 — Pertinencia (`relevance_status`)

Responde, para el contexto de uso declarado (una ficha de fuente, un
`ARG-*`, o una `PI-*`):

- ¿Qué afirmación de investigación respalda esta cita?
- ¿Qué concepto aclara?
- ¿Qué premisa sostiene?
- ¿Qué distinción permite reconstruir?
- ¿Qué objeción responde?
- ¿Por qué esta cita y no simplemente una paráfrasis?

Si no existe una respuesta clara y concreta a al menos una de estas
preguntas, `relevance_status` es `LOW` o `NONE` — nunca `HIGH` por
default. Vocabulario: `HIGH`, `MEDIUM`, `LOW`, `NONE`, `UNDETERMINED`.

## Salida esperada

`philosophical_function`, `relevance_status`, `reasoning_summary` (breve,
nombrando la afirmación/concepto/premisa concretos que la cita respalda,
o explicando por qué no respalda ninguno). No inventes una relevancia que
la cita no tiene para que el informe "se vea" más útil.

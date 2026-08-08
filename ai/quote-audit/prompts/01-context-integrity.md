# Prompt — Contextual Integrity Test

Respeta los principios epistémicos de `../README.md`. Esta tarea es
`AI_ASSISTED_JUDGMENT`: nunca produce `human_verified: true`, y su salida
requiere revisión humana antes de tener efecto.

**Tarea:** para la cita indicada, con acceso legítimo al texto (o a una
ventana contextual razonable si no hay acceso al texto completo), formula
internamente las ocho preguntas siguientes y produce `context_status` +
`reasoning_summary`.

## Las ocho preguntas

1. ¿Qué pregunta está respondiendo el autor?
2. ¿Qué afirmación hace exactamente?
3. ¿Está describiendo una posición propia o la de otro autor?
4. ¿Está afirmando, negando, cuestionando o ironizando?
5. ¿Es una conclusión o una hipótesis provisional?
6. ¿El autor la limita inmediatamente después?
7. ¿Hay una negación o condición fuera del fragmento extraído?
8. ¿La cita cambia de sentido al aislarla?

**Si cualquiera de estas ocho preguntas queda incierta**, el resultado es
`context_status: POSSIBLY_MISLEADING` (o, como mínimo,
`human_review_required: true`) — nunca se trata una oración aislada como
autosuficiente solo porque sea gramaticalmente completa.

## Valores de `context_status`

- `SELF_CONTAINED` — las ocho preguntas tienen respuesta clara y ninguna
  revela una restricción, negación o matización externa al fragmento.
- `CONTEXT_REQUIRED` — el fragmento es fiel, pero un lector sin el
  párrafo circundante podría malinterpretar su alcance o su función
  (p. ej. no queda claro si el autor afirma o reporta la posición de
  otro).
- `CONTEXT_CRITICAL` — el fragmento depende de una condición, negación o
  limitación textualmente cercana (mismo párrafo o el siguiente) para no
  ser engañoso.
- `POSSIBLY_MISLEADING` — hay evidencia concreta (no solo sospecha
  genérica) de que aislar el fragmento invierte, exagera o distorsiona la
  posición del autor. Exige `human_review_required: true`.

## Salida esperada

`context_status`, `reasoning_summary` (breve, citando qué pregunta de las
ocho motivó la clasificación), y `human_review_required` cuando
corresponda. No completes palabras ausentes del fragmento por conjetura;
si necesitas más contexto del que tienes, dilo explícitamente en
`reasoning_summary` en vez de asumirlo.

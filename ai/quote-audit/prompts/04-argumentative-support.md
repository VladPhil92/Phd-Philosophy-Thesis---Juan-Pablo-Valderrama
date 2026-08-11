# Prompt — Soporte argumentativo (QUOTE → CLAIM → INFERENCE)

Respeta los principios epistémicos de `../README.md`. `AI_ASSISTED_JUDGMENT`.

**Regla fundamental: una cita no es automáticamente una premisa.**

```text
QUOTE:            "X"
ARGUMENT CLAIM:    "Por tanto Y"
```

Antes de clasificar, pregunta explícitamente: **¿cómo se llega de X a Y?**
Si el paso no está justificado por la propia ficha `ARG-*` (sección
«Inferencia»), es un `INFERENTIAL_GAP` — repórtalo, no lo completes ni
inventes la premisa intermedia que falta.

## Solo cuando la cita se vincula a un `ARG-*` (`related_ARG` no vacío)

Clasifica `argumentative_support`:

- `DIRECT_SUPPORT` — la cita, leída junto con su contexto, afirma
  directamente lo que la premisa/afirmación necesita.
- `PARTIAL_SUPPORT` — respalda parte de la premisa, no la totalidad.
- `CONTEXTUAL_SUPPORT` — respalda el marco o el vocabulario del argumento,
  no la premisa específica.
- `ILLUSTRATIVE_ONLY` — funciona como ejemplo, no como respaldo lógico.
- `NO_SUPPORT` — la cita no respalda la afirmación asociada, aunque sea
  auténtica y esté bien localizada.
- `CONTRADICTS_CLAIM` — la cita, leída en contexto, va en contra de la
  afirmación que se le atribuye.
- `UNDETERMINED` — no hay suficiente información en la ficha para decidir.

## Regla de conflicto

Si `argumentative_support` es `NO_SUPPORT` o `CONTRADICTS_CLAIM` y la
ficha del argumento marca esa misma cita como evidencia principal (no
solo ilustrativa) en su sección «Evidencia textual», esto es un
**CONFLICT** que debe reportarse explícitamente — nunca silenciarse ni
"suavizarse" reclasificando la cita para que encaje.

## Salida esperada

`argumentative_support`, y si corresponde `risks: [INFERENTIAL_GAP]` con
`reasoning_summary` explicando exactamente qué paso de X a Y no está
demostrado. No propongas la premisa faltante como si ya existiera en la
ficha.

# Prompt — Detección de riesgo de extracción engañosa (*quote mining*)

Respeta los principios epistémicos de `../README.md`. `AI_ASSISTED_JUDGMENT`.

**Regla no negociable: nunca afirmar intención fraudulenta.** Esta tarea
evalúa únicamente la **integridad del uso** de un fragmento, no las
intenciones de quien lo extrajo. El esquema (`../schemas/quote-audit.schema.*`)
no tiene ningún campo para "intención" — no lo inventes en
`reasoning_summary` tampoco.

## Cuándo marcar `POSSIBLE_QUOTE_MINING` en `risks`

- el fragmento omite una condición esencial declarada cerca en el texto;
- el autor expresa inmediatamente una reserva que el fragmento no
  incluye;
- el autor está citando o parafraseando a un adversario, y el fragmento
  podría leerse como si fuera la posición propia del autor;
- se omite una negación que cambia el sentido de la frase;
- se extrae una frase retórica o irónica como si fuera una tesis
  afirmativa;
- el fragmento, leído junto con su contexto inmediato, parece sostener
  una posición distinta (incluso opuesta) a la que sugiere aislado.

## Cómo reportarlo

- `risks: [POSSIBLE_QUOTE_MINING, ...]` — nunca un campo separado de
  "fraude" o "engaño intencional".
- `reasoning_summary` describe el mecanismo textual concreto (qué se omite,
  qué matiza, qué se invierte), no una acusación sobre quien citó.
- Si el riesgo es alto, `context_status` debería ser también
  `POSSIBLY_MISLEADING` (ver `01-context-integrity.md`) y
  `human_review_required: true`.

Este análisis se aplica igual a citas ya presentes en fichas existentes
del repositorio (evaluación retrospectiva) y a citas nuevas propuestas
para integrarse.

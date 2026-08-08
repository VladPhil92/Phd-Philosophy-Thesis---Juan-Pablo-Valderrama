# Lista de verificación de falacias — ARG-000

> Cada fila requiere justificación textual, no una intuición. `NOT_DETECTED`
> es el valor por defecto y no requiere justificación extensa; cualquier
> otro valor sí. Ninguna fila puede afirmar certeza absoluta: el
> vocabulario admitido es exactamente `POSSIBLE` / `LIKELY` / `UNLIKELY` /
> `NOT_DETECTED` (véase `plaa/fallacy_checklist.py`).

| Falacia | Veredicto | Justificación (con ubicación textual) |
|---|---|---|
| Ad hominem | NOT_DETECTED | |
| Hombre de paja (strawman) | NOT_DETECTED | |
| Falso dilema | NOT_DETECTED | |
| Petición de principio (begging the question) | NOT_DETECTED | |
| Afirmación del consecuente | NOT_DETECTED | |
| Negación del antecedente | NOT_DETECTED | |
| Equivocación | NOT_DETECTED | |
| Falsa causa | NOT_DETECTED | |
| Falacia de composición | NOT_DETECTED | |
| Falacia de división | NOT_DETECTED | |
| Circularidad | NOT_DETECTED | |
| Generalización apresurada | NOT_DETECTED | |
| Apelación a la autoridad | NOT_DETECTED | |

## Capa de seguridad hermenéutica

Para cada fila marcada `POSSIBLE` o `LIKELY`: ¿podría tratarse de una
aporía, una tensión dialéctica productiva o una ambigüedad deliberada del
autor, en vez de un error? Si la respuesta es plausible, marca
`reviewed_as_possible_aporia: true` en el informe de análisis
correspondiente y usa el estado `PHILOSOPHICAL_REVIEW_REQUIRED` en vez de
tratarlo como un defecto (véase `prompts/08-hermeneutic-safety-layer.md`).

# Arquitectura de Quote Audit

## Decisión de diseño central

Igual que PLAA (`ai/plaa/ARCHITECTURE.md`), cada capacidad exigida es
determinista o de juicio, y este documento no disfraza una de otra:

- **Determinista (código Python, `quote_audit/*.py`).** Presencia y
  formato de campos, validez de valores frente a un vocabulario cerrado,
  el umbral de 40 palabras de APA 7, existencia de la clave BibTeX,
  candados de estado que exigen marca humana explícita. Todo esto es
  verificable mecánicamente y tiene pruebas en `tests/`.
- **De juicio (`prompts/*.md`, sesión de IA + revisión humana).**
  Integridad contextual, función filosófica, pertinencia, riesgo de
  *quote mining*, y si una cita realmente sostiene una afirmación. Ninguna
  de estas tareas se resuelve con longitud, palabras clave o similitud
  semántica — el propio encargo que originó este componente lo prohíbe
  explícitamente. El código valida la **forma** de la salida de juicio
  (que declare confianza, que use el vocabulario permitido, que nunca
  imprima `HUMAN_VERIFIED` ni `APPROVED_FOR_*`), nunca su contenido
  filosófico.

| Bloque del encargo original | Tipo | Implementación | Qué valida el código |
|---|---|---|---|
| A. Autenticidad | Humana (fuera de este componente) | — | Quote Audit no re-verifica autenticidad; parte de una cita ya cotejada por el investigador (`.claude/rules/sources.md`). |
| B. Localización | Determinista | `quote_audit/schema_check.py` | Presencia de `locator`; que `source` resuelva a una clave real de `research/sources/bibliography.bib` (`quote_audit/parser.py`). |
| C. Contexto (Contextual Integrity Test) | De juicio | `prompts/01-context-integrity.md` | El código exige que `context_status` use uno de los cuatro valores admitidos y que, si es `POSSIBLY_MISLEADING` o si alguna de las 8 preguntas queda incierta, `human_review_required: true`. |
| Pertinencia filosófica (`philosophical_function`, `relevance_status`) | De juicio | `prompts/02-philosophical-relevance.md` | El código exige `philosophical_function` de un catálogo cerrado de 12 valores y `relevance_status` de 5 valores, cada uno con `reasoning_summary` no vacío. No decide el valor. |
| Detección de *quote mining* | De juicio | `prompts/03-quote-mining-detection.md` | El código permite `POSSIBLE_QUOTE_MINING` en `risks`, nunca una afirmación de fraude — el prompt lo prohíbe explícitamente y el esquema no admite un campo de "intención". |
| Relación con interpretación (`supports`, `argumentative_support`) | De juicio + determinista | `prompts/04-argumentative-support.md` produce el juicio; `quote_audit/schema_check.py` exige que, si `argumentative_support` no es `DIRECT_SUPPORT`, se declare `INFERENTIAL_GAP` o una nota equivalente en `reasoning_summary` | El código nunca infiere ni completa el paso argumentativo faltante. |
| APA 7 | Determinista (subconjunto documentado) | `quote_audit/schema_check.py`, reglas listadas en `prompts/05-apa7-structural.md` | Solo las reglas estructurales que el propio documento declara implementadas (umbral de 40 palabras, localizador, correspondencia bibliográfica). Todo lo demás queda marcado `APA7_HUMAN_REVIEW` explícitamente — "no inventes reglas". |
| Estados de cita y candado `HUMAN_VERIFIED` | Determinista | `quote_audit/schema_check.py` | Mismo patrón que el candado `VALIDATED`/`human_validation` de `ai/plaa/plaa/schema_check.py`: ninguna sesión de IA puede producir `human_verified: true`; si `recommended_status` es `HUMAN_VERIFIED` sin ese campo, es error. |

## Objeto de auditoría

Toda auditoría de una cita produce un **registro de auditoría de cita**
(véase `schemas/quote-audit.schema.yaml` y `templates/quote-audit-report.md`)
con los campos que exige el encargo original: identificador de cita,
fuente, localizador, integridad textual, integridad contextual, función
filosófica, pertinencia, soporte argumentativo, estado APA 7, riesgos,
estado recomendado, confianza, necesidad de revisión humana, resumen de
razonamiento y clasificación final.

## Reutilización explícita de PLAA

`confidence_vocabulary` (`POSSIBLE`, `LIKELY`, `UNLIKELY`, `NOT_DETECTED`)
se reutiliza tal cual de `ai/plaa/CONFIG.yaml` — mismo vocabulario, mismo
significado, sin inventar uno nuevo para esta capa. Véase `CONFIG.yaml`
de este paquete.

## Sin dependencias nuevas

Misma política que `ai/plaa/` y `scripts/auditar_repositorio.py`:
solo biblioteca estándar (`re`, `dataclasses`, `pathlib`). Los archivos
`schemas/*.schema.yaml` y `schemas/*.schema.json` son documentación de
referencia para personas; `quote_audit/schema_check.py` implementa las
mismas reglas como constantes Python, mantenidas sincronizadas a mano con
ambos archivos de esquema — si divergen, se corrigen los tres a la vez.

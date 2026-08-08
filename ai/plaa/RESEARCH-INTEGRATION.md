# Cómo PLAA se integra con el resto del repositorio

PLAA no crea un sistema de identificadores, metodología o política de IA
paralelos. Reutiliza lo que ya existe.

## Identificadores reutilizados

- `PI-*` (`research/questions.md`) — un informe de análisis PLAA hereda las
  preguntas de investigación ya declaradas en el `ARG-*` auditado; no las
  reinterpreta ni les asigna nuevas.
- `ARG-*` (`research/argument-ledger/`) — unidad de entrada de todo módulo
  PLAA. PLAA nunca crea un `ARG-*` nuevo.
- `IA-AAAA-MM-DD-NN` (`ai/`, `templates/registro-ia.md`) — toda sesión que
  use un prompt de PLAA y cuyo resultado influya materialmente en un
  argumento se registra igual que cualquier otra intervención de IA, con
  el mismo formato y las mismas reglas de `.claude/rules/ai-transparency.md`.
- Claves BibTeX (`research/sources/bibliography.bib`) — un informe PLAA
  puede citar una clave existente al referirse a evidencia; nunca inventa
  ni verifica una clave nueva (eso es competencia de
  `.claude/rules/sources.md` y de `epistemic-auditor`).

## Documentos reutilizados, no duplicados

- **Metodología filosófica:** PLAA no define método. Si un módulo PLAA
  (p. ej. formalización) presupone una postura metodológica no resuelta en
  `research/methodology.md`, el informe debe declararlo como
  `HUMAN_DECISION_REQUIRED`, remitiendo a la sección correspondiente de
  ese documento en vez de asumir una respuesta.
- **Política de IA:** `ai/policy.md` y `AI-RESEARCH-PROTOCOL.md` siguen
  siendo la autoridad sobre qué constituye una intervención material de IA
  y cómo se registra. PLAA no añade una política paralela.
- **Provenance:** la cadena `PI → SRC → NOTE → QUOTE → ARG → OBJ → AI →
  REV → CHAPTER` de `governance/provenance.md` sigue siendo la única
  cadena de trazabilidad. Un informe PLAA es, en esa cadena, un artefacto
  del eslabón `AI` que puede afectar a `ARG` y a `OBJ` — no un eslabón
  nuevo.
- **Auditoría general:** `epistemic-auditor` sigue siendo responsable de
  procedencia, respaldo de citas y estado de validación humana de
  cualquier ficha del repositorio (`ARG-*`, fuentes, registros de IA).
  PLAA es un complemento más estrecho, centrado en forma lógica y
  consistencia conceptual, no un reemplazo.

## Relación con `.claude/agents/epistemic-auditor.md`

`epistemic-auditor` puede usar los prompts de PLAA como parte de su propio
proceso al auditar la categoría «vacíos inferenciales» y «objeciones» de
un `ARG-*` (véase su definición), pero PLAA no es en sí mismo un subagente
de Claude Code (véase la sección «Cómo se invoca hoy» de `README.md`) —
mantiene la restricción de «un solo subagente por ahora» de
`governance/decision-log.md` (DEC-003).

## Relación con `scripts/auditar_repositorio.py`

El auditor de repositorio comprueba invariantes documentales globales
(enlaces, IDs duplicados, estado epistémico válido). No ejecuta PLAA ni
depende de él. `plaa/schema_check.py` es deliberadamente independiente y
puede evolucionar sin tocar `scripts/auditar_repositorio.py`; si en el
futuro conviene que el auditor general también valide informes PLAA
guardados en el repositorio, esa integración debe decidirse y
justificarse por separado (véase `ROADMAP.md`).

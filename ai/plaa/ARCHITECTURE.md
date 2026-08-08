# Arquitectura de PLAA

## Decisión de diseño central

Cada uno de los ocho módulos exigidos requiere uno de dos tipos de
capacidad, y este documento los distingue sin disfrazar uno de otro:

- **Determinista (código Python).** Tareas mecánicas y verificables:
  extraer secciones marcadas de un Markdown con frontmatter YAML conocido,
  construir un grafo a partir de relaciones ya declaradas explícitamente,
  validar que una estructura de datos cumple un esquema. Esto se implementa
  en `plaa/*.py` y tiene pruebas deterministas en `tests/`.
- **De juicio (sesión de IA guiada por prompt + revisión humana).**
  Tareas que requieren comprensión semántica real: detectar una falacia
  posible, formalizar un argumento en lógica proposicional, generar la
  mejor objeción posible. Ninguna de estas tareas se resuelve con
  expresiones regulares ni heurísticas superficiales disfrazadas de
  análisis lógico — eso sería «magia de IA», exactamente lo que este
  componente debe evitar. Se implementan como plantillas de prompt en
  `prompts/*.md` que instruyen a una sesión de Claude Code (hoy) o a un
  motor simbólico configurado (en el futuro, vía `validator_interfaces.py`)
  a producir una salida que **el código sí puede validar
  estructuralmente**: que declare confianza, que cite evidencia, que use
  solo el vocabulario permitido, que nunca imprima `VALIDATED`.

La tabla siguiente asigna cada módulo del encargo original a esta
distinción.

| Módulo | Tipo | Implementación | Qué valida el código |
|---|---|---|---|
| 1. Argument Miner | Determinista | `plaa/miner.py` | Extrae CLAIM/PREMISE/OBJECTION/… de las secciones ya presentes en `templates/ficha-argumento.md` (mapeo de encabezados en español a tipos canónicos en inglés). No infiere nada que no esté ya delimitado por un encabezado. |
| 2. Argument Graph | Determinista | `plaa/graph.py` | Construye nodos/aristas a partir de: (a) frontmatter de `ARG-*`, (b) `research/argument-map.md`, (c) los subnodos que produce el miner. No infiere relaciones no declaradas. |
| 3. Logical Formalizer | De juicio + determinista | `prompts/03-logical-formalizer.md` produce la reconstrucción; `plaa/schema_check.py` valida que nunca sobrescribe el texto original y que queda marcada `provisional` | El código nunca genera la formalización; solo valida su forma y su estado. |
| 4. Logical Validator | Interfaz para motor futuro | `plaa/validator_interfaces.py` | Define el contrato (`LogicalValidatorEngine`) para SAT/SMT/Prolog/Lean/Coq/Z3. Hoy solo existe `NullValidatorEngine`, que siempre responde `INCOMPLETE` con la razón «no hay motor simbólico configurado». Ningún motor real está integrado. |
| 5. Fallacy Analyzer | De juicio + determinista | `prompts/05-fallacy-analyzer.md` produce el juicio; `plaa/fallacy_checklist.py` fija el catálogo cerrado de falacias y el vocabulario `POSSIBLE`/`LIKELY`/`UNLIKELY`/`NOT_DETECTED` que la salida debe usar | El código rechaza cualquier salida que use un vocabulario de certeza distinto (p. ej. «es una falacia»). |
| 6. Concept Consistency Engine | De juicio + determinista | `prompts/06-concept-consistency.md` produce el análisis; `plaa/miner.py` aporta las apariciones textuales del concepto que el juicio debe citar | El código no decide si hay deriva conceptual; exige que cada afirmación de deriva cite al menos dos apariciones concretas. |
| 7. Argument Stress Test | De juicio | `prompts/07-stress-test.md` | El código valida solo la forma del informe (campos obligatorios presentes), nunca la calidad de la objeción generada. |
| 8. Hermeneutic Safety Layer | Regla transversal, no módulo aislado | `prompts/08-hermeneutic-safety-layer.md`, referenciada obligatoriamente desde los prompts 3, 4, 5 y 7 | El código exige que todo hallazgo de tipo `ERROR`/`INVALID`/`CONTRADICTION` incluya explícitamente el campo `revisado_como_posible_aporia: true/false` antes de aceptarse como bien formado. |

## Objeto de análisis y objeto de concepto

Toda auditoría de un `ARG-*` produce un **informe de análisis** (véase
`schemas/analysis-report.schema.yaml` y `templates/analysis-report.md`) con
los campos exigidos por el encargo original: identificador del argumento,
fuente, premisas, conclusión, formalización, estado lógico, problemas
detectados, premisas faltantes, ambigüedad conceptual, falacias posibles,
contraargumento, confianza, necesidad de revisión humana y referencias al
repositorio.

Un **concepto** (`schemas/concept.schema.yaml`) es cualquier término que el
motor 6 rastree a través de fichas de fuente y argumento (p. ej.
«soberanía», «hospitalidad», «comunidad», «animal»), con sus apariciones y
posibles definiciones divergentes.

## Principios SOLID aplicados

- **Responsabilidad única:** cada archivo en `plaa/` hace una sola cosa
  (extraer, construir grafo, validar esquema, definir interfaz de
  validador, fijar catálogo de falacias, renderizar informe).
- **Abierto/cerrado:** `validator_interfaces.py` permite añadir un motor
  simbólico nuevo (Z3, Lean…) sin modificar el código que ya lo consume;
  basta implementar el protocolo `LogicalValidatorEngine`.
- **Sustitución de Liskov:** cualquier implementación de
  `LogicalValidatorEngine` (incluida `NullValidatorEngine`) es
  intercambiable donde se espera la interfaz.
- **Segregación de interfaces:** el miner no depende del grafo ni de los
  esquemas; el chequeo de esquema no depende del miner.
- **Inversión de dependencias:** `report.py` depende de la interfaz
  `LogicalValidatorEngine`, no de una implementación concreta.
- **Composición sobre herencia:** `graph.py` compone nodos y aristas como
  `dataclasses` simples; no hay jerarquías de clases profundas.

## Sin dependencias nuevas

Todo el paquete usa exclusivamente la biblioteca estándar de Python
(`re`, `dataclasses`, `json`, `enum`, `pathlib`). No se añade PyYAML,
`jsonschema` ni ningún paquete externo como dependencia de ejecución,
siguiendo la misma política que `scripts/auditar_repositorio.py`. Los
archivos `schemas/*.schema.yaml` y `schemas/*.schema.json` son
documentación de referencia para personas (y, en el caso del `.json`, un
artefacto reutilizable si en el futuro se añade `jsonschema` como
dependencia real). `plaa/schema_check.py` no los parsea en tiempo de
ejecución: implementa las mismas reglas como constantes Python
(`REQUIRED_ARGUMENT_FIELDS`, `VALID_STATUSES`, etc.) que deben mantenerse
sincronizadas manualmente con ambos archivos de esquema. Esta duplicación
deliberada es más simple y más auditable que añadir un motor de validación
de esquemas genérico para dos objetos con forma tan estable.

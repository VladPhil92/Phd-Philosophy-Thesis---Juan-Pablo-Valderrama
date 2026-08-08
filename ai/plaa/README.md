# PLAA — Auditor Lógico y Argumental Filosófico

**Philosophical Logic & Argument Auditor**

**Estado:** infraestructura inicial, sin argumentos reales auditados todavía.

## Qué es

PLAA es un componente de auditoría epistémica para las fichas `ARG-*` de
[`research/argument-ledger/`](../../research/argument-ledger/). Examina un
argumento ya redactado por el investigador y reporta, de forma estructurada,
posibles problemas de forma: premisas faltantes, inferencias no
demostradas, ambigüedad conceptual, falacias posibles, contraejemplos y
objeciones no consideradas.

## Qué NO es

- **No es un asistente de escritura.** No redacta argumentos, capítulos ni
  conclusiones.
- **No es un chatbot filosófico.** No sostiene una conversación abierta
  sobre las tesis del investigador.
- **No decide verdad filosófica.** Nunca falla la validez de un argumento
  ni resuelve una disputa interpretativa por su cuenta.
- **No es un motor de lógica simbólica.** No incluye (todavía) un SAT/SMT
  solver, Prolog, Lean, Coq ni Z3. Define interfaces para integrarlos en el
  futuro, pero hoy responde `INCOMPLETE` cuando se le pide una verificación
  formal real (véase [`plaa/validator_interfaces.py`](plaa/validator_interfaces.py)).
- **No sustituye al auditor epistémico general.** El subagente
  `.claude/agents/epistemic-auditor.md` audita procedencia, fuentes y estado
  de validación humana de todo el repositorio. PLAA es más estrecho:
  audita la **forma lógica y conceptual** de un argumento ya existente.

## Principios epistémicos (obligatorios en todo módulo)

1. La IA nunca determina verdad filosófica.
2. Toda formalización es una reconstrucción, no el significado del autor.
3. Todo hallazgo lógico declara su nivel de confianza.
4. Todo hallazgo requiere revisión humana antes de tener efecto en el
   manuscrito o en el estado epistémico de un `ARG-*`.
5. Toda formalización permanece provisional hasta aprobación humana.
6. La evidencia precede a la inferencia: no se reporta un problema lógico
   sin señalar en qué texto concreto se apoya.
7. Ningún hallazgo carece de trazabilidad hacia el `ARG-*`, la sección y,
   cuando aplique, la fuente citada.

Véase [`ARCHITECTURE.md`](ARCHITECTURE.md) para cómo cada módulo cumple
estos principios, y [`RESEARCH-INTEGRATION.md`](RESEARCH-INTEGRATION.md)
para cómo PLAA se conecta con el resto del repositorio sin duplicar
sistemas existentes.

## Cómo se invoca hoy

PLAA no es (todavía) un subagente de Claude Code independiente —
`CLAUDE.md` y `governance/decision-log.md` (DEC-003) restringen este
repositorio a un único subagente (`epistemic-auditor`) mientras no exista
material real que auditar. Hoy, PLAA se usa de dos maneras:

1. **Como paquete Python** (`ai/plaa/plaa/`) para las tareas puramente
   estructurales y deterministas: extraer secciones de una ficha `ARG-*`,
   construir el grafo de relaciones, y validar que un informe de análisis
   cumple el esquema exigido.
2. **Como conjunto de plantillas de prompt** (`ai/plaa/prompts/`) que un
   investigador puede pegar en una sesión de Claude Code (o dar a
   `epistemic-auditor`) para pedir un análisis de un módulo concreto sobre
   un `ARG-*` específico. La salida de esa sesión se valida después con
   `plaa.schema_check` antes de considerarse un informe completo.

Véase [`ROADMAP.md`](ROADMAP.md) para cuándo tendría sentido promover PLAA
a subagente propio.

## Mapa de archivos

```text
ai/plaa/
  README.md                     este documento
  ARCHITECTURE.md               los 8 módulos y cómo se implementan
  DEVELOPER-GUIDE.md            cómo extender el paquete Python
  USER-GUIDE.md                 cómo el investigador pide una auditoría
  RESEARCH-INTEGRATION.md       cómo PLAA reutiliza PI-*/ARG-*/IA-* y el resto del repositorio
  ROADMAP.md                    qué falta y cuándo tendría sentido construirlo
  CONFIG.yaml                   módulos habilitados, vocabulario de confianza, motor simbólico configurado
  schemas/                      especificación de objetos Argument y Concept (YAML + JSON)
  templates/                    plantillas Markdown para cada tipo de informe
  prompts/                      instrucciones de módulo para sesiones de Claude Code
  plaa/                         paquete Python (parsing, grafo, validación de esquema, interfaces de validador simbólico)
  tests/                        pruebas del paquete Python, con fixture ficticio
  examples/                     un análisis de ejemplo completo, explícitamente ficticio
```

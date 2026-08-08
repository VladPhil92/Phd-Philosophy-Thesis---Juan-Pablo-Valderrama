# Quote Audit — Auditoría filosófica de citas

**Estado:** infraestructura inicial, sin citas reales auditadas todavía
(véase `examples/ARG-001-quotes-audit.md` para una demostración sobre
citas ya verificadas del corpus).

## Qué es

Quote Audit es un componente de auditoría epistémica para las citas
registradas en `research/sources/notes/**` (sección «Citas verificadas» y,
cuando se audite una cita concreta, el bloque opcional «Auditoría de
citas» de `templates/ficha-fuente.md`). Examina una cita ya localizada y
cotejada por el investigador y reporta, de forma estructurada, si además
de auténtica es: contextualmente íntegra, filosóficamente relevante, y
capaz de sostener el argumento al que se asocia.

## Por qué existe: la distinción que resuelve

```text
AUTHENTIC QUOTATION  ≠  RELEVANT QUOTATION  ≠  INTERPRETIVE EVIDENCE  ≠  ARGUMENTATIVE SUPPORT
```

Antes de este componente, "cita verificada" en este repositorio
significaba únicamente "auténtica, localizada y cotejada contra la
edición" (véase `.claude/rules/sources.md`). Eso sigue siendo necesario
pero no es suficiente para que una cita sostenga un argumento: una frase
puede ser auténtica y estar perfectamente localizada, y aun así ser
trivial, estar fuera de contexto, o no respaldar la afirmación a la que
se asocia. Quote Audit añade esa capa, sin sustituir la verificación de
autenticidad que ya hace el investigador.

## Qué NO es

- **No re-verifica autenticidad.** Que una cita coincida literalmente con
  la edición sigue siendo responsabilidad exclusiva del investigador
  (`.claude/rules/sources.md`); Quote Audit parte de que ese cotejo ya
  ocurrió y evalúa lo que viene después.
- **No es un motor de similitud semántica.** No usa keywords, longitud ni
  comparación vectorial para decidir relevancia filosófica — eso es
  precisamente el error que este componente existe para evitar. La
  relevancia, la integridad contextual y el riesgo de *quote mining* son
  siempre `AI_ASSISTED_JUDGMENT`: una sesión de IA los evalúa siguiendo
  los criterios de `prompts/`, y el resultado exige revisión humana antes
  de tener efecto.
- **No sustituye a PLAA.** PLAA (`ai/plaa/`) audita si la *inferencia* de
  un argumento funciona (premisas → conclusión). Quote Audit audita si la
  *evidencia* que alimenta esas premisas es legítima y relevante. Son
  capas sucesivas, no alternativas:

  ```text
  QUOTE AUDIT → ¿la evidencia es legítima y relevante?
       ↓
  ARGUMENT (ARG-*)
       ↓
  PLAA → ¿la inferencia funciona?
  ```

- **No sustituye al auditor epistémico general.** `.claude/agents/
  epistemic-auditor.md` sigue siendo el único subagente de auditoría
  epistémica del repositorio; este paquete es la infraestructura que ese
  agente usa cuando audita citas (sección "Auditoría de citas" de ese
  archivo), no un segundo agente independiente.
- **No obliga a re-auditar las citas ya integradas.** Las ~184 citas ya
  verificadas en `research/sources/notes/**` siguen siendo válidas para
  su uso actual (evidencia de lectura, respaldo de fichas). El bloque de
  auditoría estructurada es opt-in: se aplica cuando una cita concreta se
  somete a auditoría — típicamente antes de usarse como evidencia
  principal de un `ARG-*`, o antes de integrarse a un capítulo.

## Principios epistémicos (obligatorios)

1. La IA localiza, compara, contextualiza, clasifica y detecta riesgos;
   nunca determina el significado filosófico definitivo de un autor.
2. Ninguna sesión de IA marca `human_verified: true`, `HUMAN_VERIFIED`,
   ni ningún estado que implique decisión humana — ese campo lo escribe
   el investigador.
3. La cita original nunca se modifica para "mejorar redacción"; la
   interpretación vive siempre en una nota separada, nunca fusionada con
   el texto citado.
4. Ante incertidumbre en cualquiera de las ocho preguntas del test de
   integridad contextual (`prompts/01-context-integrity.md`):
   `HUMAN_REVIEW_REQUIRED`.
5. Un vacío inferencial entre la cita y la afirmación que pretende
   respaldar se declara explícitamente (`INFERENTIAL_GAP`); nunca se
   inventa la premisa que falta.
6. Las decisiones de uso final (`APPROVED_FOR_INTERPRETIVE_USE`,
   `APPROVED_FOR_ARGUMENTATIVE_USE`, `APPROVED_FOR_MANUSCRIPT`) son
   exclusivas de Juan Pablo Valderrama Pino. La IA únicamente recomienda
   (`recommended_status`).

## Cómo se invoca hoy

Igual que PLAA, este paquete no es un subagente independiente. Se usa de
dos maneras:

1. **Como paquete Python** (`quote_audit/`) para las tareas deterministas:
   parsear un bloque de auditoría de una ficha, validar que cumple el
   esquema, comprobar la clave BibTeX contra `research/sources/
   bibliography.bib`, aplicar la regla estructural de 40+ palabras de
   APA 7, y bloquear estados que requieren marca humana explícita.
2. **Como conjunto de prompts** (`prompts/*.md`) que el `epistemic-
   auditor` (o el investigador directamente) aplica a una cita concreta
   para producir el juicio de integridad contextual, pertinencia
   filosófica, riesgo de *quote mining* y fuerza argumentativa. La salida
   se valida después con `quote_audit.schema_check` antes de considerarse
   un informe completo.

## Mapa de archivos

```text
ai/quote-audit/
  README.md                 este documento
  ARCHITECTURE.md           capa determinista vs. capa de juicio, módulo por módulo
  CONFIG.yaml               vocabularios admitidos (comparte confidence_vocabulary con PLAA)
  schemas/                  especificación del objeto Quote Audit (YAML + JSON)
  templates/                plantilla Markdown del informe de auditoría
  prompts/                  instrucciones de juicio para sesiones de Claude Code
  quote_audit/               paquete Python (parseo, validación de esquema)
  tests/                    pruebas del paquete Python, con fixtures ficticios
  examples/                 una auditoría de ejemplo sobre citas reales ya verificadas (ARG-001)
```

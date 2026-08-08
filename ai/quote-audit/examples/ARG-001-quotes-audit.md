# Ejemplo — Auditoría de las 3 citas de evidencia de ARG-001

> Demostración de punta a punta de Quote Audit sobre citas **reales, ya
> verificadas** del corpus (no ficticias, a diferencia de
> `ai/plaa/examples/example-analysis-report.md`, porque aquí ya existe
> material real que auditar: `research/argument-ledger/ARG-001.md`). No
> modifica `ARG-001.md` ni las fichas de fuente — es un archivo aparte.
> Los tres registros son estructuralmente válidos contra
> `quote_audit.schema_check.validate_quote_audit_record` (ver
> `../tests/`), pero el juicio filosófico (`context_status`,
> `philosophical_function`, `relevance_status`, `argumentative_support`,
> `classification`) es `AI_ASSISTED_JUDGMENT` de esta sesión, **no
> revisado todavía por el investigador** — por eso ninguno alcanza
> `recommended_status: READY_FOR_ARGUMENT_USE` (eso exigiría
> `human_verified: true` explícito, que solo el investigador puede
> poner).

## Cita 1 — "yo puedo" ilimitado (La bestia y el soberano, p. 306/352)

```yaml
quote_id: derrida-2010-bestia-soberano-1#c7
source: derrida-2010-bestia-soberano-1
locator: "p. 306, retomado p. 352"
recommended_status: RELEVANCE_AUDITED
context_status: SELF_CONTAINED
philosophical_function: DEFINITION
relevance_status: HIGH
related_PI: [PI-02, PI-07]
related_ARG: [ARG-001]
primary_evidence: true
argumentative_support: DIRECT_SUPPORT
apa7:
  compliant: true
  quote_type: short
  locator_present: true
  bibliography_entry_found: true
  issues: []
risks: []
confidence: LIKELY
human_review_required: false
human_verified: false
classification: VERIFIED_RELEVANT
reasoning_summary: >
  Definición explícita y autónoma de la soberanía como potencia sin
  límite; no depende de una condición o negación cercana que la matice
  (repetida idéntica en p. 352), por eso SELF_CONTAINED. Respalda
  directamente la premisa 1 de ARG-001.
```

## Cita 2 — "no puedo, por tanto debo" (Hospitality, p. 232)

```yaml
quote_id: derrida-2023-hospitality#c56
source: derrida-2023-hospitality
locator: "p. 232"
recommended_status: RELEVANCE_AUDITED
context_status: CONTEXT_REQUIRED
philosophical_function: ARGUMENT_PREMISE
relevance_status: HIGH
related_PI: [PI-01, PI-07]
related_ARG: [ARG-001]
primary_evidence: true
argumentative_support: DIRECT_SUPPORT
apa7:
  compliant: true
  quote_type: short
  locator_present: true
  bibliography_entry_found: true
  issues: []
risks: []
confidence: LIKELY
human_review_required: false
human_verified: false
classification: VERIFIED_RELEVANT
reasoning_summary: >
  CONTEXT_REQUIRED, no SELF_CONTAINED: es nota de sesión oral ("no
  declaration of generous hospitality will be able to deny this fact...")
  y su fuerza depende de leerla junto con la constatación de límite que
  la sigue ("if one wanted to receive everyone, one would receive no
  one"), ya presente en la misma ficha (cita 57) pero no reproducida
  dentro de este fragmento. Respalda directamente la premisa 2 de
  ARG-001.
```

## Cita 3 — "a possibility without power" (The Animal That Therefore I Am, p. 27)

```yaml
quote_id: derrida-2008-animal#c-bentham-27
source: derrida-2008-animal
locator: "p. 27"
recommended_status: RELEVANCE_AUDITED
context_status: CONTEXT_CRITICAL
philosophical_function: ARGUMENT_PREMISE
relevance_status: MEDIUM
related_PI: [PI-04, PI-07]
related_ARG: [ARG-001]
primary_evidence: true
argumentative_support: PARTIAL_SUPPORT
apa7:
  compliant: true
  quote_type: short
  locator_present: true
  bibliography_entry_found: true
  issues: []
risks: []
confidence: POSSIBLE
human_review_required: true
human_verified: false
classification: VERIFIED_CONTEXT_NEEDED
reasoning_summary: >
  CONTEXT_CRITICAL: la frase describe una estructura pasiva (poder
  sufrir como no-poder) mientras que la premisa 2 de ARG-001 usa una
  estructura activa (el anfitrión que no puede recibir a todos) — la
  propia ficha de ARG-001, sección "Interpretaciones alternativas",
  ya registra esta tensión ("son categorías gramaticalmente distintas
  ... que podrían no ser homologables sin trabajo conceptual
  adicional"). Por eso PARTIAL_SUPPORT y relevance MEDIUM, no HIGH:
  la cita respalda el patrón general pero no sostiene por sí sola el
  paso de "posibilidad sin poder" a "no puedo, por tanto debo" sin la
  homologación que ARG-001 mismo señala como no demostrada
  (INFERENTIAL_GAP ya declarado en esa ficha, sección "Inferencia").
```

## Lectura del resultado

Ninguna de las tres citas es rechazada, pero solo la primera resulta
`SELF_CONTAINED` con soporte `DIRECT_SUPPORT` sin reservas. La tercera es
la más débil de las tres — no porque sea inauténtica o esté mal
localizada, sino porque la homología gramatical entre "posibilidad sin
poder" y "no puedo, por tanto debo" es precisamente el paso que
`ARG-001.md` ya señala como no demostrado. Esto confirma, con
herramientas distintas, la misma cautela que `ARG-001.md` ya se impuso a
sí mismo — es la clase de resultado que este componente debería producir:
ni inflar la evidencia disponible ni descartarla, solo mostrar dónde es
fuerte y dónde necesita más trabajo.

---
description: Reglas para fuentes primarias, fichas y biblioteca
paths:
  - "research/sources/**"
  - "library/**"
---

# Reglas para fuentes (`research/sources/**`, `library/**`)

- No completes metadatos bibliográficos de forma especulativa. Un campo sin
  verificar se marca `PENDIENTE` o se deja vacío; nunca se rellena por
  plausibilidad.
- El OCR y las transcripciones no son autoritativos. No constituyen
  evidencia por sí mismos y no acreditan que la obra fue leída; deben
  cotejarse contra la edición original antes de citarse.
- Preserva siempre la procedencia de edición y página (localizador exacto)
  al registrar una cita. Una cita sin localizador no se considera
  verificada.
- Los originales protegidos por derechos de autor permanecen fuera del
  repositorio público salvo autorización legal explícita; no los versiones
  ni los transcribas íntegros en Markdown.
- Excepción única y explícita: el propio trabajo previo depositado del
  investigador (`PREVIOUS_RESEARCH_BY_AUTHOR`, tesis de maestría y trabajo
  de grado) puede versionarse en PDF bajo `research/background/**/originals/`,
  porque el investigador es su autor y depositante, no un tercero — no
  constituye precedente para versionar ninguna otra edición protegida.
  `scripts/auditar_repositorio.py` (`ALLOWED_SELF_AUTHORED_PDFS`) permite
  únicamente esas dos rutas por nombre exacto, no una excepción genérica de
  extensión `.pdf` (véase `governance/decision-log.md`, DEC-012).
- No recrees fichas o registros para obras que el investigador aún no ha
  incorporado realmente al corpus, incluso si una rama histórica del
  repositorio las propuso.

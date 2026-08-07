---
description: Reglas para el material de investigación (preguntas, fuentes, argumentos)
paths:
  - "research/**"
---

# Reglas para `research/**`

- Preserva la procedencia `PI-*` → fuente → `ARG-*`. Todo argumento nuevo o
  editado debe seguir enlazando preguntas y fuentes reales, no inventadas.
- Distingue explícitamente evidencia textual (cita cotejada) de
  interpretación del investigador. No fusiones ambas categorías en la misma
  frase sin marcarlo.
- Preserva la incertidumbre declarada: si una ficha dice `PENDIENTE`, `idea`
  o señala un límite, no lo completes por conjetura ni lo borres para que el
  documento «se vea» más avanzado.
- Nunca cambies `human_validation` ni el estado epistémico de un argumento a
  `VALIDATED` de forma autónoma. Ese cambio pertenece solo al investigador.
- No crees fichas de fuente especulativas para obras que el investigador no
  ha incorporado realmente al corpus (véase `research/sources/**`, regido
  además por `.claude/rules/sources.md`).
- Usa las plantillas existentes (`templates/ficha-fuente.md`,
  `templates/ficha-argumento.md`) en vez de formatos ad hoc.

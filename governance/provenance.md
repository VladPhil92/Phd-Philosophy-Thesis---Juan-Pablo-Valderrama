# Convención mínima viable de procedencia epistémica

Este documento define la cadena de identificadores que permite reconstruir
cómo una afirmación del manuscrito llegó a existir. No introduce una base de
datos ni un sistema paralelo: reutiliza los identificadores ya definidos en
`governance/architecture.md` y los extiende solo donde faltaba una pieza de
la cadena. Declarado como parte de **Research Environment v1.0**
(`governance/decision-log.md`, DEC-003).

## La cadena

```text
PI  →  SRC  →  NOTE  →  QUOTE  →  ARG  →  OBJ  →  AI  →  REV  →  CHAPTER
```

| Eslabón | Identificador | Dónde vive | Estado actual |
|---|---|---|---|
| Pregunta de investigación | `PI-*` | `research/questions.md` | Implementado (PI-01…PI-07) |
| Fuente | clave BibTeX `apellido-anio-palabra` (`SRC` conceptual) | `research/sources/bibliography.bib` | Implementado, catálogo vacío |
| Ficha de fuente / nota de lectura | nombre de archivo = clave BibTeX | `research/sources/notes/` (`templates/ficha-fuente.md`) | Implementado, sin fichas aún |
| Cita verificada | sección «Citas verificadas» dentro de la ficha de fuente, con localizador | `research/sources/notes/<clave>.md` | Implementado como sección, no como ID propio |
| Argumento | `ARG-*` | `research/argument-ledger/` (`templates/ficha-argumento.md`) | Implementado, sin fichas aún |
| Objeción | subsección «Objeciones y respuestas» dentro del `ARG-*` | `research/argument-ledger/<ARG>.md` | Implementado como sección, no como ID propio |
| Intervención de IA | `IA-AAAA-MM-DD-NN` | `ai/` (`templates/registro-ia.md`) | Implementado, sin registros aún |
| Revisión | referencia de commit de Git + entrada en `thesis/review/` | `thesis/review/` | Implementado de forma ligera (checklist), sin ID propio |
| Capítulo | ruta en `thesis/chapters/` (p. ej. `01-introduccion.md`) | `thesis/chapters/` | Implementado, sin capítulos aún |

No se crean identificadores nuevos para `QUOTE`, `OBJ` y `REV` como
archivos separados: dado el volumen actual de investigación (cero fuentes,
cero argumentos), representarlos como secciones dentro de la ficha de fuente
o de argumento es suficiente y evita una base de datos prematura (véase la
sección «Cuándo reconsiderar» más abajo).

## Cómo se enlazan los eslabones

- Una ficha de fuente (`research/sources/notes/<clave>.md`) declara qué
  `PI-*` le son pertinentes en su sección «Relación con preguntas y
  argumentos».
- Una ficha de argumento (`research/argument-ledger/ARG-*.md`) declara, en su
  cabecera, al menos una `PI-*` y una o más claves BibTeX de
  `research/sources/bibliography.bib`.
- Una ficha de argumento declara, si corresponde, el identificador `IA-*` de
  toda intervención de IA que haya influido materialmente en su contenido, y
  el estado de esa intervención (`ACEPTADA`, `MODIFICADA`, `RECHAZADA`,
  `SOLO_EXPLORATORIA` — véase `templates/registro-ia.md`).
- Un capítulo en `thesis/chapters/` integra únicamente `ARG-*` cuyo estado
  epistémico sea `READY_FOR_HUMAN_REVIEW` o posterior; nunca integra un
  argumento en estado `IDEA` o `DEVELOPING`.
- `research/argument-map.md` documenta las relaciones *entre* argumentos
  (`supports`, `depends-on`, `objects-to`, `revises`, `contradicts`,
  `distinguishes`, `applies-to`), separadas de las relaciones argumento↔fuente
  y argumento↔pregunta que ya viven dentro de cada ficha.

## Preguntas que la cadena debe permitir responder

- ¿Qué fuente respalda este argumento? → sección «Fuentes» del `ARG-*`.
- ¿Qué argumentos dependen de esta fuente? → búsqueda de la clave BibTeX en
  `research/argument-ledger/**`.
- ¿Qué pregunta de investigación aborda este argumento? → campo «Preguntas
  relacionadas» del `ARG-*`.
- ¿Qué intervención de IA afectó a este argumento? → campo «Uso de IA» del
  `ARG-*`, enlazado al `IA-*` correspondiente.
- ¿Esa salida de IA fue aceptada, modificada o rechazada? → decisión humana
  registrada en el `IA-*` referenciado.
- ¿Fue validado el argumento por el investigador? → campo
  `human_validation` en la cabecera del `ARG-*`.
- ¿Dónde aparece en el manuscrito? → campo «Capítulo de destino» del `ARG-*`.

## Regla de autoridad

Ningún script, agente o sesión de Claude Code puede escribir
`human_validation: validated` ni un estado epistémico `VALIDATED` de forma
autónoma. Ese cambio requiere instrucción explícita del investigador en la
propia sesión donde se aplica (véase `CLAUDE.md`).

## Cuándo reconsiderar esta convención

Esta convención deliberadamente no usa una base de datos, un grafo formal ni
identificadores de archivo independientes para citas, objeciones o
revisiones. Reconsidérese solo cuando exista evidencia real de necesidad,
por ejemplo: decenas de `ARG-*` con objeciones cruzadas difíciles de
rastrear en Markdown plano, o la necesidad recurrente de citar la misma
`QUOTE` desde múltiples argumentos. Hasta entonces, Markdown, BibTeX,
frontmatter YAML ligero y Git bastan.

## Investigación previa del autor

Los artefactos `PREVIOUS_RESEARCH_BY_AUTHOR` usan `SRC-PR-*` en el manifiesto y
una clave BibTeX canónica, pero permanecen fuera del corpus doctoral. Sus
análisis viven únicamente en `research/background/`; una autocita puede probar
cronología autoral, no una afirmación filosófica. La integración de la tesis de
grado de 2015 (`SRC-PR-002`) fue asistida por IA y está registrada en
[`ai/IA-2026-08-10-03.md`](../ai/IA-2026-08-10-03.md). El PDF original ya está
archivado y su integridad binaria fue verificada; esto cierra la procedencia
documental, pero no promueve automáticamente los pasajes históricos al
`quote-ledger`. Cada candidato conserva `SOURCE_RECHECK_REQUIRED` hasta que sea
cotejado textual y contextualmente por el investigador.
## Genealogía intelectual del asesor de grado

La operación `INTELLECTUAL_GENEALOGY_RESEARCH` sobre Kenneth Moreno May está
registrada en [`IA-2026-08-10-04`](../ai/IA-2026-08-10-04.md). Sus actividades
fueron recuperación bibliográfica, reconstrucción cronológica, clasificación de
fuentes, comparación conceptual, auditoría de influencia y reconstrucción de
contexto. Los registros `SRC-201`–`SRC-209` permanecen candidatos; la
interpretación requiere revisión humana. En esta cadena, supervisión e
influencia reconocida no autorizan inferir dependencia ni origen conceptual.

## Dossier público del investigador

La investigación y organización del dossier público de identidad académica se
documenta en
[`ai/IA-2026-08-10-04.md`](../ai/IA-2026-08-10-04.md). Su resultado canónico es
[`RESEARCHER.md`](../RESEARCHER.md), permanece `HUMAN_REVIEW_REQUIRED` y no
modifica la procedencia archivística de los trabajos previos ni crea un sistema
paralelo.

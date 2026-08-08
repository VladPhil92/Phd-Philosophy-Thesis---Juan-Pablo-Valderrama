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
| Cita verificada | sección «Citas verificadas» dentro de la ficha de fuente, con localizador; opcionalmente, un `quote_id` propio (`clave-bibtex#cNN`) cuando la cita se somete a auditoría (véase `ai/quote-audit/`) | `research/sources/notes/<clave>.md`, sección opcional «Auditoría de citas» | Implementado como sección; `quote_id` es un identificador opcional para citas auditadas, no obligatorio para toda cita |
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

**Nota (2026-08-08):** el segundo disparador citado arriba —auditar la
misma cita con criterios de relevancia/contexto/soporte argumentativo,
potencialmente reutilizables desde más de un `ARG-*`— ya ocurrió, y se
resolvió de la forma más pequeña posible: un `quote_id` **opcional**
dentro de la misma ficha de fuente (`ai/quote-audit/`, sin archivo
independiente por cita, sin base de datos). No es una reconsideración de
la convención, es la extensión mínima que la propia convención preveía;
si en el futuro se necesita más que eso, aplica el mismo criterio de esta
sección antes de construirlo.

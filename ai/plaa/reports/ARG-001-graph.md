# PLAA — Módulo 2: Argument Graph — ARG-001

**Fuente auditada:** `research/argument-ledger/ARG-001.md`
**Comparado contra:** `research/argument-map.md` y el catálogo completo de
`research/argument-ledger/` (verificado con `ls`: solo existen
`ARG-001.md` y `README.md` en ese directorio).
**Método:** ejecución determinista de `plaa.graph.build_graph` sobre el
único documento minado (`ARG-001`) y el contenido íntegro de
`research/argument-map.md`.

> Este informe no es un informe de juicio (no requiere frontmatter YAML
> del esquema `analysis-report`, según indica el prompt del módulo 2).

## Resultado determinista

`research/argument-map.md` declara explícitamente: «Estado: idea — el
catálogo de argumentos está vacío» y su tabla de relaciones contiene
únicamente la fila placeholder `| — | — | — | Sin argumentos registrados
todavía. |`. La función `parse_argument_map_relations` descarta esa fila
(fuente `—`) y la sección "Ejemplo (ficticio...)" ya se declara a sí misma
como no correspondiente a fichas reales, de modo que no aporta ninguna
arista real.

El grafo construido contiene:

- **Nodos:** `ARG-001` (nodo de argumento) y sus siete nodos internos
  minados por el módulo 1 (`CLAIM`, 4×`PREMISE`, `OBJECTION` agregado,
  `DISTINCTION` agregado — ver `ARG-001-miner.md` para la segmentación
  fina de estos dos últimos).
- **Aristas:** únicamente `contains` (`ARG-001 → ARG-001:<nodo>`), es
  decir, relaciones de composición interna del propio `ARG-001`, no
  relaciones `ARG-* ↔ ARG-*`.
- **Ninguna arista `supports` / `depends-on` / `objects-to` / `revises` /
  `contradicts` / `distinguishes` / `applies-to` entre `ARG-001` y otro
  `ARG-*`**, porque no existe ningún otro `ARG-*` en el repositorio contra
  el cual declarar una relación.

## Relaciones propuestas (Módulo 2, juicio)

**Ninguna.** Tal como anticipa la instrucción de la tarea, `ARG-001` es el
único argumento real del repositorio (`research/argument-ledger/` no
contiene ningún otro `ARG-*.md`). Este módulo solo puede *proponer* una
relación entre dos `ARG-*` ya existentes, citando texto concreto de
ambos extremos (`02-argument-graph.md`, instrucción 1); al no existir un
segundo extremo, no hay ninguna relación que pueda justificarse con esa
evidencia. No se fuerza ninguna relación con una nota de fuente
(`derrida-2010-bestia-soberano-1`, `derrida-2023-hospitality`,
`derrida-2008-animal`) ni con una pregunta de investigación (`PI-*`):
esas relaciones ya viven en la cabecera de `ARG-001.md` y en las propias
fichas de fuente, y el prompt del módulo 2 (instrucción 3) indica
explícitamente que no se duplican en este grafo.

## Nota sobre candidatos futuros mencionados en el propio ARG-001

La sección "Alcance y límites" de `ARG-001.md` señala dos candidatos a
`ARG-*` futuros y distintos (la homología bestia/soberano de
`derrida-2010-bestia-soberano-1.md`, y la distinción dominio/nombrar de
`derrida-2008-animal.md`), declarando expresamente que «no deben
fusionarse sin justificación explícita» con `ARG-001`. Esto **no** es una
relación entre dos `ARG-*` existentes — son candidatos que todavía no
tienen ficha propia — por lo que tampoco se registra como arista del
grafo. Se deja constancia aquí únicamente como nota de contexto para
cuando esas fichas existan.

## Confianza y trazabilidad

**Confianza:** `NOT_DETECTED` (no se detecta ninguna relación grafo↔grafo
que pueda proponerse, con vocabulario del Principio 3).
**Repository references:** `research/argument-ledger/ARG-001.md`,
`research/argument-map.md`, `research/argument-ledger/` (listado de
directorio, verificado en esta sesión).

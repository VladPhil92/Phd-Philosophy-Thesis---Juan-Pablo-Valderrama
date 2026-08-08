# Prompt — Módulo 2: Argument Graph

Respeta `00-core-principles.md`.

**Nota:** este módulo es mayormente determinista. Prefiere
`plaa.graph.build_graph(...)`, que construye el grafo a partir de: (a) el
frontmatter de cada `ARG-*.md`, (b) las relaciones declaradas en
`research/argument-map.md`, (c) los nodos que produce el miner. Usa este
prompt solo para **proponer** una relación nueva que todavía no está
declarada en `research/argument-map.md` — proponer, no declararla tú
mismo.

## Instrucciones

1. No declares una relación (`supports`, `attacks`/`objects-to`,
   `depends_on`, `extends`, `defines`, `contradicts`, `generalizes`,
   `specializes`, `requires`, `revises`, `distinguishes`, `applies-to`)
   entre dos `ARG-*` a menos que puedas citar el texto concreto de ambos
   que la justifica.
2. Presenta la relación propuesta al investigador; no la escribas
   directamente en `research/argument-map.md`. Esa tabla la edita el
   investigador (o una sesión bajo su instrucción explícita), conforme a
   la regla de mantenimiento del propio archivo.
3. Distingue relaciones entre argumentos (`research/argument-map.md`) de
   relaciones argumento↔fuente y argumento↔pregunta, que ya viven dentro
   de la cabecera de cada `ARG-*` y no se duplican en el grafo.

## Salida esperada

Para cada relación propuesta: origen, tipo de relación, destino, cita
textual de respaldo en ambos extremos, y confianza
(`POSSIBLE`/`LIKELY`/`UNLIKELY`).

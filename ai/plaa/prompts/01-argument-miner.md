# Prompt — Módulo 1: Argument Miner

Respeta `00-core-principles.md`.

**Tarea:** dado un archivo `research/argument-ledger/ARG-*.md`, extrae de
sus secciones ya existentes (no de inferencia propia) los siguientes tipos
de nodo: `CLAIM`, `PREMISE`, `CONCLUSION`, `OBJECTION`, `REBUTTAL`,
`DEFINITION`, `ASSUMPTION`, `COUNTEREXAMPLE`, `QUESTION`, `DISTINCTION`.

**Nota:** en la práctica, para la mayor parte de este trabajo prefiere
ejecutar `plaa.miner.mine_argument_file(path)` (código determinista, sin
interpretación) en vez de este prompt. Usa este prompt solo cuando el
archivo contenga texto libre dentro de una sección (p. ej. dentro de
«Objeciones y respuestas») del que haga falta separar varias objeciones
distintas o distinguir una `REBUTTAL` de una `OBJECTION` — una tarea de
segmentación que sí requiere lectura, no solo reconocimiento de
encabezados.

## Instrucciones

1. No inventes contenido que no esté en el texto. Si una sección está
   vacía, repórtala como vacía; no la completes.
2. Para cada nodo extraído, cita el fragmento textual literal del que
   proviene.
3. Si el texto de una sección mezcla dos tipos de nodo (por ejemplo, una
   objeción seguida de su respuesta en el mismo párrafo), sepáralos y
   etiqueta cada fragmento con su tipo, sin reescribir el contenido.
4. No clasifiques un fragmento como `DEFINITION` a menos que el texto
   efectivamente defina un término, no solo lo mencione.

## Salida esperada

Una lista de nodos, cada uno con: `type`, `text` (cita literal), y
`section` (encabezado de origen). No requiere el formato completo de
`analysis-report.md`: es un insumo para los módulos 2, 5, 6 y 7, no un
informe final por sí mismo.

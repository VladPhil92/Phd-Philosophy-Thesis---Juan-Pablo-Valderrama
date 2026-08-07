# Hoja de ruta de PLAA

Ordenada por cuándo tendría sentido cada paso, no por preferencia técnica.
Ningún paso se ejecuta solo porque es técnicamente posible: cada uno
requiere que exista la necesidad de investigación real que lo motive.

## Ahora (Research Environment v1.0)

- Infraestructura del paquete, esquemas, plantillas y prompts (este
  commit). Cero argumentos reales auditados: no puede haberlos, porque
  `research/argument-ledger/` todavía no contiene fichas sustantivas.

## Cuando exista el primer `ARG-*` real con contenido sustantivo

- Ejecutar manualmente los módulos 1 (miner) y 2 (graph) sobre él para
  confirmar que el mapeo de encabezados en español sigue siendo correcto
  frente a texto filosófico real, no solo frente al fixture ficticio de
  `tests/`.
- Ejecutar el prompt del módulo 5 (falacias) y el módulo 7 (stress test)
  sobre ese primer argumento y evaluar si el formato de salida es
  realmente útil para el investigador o necesita ajuste.

## Cuando existan 5-10 argumentos con relaciones declaradas

- Revisar si `research/argument-map.md` en Markdown plano sigue siendo
  suficiente o si conviene una exportación a Graphviz DOT (ya soportada de
  forma opcional por `plaa/graph.py`) para inspección visual. Esto no
  requiere una base de datos ni un servicio nuevo.

## Cuando el investigador decida trabajar con formalización lógica seria

- Decidir, con el investigador, si vale la pena integrar un motor
  simbólico real (Z3 es la opción más accesible para lógica proposicional
  y de primer orden desde Python) implementando
  `LogicalValidatorEngine`. Esto añade una dependencia externa real y debe
  documentarse en `governance/decision-log.md` antes de implementarse, no
  después.
- Hasta entonces, el módulo 4 permanece deliberadamente incompleto
  (`NullValidatorEngine`), y eso es preferible a fingir una validación
  simbólica con heurísticas de texto.

## Cuando el volumen de auditorías lo justifique

- Evaluar si PLAA merece convertirse en su propio subagente
  (`.claude/agents/plaa-auditor.md`), separado de `epistemic-auditor`. No
  antes: `governance/decision-log.md` (DEC-003) fija deliberadamente un
  único subagente mientras el repositorio no tiene material sustantivo
  que justifique más superficie de configuración.
- Evaluar si conviene añadir un job de CI que ejecute
  `python3 -m unittest discover -s ai/plaa/tests` en cada push. Hoy no
  existe ese job: añadirlo es una decisión de infraestructura menor pero
  real, y debe confirmarse explícitamente, no darse por hecho.

## Explícitamente fuera de alcance por ahora

- Neo4j, PostgreSQL, bases de datos vectoriales, APIs, dashboards o
  aplicaciones web para visualizar el grafo argumental.
- Cualquier intento de que PLAA determine si un argumento es
  filosóficamente correcto, más allá de reportar problemas de forma con
  confianza declarada.
- Detección de falacias o consistencia conceptual mediante heurísticas de
  texto (regex, listas de palabras clave) presentadas como análisis
  semántico. Si algún día se automatiza parcialmente, debe seguir
  declarando confianza baja y marcarse explícitamente como heurística.

# Guía de desarrollo de PLAA

Para quien extienda el paquete `ai/plaa/plaa/`, no para el investigador
(véase [`USER-GUIDE.md`](USER-GUIDE.md) para eso).

## Requisitos

Solo biblioteca estándar de Python ≥ 3.10. Sin `requirements.txt`: si en
el futuro un módulo necesita una dependencia real (por ejemplo, un binding
a Z3), documenta la justificación en `ROADMAP.md` y en
`governance/decision-log.md` antes de añadirla, conforme a la regla de
arquitectura de `CLAUDE.md`.

## Estructura del paquete

```text
plaa/
  __init__.py               versión y exports públicos
  miner.py                  extracción determinista de secciones de un ARG-*.md
  graph.py                  construcción de grafo a partir de fichas y argument-map.md
  fallacy_checklist.py      catálogo cerrado de falacias y vocabulario de confianza
  validator_interfaces.py   contrato para motores simbólicos futuros + NullValidatorEngine
  schema_check.py           validación estructural de frontmatter y de informes de análisis
  report.py                 dataclass AnalysisReport + render a Markdown + validación de esquema
```

## Reglas de contribución específicas de este paquete

1. **Ningún módulo de "juicio" (formalización, falacias, stress test,
   consistencia conceptual) se implementa con heurísticas de texto
   (regex, listas de palabras clave, similitud superficial) haciéndolas
   pasar por análisis lógico o filosófico.** Si una tarea requiere
   comprensión semántica, su lugar es un archivo en `prompts/`, no una
   función en `plaa/`. La única excepción es una heurística
   explícitamente etiquetada como tal y con confianza `UNKNOWN` forzada.
2. **Todo dataclass público lleva un docstring de una línea**, no un bloque
   de documentación — el resto vive en este archivo o en
   `ARCHITECTURE.md`.
3. **Ninguna función de `plaa/*.py` escribe en `research/` ni en
   `thesis/`.** El paquete lee fichas existentes y produce estructuras de
   datos u objetos `AnalysisReport`; quien decide guardar el informe en el
   repositorio es el investigador, no el paquete.
4. **Ninguna función marca `human_validation: validated` ni un estado
   `VALIDATED`.** Esa restricción de `templates/ficha-argumento.md` aplica
   también aquí.
5. Nombres descriptivos en inglés para símbolos de código (consistente con
   el resto de identificadores técnicos del repositorio, p. ej. `ARG-*`,
   `IA-AAAA-MM-DD-NN`); prosa de documentación en español, consistente con
   el resto del repositorio.

## Cómo ejecutar las pruebas

Sin dependencias adicionales:

```bash
python3 -m unittest discover -s ai/plaa/tests -p "test_*.py" -v
```

No se ha añadido un job de CI para estas pruebas (véase `ROADMAP.md`): es
una decisión de infraestructura que corresponde confirmar junto con el
investigador antes de modificar `.github/workflows/`.

## Cómo añadir un nuevo tipo de nodo al Argument Miner

1. Añade el encabezado en español que ya usa `templates/ficha-argumento.md`
   (o uno nuevo, si el investigador amplía la plantilla) al diccionario
   `SECTION_HEADINGS` en `miner.py`.
2. Asocia ese encabezado a uno de los tipos canónicos ya definidos en
   `NodeType` (`CLAIM`, `PREMISE`, `CONCLUSION`, `OBJECTION`, `REBUTTAL`,
   `DEFINITION`, `ASSUMPTION`, `COUNTEREXAMPLE`, `QUESTION`,
   `DISTINCTION`). No crees un tipo nuevo sin actualizar también
   `schemas/argument.schema.yaml`.
3. Añade un caso de prueba en `tests/test_miner.py` usando el fixture
   ficticio existente o uno nuevo, siempre marcado explícitamente como
   ficticio.

## Cómo añadir un motor de validación simbólica real

1. Implementa el protocolo `LogicalValidatorEngine` de
   `validator_interfaces.py` en un módulo nuevo (por ejemplo,
   `plaa/engines/z3_engine.py`).
2. No modifiques `report.py` ni `schema_check.py`: deben seguir
   funcionando con cualquier implementación del protocolo, incluida
   `NullValidatorEngine`.
3. Documenta la dependencia externa añadida, su justificación y su
   instalación en `ROADMAP.md` y en una entrada nueva de
   `governance/decision-log.md`, conforme a la regla de arquitectura del
   repositorio.

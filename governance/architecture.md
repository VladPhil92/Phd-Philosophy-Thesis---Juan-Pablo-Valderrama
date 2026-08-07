# Arquitectura del repositorio

## Objetivo

La arquitectura separa el material por función epistémica para reconstruir cómo
una afirmación del manuscrito se relaciona con una pregunta, una fuente y una
decisión analítica.

## Capas y dependencias

1. **`governance/`** define reglas transversales, auditorías y decisiones.
2. **`research/`** reúne preguntas, método, fuentes y análisis. Su
   `argument-ledger/` conecta esos elementos mediante argumentos identificables.
3. **`thesis/`** integra los argumentos en el esquema, capítulos y revisión; no
   duplica metadatos bibliográficos.
4. **`ai/`** conserva política y registros del apoyo automatizado; no contiene
   evidencia de la tesis.
5. **`templates/`**, `assets/` y `scripts/` proporcionan formatos, recursos
   autorizados y validaciones.

El flujo normal va de `research/` a `thesis/`; gobernanza y controles son
transversales. `library/` y `tools/library/output/` son espacios locales
ignorados para originales privados y derivados, no capas de evidencia
versionada.

## Unidad de trazabilidad

Se emplean identificadores estables: preguntas `PI-*`, argumentos `ARG-*`, usos
de IA `IA-AAAA-MM-DD-NN` y claves BibTeX `apellido-anio-palabra`. Una ficha de
argumento enlaza al menos una pregunta y enumera fuentes verificadas; un capítulo
remite a argumentos. Los cambios de ruta actualizan enlaces, no identificadores.

## Estados documentales

Todo documento sustantivo indica `idea`, `en desarrollo`, `en revisión` o
`aprobado`. La aprobación significa revisión humana, no verdad definitiva. Las
incertidumbres se conservan explícitas.

## Cambios de arquitectura

Una modificación requiere motivación, impacto en trazabilidad, plan de migración
y entrada en `decision-log.md`. La automatización valida invariantes, pero la
calidad filosófica permanece bajo revisión humana.

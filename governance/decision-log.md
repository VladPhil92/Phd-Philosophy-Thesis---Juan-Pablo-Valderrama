# Registro de decisiones

Cada entrada registra únicamente decisiones metodológicas o arquitectónicas con
efectos duraderos; este archivo no es un diario. La forma mínima es: ID, fecha,
problema, alternativas consideradas, decisión y razón, consecuencias y estado.

## DEC-006 — Canonicalización final e Infrastructure Freeze

- **Fecha:** 2026-08-10
- **Problema:** el mapa de candidatos competía parcialmente con el catálogo
  bibliográfico; las citas y los conceptos carecían de un índice transversal;
  y la procedencia aún describía las citas solo como secciones sin ID.
- **Alternativas consideradas:** conservar el doble registro; crear una base de
  datos o una carpeta por entidad; o consolidar los registros mínimos en
  Markdown y mantener BibTeX exclusivamente como formato de citación.
- **Decisión y razón:** adoptar un solo `library-manifest.md` para identidad,
  clasificación y progreso de cada obra; un `concept-registry.md` y un
  `quote-ledger.md` como índices ligeros; mantener preguntas, argumentos,
  decisiones, antecedentes e intervenciones de IA en sus ubicaciones actuales.
  Se elige Markdown para evitar software, profundidad y metadatos paralelos.
- **Consecuencias:** `corpus-map.md` queda sustituido; cada fuente tiene una
  categoría de gobernanza y un flujo de lectura explícitos; las citas adquieren
  IDs reutilizables. `bibliography.bib` conserva solo los registros citables de
  ediciones verificadas y referencia el ID de obra, sin asumir la función de
  inventario. No se crean fichas especulativas ni prosa doctoral.
- **Estado:** aceptada. **READY FOR INFRASTRUCTURE FREEZE**; cualquier cambio
  estructural posterior requiere una necesidad investigativa demostrada y una
  nueva decisión.

## DEC-004 — Refinamiento del título y de la jerarquía conceptual

- **Fecha:** 2026-08-09
- **Estado:** aceptada
- **Contexto:** el título provisional coordinaba dos formulaciones que la
  arquitectura intelectual actual sitúa en niveles distintos.
- **Decisión:** refinar el título de *Soberanía de la hospitalidad y comunidad
  política interespecie* a *Soberanía de la hospitalidad: los límites
  antropológicos de la comunidad política*.
- **Justificación:** el nuevo título refleja mejor la jerarquía de la
  investigación, conserva la centralidad de soberanía y hospitalidad, y sitúa
  la cuestión animal dentro del problema más fundamental de los límites
  antropológicos de la pertenencia política. Así evita presuponer una comunidad
  interespecie como conclusión, sin excluirla como posibilidad pendiente de
  justificación.
- **Consecuencias:** «comunidad política interespecie» deja de ser parte del
  título y se usa solo como categoría exploratoria, horizonte normativo,
  interlocución con teoría política animal, hipótesis derivada o formulación
  por justificar. No se modifican las preguntas canónicas ni la hipótesis
  central.

## DEC-001 — Arquitectura por función epistémica

- **Fecha:** 2026-08-07
- **Estado:** aceptada
- **Contexto:** el repositorio no distinguía fuentes, análisis, escritura y
  controles, lo cual impedía demostrar procedencia.
- **Decisión:** adoptar las seis capas numeradas descritas en `arquitectura.md`
  y conservar recursos auxiliares fuera de ellas.
- **Consecuencias:** las rutas comunican el papel de cada documento; cualquier
  migración futura debe mantener los identificadores y actualizar enlaces.

## DEC-002 — Consolidación en arquitectura semántica

- **Fecha:** 2026-08-07
- **Estado:** aceptada
- **Contexto:** dos arquitecturas paralelas duplicaban gobernanza, investigación,
  escritura y plantillas.
- **Decisión:** adoptar `governance/`, `research/`, `thesis/`, `ai/` y
  `templates/` como rutas canónicas; migrar mediante renombres todos los archivos
  sustantivos de las capas numeradas.
- **Consecuencias:** existe una sola ubicación por función; se actualizaron
  enlaces, auditoría y documentación sin alterar los identificadores.

## DEC-003 — Research Environment v1.0

- **Fecha:** 2026-08-07
- **Estado:** aceptada
- **Contexto:** tras DEC-001 y DEC-002 el repositorio cuenta con una
  arquitectura documental única, auditoría automatizada en verde, política de
  IA, plantillas y trazabilidad `PI-*` → fuente → `ARG-*` → capítulo. Sin
  embargo, cuatro ramas históricas de pull request (#2, #3, #6, #9) seguían
  abiertas contra bases de `main` muy anteriores a DEC-001/DEC-002, proponiendo
  arquitecturas paralelas (directorios numerados `00-gobernanza/…`,
  `library/primary/<autor>/<obra>/` con transcripciones completas
  especulativas de obras aún no incorporadas al corpus, y un README alternativo
  que añade un «doble frente» animal/IA no presente en la formulación vigente
  de la pregunta de investigación). Ninguna de esas ramas es compatible con la
  arquitectura ya consolidada; su contenido sustantivo o ya está en `main` en
  forma más depurada, o es especulativo y no debe recrearse sin fuentes reales,
  o plantea un cambio de alcance de investigación que requiere decisión del
  investigador, no una fusión automática.
- **Decisión:** el repositorio entra en **Research Environment v1.0**. La
  arquitectura documental canónica (`governance/`, `research/`, `thesis/`,
  `ai/`, `templates/`, `assets/`, `scripts/`) se considera estable. Todo cambio
  estructural de nivel superior requiere justificación explícita y una nueva
  entrada en este registro antes de aplicarse. El trabajo prioritario deja de
  ser la construcción de infraestructura y pasa a ser investigación
  sustantiva: ingestión progresiva de fuentes primarias, bibliografía
  verificada, notas de lectura, citas cotejadas, análisis conceptual,
  construcción de argumentos (`ARG-*`), objeciones, revisión argumental y
  desarrollo capitular. El trabajo de infraestructura futuro debe responder a
  una necesidad real de investigación, no a preferencia arquitectónica. Las
  cuatro ramas de PR históricas mencionadas se consideran superadas por esta
  arquitectura y deben cerrarse como tales; ninguna se usa como base de
  migraciones futuras. Su cierre efectivo en GitHub requiere confirmación del
  investigador antes de ejecutarse.
- **Consecuencias:** se añaden `CLAUDE.md`, `.claude/rules/*.md` y
  `.claude/agents/epistemic-auditor.md` como configuración operativa de
  Claude Code alineada con esta arquitectura; se documenta la convención de
  procedencia mínima viable en `governance/provenance.md`; se fortalece
  `templates/ficha-argumento.md` con estado epistémico y validación humana
  explícita; se extiende `scripts/auditar_repositorio.py` con comprobaciones
  de invariantes documentales adicionales. Ningún contenido filosófico nuevo
  se fabricó para poblar estas estructuras.

## DEC-005 — Capa canónica de research lineage

- **Fecha:** 2026-08-10
- **Estado:** aceptada, pendiente de revisión humana sustantiva
- **Contexto:** cuatro notas planas de `research/background/` ofrecían una
  reconstrucción preliminar, pero no separaban ficha, original archivístico,
  argumentos históricos y auditoría, y contenían inferencias incompatibles con
  nuevos datos reportados sobre hospitalidad en 2020.
- **Decisión:** mantener `research/background/` como única capa histórica,
  consolidar un mapa `research-lineage.md` y aislar el dossier en
  `masters-thesis/`. No crear `research/intellectual-history/` ni mezclar el
  antecedente con el corpus o el *argument ledger*.
- **Consecuencias:** toda atribución interna queda pendiente hasta recibir el
  PDF; la posición previa se distingue de la doctoral; el original futuro se
  identifica por hash y se preserva sin corrección; las rutas planas anteriores
  se sustituyen por documentos con una sola función epistémica.

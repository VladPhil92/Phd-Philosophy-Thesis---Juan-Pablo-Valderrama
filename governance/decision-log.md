# Registro de decisiones

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

## DEC-004 — Repository Authority Policy

- **Fecha:** 2026-08-08
- **Estado:** aceptada
- **Contexto:** la autoridad exclusiva del investigador sobre el contenido
  canónico del repositorio estaba implícita y dispersa en `CLAUDE.md`,
  `ai/policy.md` y `CONTRIBUTING.md`, sin un documento único que la
  formalizara como referencia canónica.
- **Decisión:** adoptar `governance/authority-policy.md`, redactada y
  aprobada directamente por Juan Pablo Valderrama Pino (VladPhil92), como
  autoridad exclusiva sobre aprobar, modificar, integrar, rechazar o
  validar cambios en el repositorio de investigación canónico. Terceros
  pueden leer, citar, hacer fork, proponer issues y pull requests, y
  ofrecer crítica académica; no pueden modificar contenido de investigación
  directamente, fusionar cambios, validar argumentos, modificar preguntas
  de investigación, alterar la hipótesis, cambiar decisiones metodológicas
  ni modificar las reglas de gobernanza de IA. Los agentes de IA tienen
  capacidades técnicas delegadas únicamente, sin autoridad propia sobre el
  repositorio ni autoridad académica.
- **Consecuencias:** no se modifica ninguna regla epistémica existente —
  esta autoridad ya se seguía implícitamente de ellas—; se formaliza en un
  solo lugar citable. `CLAUDE.md` y `README.md` enlazan a este documento en
  vez de duplicar su contenido.

## DEC-005 — Master Execution Plan

- **Fecha:** 2026-08-08
- **Estado:** aceptada
- **Contexto:** el repositorio tenía gobernanza, provenance, política de
  IA y metodología documentadas por separado, pero ningún documento único
  respondía qué debe hacerse ahora, en qué orden, bajo qué condiciones y
  qué constituye el cierre de cada etapa del proyecto doctoral completo
  (desde la infraestructura actual hasta el manuscrito).
- **Decisión:** adoptar `MASTER_EXECUTION_PLAN.md` como hoja de ruta
  ejecutiva: seis fases (consolidación y seguridad, metodología,
  biblioteca de investigación, investigación sustantiva, desarrollo
  argumental, manuscrito doctoral), un modelo de madurez de investigación
  de siete niveles (0–6) definido sobre los estados ya existentes de
  fuentes y argumentos, seis puertas de decisión (A–F) que solo el
  investigador puede declarar cruzadas, y una especificación de KPI sin
  automatización nueva. Se añaden cuatro plantillas ejecutivas
  (`templates/checklist-fase.md`, `revision-semanal.md`,
  `revision-mensual.md`, `revision-trimestral.md`). No se crea ninguna
  política, cadena de procedencia o autoridad paralela: el plan enlaza y
  reutiliza `governance/authority-policy.md`, `governance/provenance.md`,
  `CLAUDE.md`, `ai/policy.md` y `research/methodology.md`.
- **Consecuencias:** `scripts/auditar_repositorio.py` añade
  `MASTER_EXECUTION_PLAN.md` y las cuatro plantillas nuevas a
  `REQUIRED_PATHS`. El plan deja explícitamente pendiente, sin resolverla
  de forma autónoma, la decisión sobre proteger técnicamente la rama
  `main` (reglas exactas a confirmar por el investigador). Ningún
  contenido filosófico ni fecha límite se fabricó para poblar el plan.

## DEC-006 — Protección técnica de la rama `main`

- **Fecha:** 2026-08-08
- **Estado:** aceptada
- **Contexto:** `governance/authority-policy.md` (DEC-004) declara que
  terceros no pueden fusionar cambios en el repositorio canónico, pero esa
  autoridad no estaba reforzada técnicamente en la configuración de
  GitHub — solo era una norma documental. `MASTER_EXECUTION_PLAN.md`
  (DEC-005) dejó explícitamente pendiente esta decisión en el checklist de
  cierre de la Fase 1, a la espera de que el investigador eligiera las
  reglas exactas.
- **Decisión:** el investigador aplicó protección de rama sobre `main`
  bloqueando force-push y borrado de la rama (`allow_force_pushes: false`,
  `allow_deletions: false`), sin exigir pull request ni checks de CI antes
  de fusionar (`enforce_admins: false`, sin
  `required_pull_request_reviews` ni `required_status_checks`). Confirmado
  directamente por Juan Pablo Valderrama Pino (VladPhil92) el 2026-08-08.
- **Consecuencias:** el checklist de cierre de la Fase 1 en
  `MASTER_EXECUTION_PLAN.md` queda completo. Nadie puede reescribir el
  historial de `main` ni borrarla por accidente o de forma maliciosa; el
  investigador conserva flujo de trabajo sin fricción (push y merge
  directos siguen permitidos). Esta configuración se aplicó fuera de esta
  sesión (la API de branch protection de GitHub no está disponible entre
  las herramientas de este agente); esta entrada documenta la decisión y
  su justificación, no ejecuta el cambio.

## DEC-007 — Auditoría filosófica de citas (`ai/quote-audit/`)

- **Fecha:** 2026-08-08
- **Estado:** aceptada
- **Contexto:** el investigador pidió explícitamente ampliar
  `epistemic-auditor` para que una cita pudiera auditarse más allá de su
  autenticidad y localizador: integridad contextual, pertinencia
  filosófica, riesgo de extracción engañosa (*quote mining*) y si
  realmente sostiene el argumento al que se asocia — distinguiendo
  siempre `AUTHENTIC QUOTATION ≠ RELEVANT QUOTATION ≠ INTERPRETIVE
  EVIDENCE ≠ ARGUMENTATIVE SUPPORT`. Es un cambio de infraestructura de
  investigación real (no capricho arquitectónico), por lo que requiere
  esta entrada antes de tocar la arquitectura congelada por DEC-003.
- **Decisión:** se creó `ai/quote-audit/`, un paquete hermano de
  `ai/plaa/` que replica su mismo patrón de diseño ya probado —capa
  determinista en Python (`quote_audit/schema_check.py`,
  `quote_audit/parser.py`: campos, vocabulario cerrado, candados de
  estado) separada de capa de juicio en *prompts* (`prompts/*.md`:
  integridad contextual, pertinencia, *quote mining*, soporte
  argumentativo — siempre `AI_ASSISTED_JUDGMENT` sujeto a revisión
  humana). No se crea un segundo subagente de Claude Code:
  `.claude/agents/epistemic-auditor.md` se extiende con una sección
  nueva («Auditoría de citas»); sigue siendo el único punto de auditoría
  epistémica del repositorio. `templates/ficha-fuente.md` gana una
  sección **opcional** «Auditoría de citas» (opt-in, no retroactiva).
  `governance/provenance.md` registra un `quote_id` opcional para citas
  auditadas, sin crear un identificador obligatorio nuevo.
- **Consecuencias:** las ~184 citas ya verificadas en
  `research/sources/notes/**` no se migran ni se modifican — siguen
  siendo válidas para su uso actual sin este bloque adicional. Se
  auditaron, como demostración y sin tocar las fichas reales, las 3
  citas de evidencia de `ARG-001`
  (`ai/quote-audit/examples/ARG-001-quotes-audit.md`): confirmó, con
  herramientas distintas, la misma cautela que `ARG-001.md` ya se había
  impuesto sobre su cita más débil. `scripts/auditar_repositorio.py` no
  se modifica (misma separación de responsabilidades que ya existe entre
  ese script y `ai/plaa/`, que tampoco está enganchado ahí). Tests:
  `python3 -m unittest discover -s ai/quote-audit/tests -p "test_*.py"`
  → 27/27.

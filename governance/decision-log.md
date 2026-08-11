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
- **Consecuencias:** las ~194 citas ya verificadas en
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

## DEC-008 — Integridad de autoría del manuscrito (Fase A)

- **Fecha:** 2026-08-08
- **Estado:** aceptada (parcial — ver «Consecuencias»)
- **Contexto:** el investigador propuso reencuadrar `epistemic-auditor`
  como auditor de tres dominios (Evidence / Argument / Authorship
  Integrity), con el principio explícito de exigir evidencia positiva de
  autoría humana en vez de detectores probabilísticos de IA. La propuesta
  completa incluía además herramientas de comparación textual contra el
  corpus (*Source Appropriation Audit*) y generación automática de
  *Authorship Evidence Bundle* por capítulo.
- **Decisión:** se acepta y se implementa únicamente la capa de
  principios y convenciones ("Fase A"), sin infraestructura de código
  nueva: dos principios en `ai/policy.md` (*Human Manuscript Principle*,
  *Positive Authorship Evidence Principle*), una matriz de operaciones
  permitidas a la IA, el "Modelo de procedencia de escritura" (`OUTLINE →
  HUMAN_DRAFT → ... → MANUSCRIPT_READY`, con `AI_GENERATED_FINAL` y
  `AI_DRAFT_TO_FINAL` explícitamente prohibidos) en
  `governance/provenance.md`, y una tercera sección de criterios en
  `.claude/agents/epistemic-auditor.md` ("Auditoría de autoría"). No se
  cambia el nombre de archivo del subagente ni se crea uno segundo.
- **Consecuencias:** se **difiere explícitamente** ("Fase B"), pendiente
  de que exista contenido real de manuscrito que auditar —hoy
  `thesis/chapters/` está vacío y `research/argument-ledger/` tiene un
  solo `ARG-*`—: el generador de *Authorship Evidence Bundle* y el
  *Originality Dossier*. Se **bloquea** hasta decisión explícita del
  investigador: cualquier comparación textual algorítmica contra el
  corpus (*Source Appropriation Audit*), porque choca con
  `.claude/rules/sources.md` (no hay texto fuente completo almacenado
  localmente contra el cual comparar) — el investigador debe decidir si
  existe un corpus local privado, fuera de Git, para ese propósito, o si
  esa comprobación queda fuera del alcance de la IA de este repositorio.
  Ninguna herramienta de detección probabilística de IA se adopta ni se
  planea adoptar.

## DEC-009 — Cierre de auditoría crítica y entrada en Research Phase 1

- **Fecha:** 2026-08-08
- **Estado:** aceptada
- **Contexto:** el investigador pidió una auditoría crítica de 12 frentes
  (PR #12, fichas de lectura, citas, argument-ledger, corpus,
  metodología, repositorio completo) antes de iniciar una etapa
  intensiva de investigación filosófica, con la regla explícita de
  corregir solo lo mínimo indispensable y reportar —no decidir— todo lo
  que requiriera juicio humano (`ai/log/IA-2026-08-08-12.md`).
- **Decisión:** auditoría completada. Se corrigieron dos hallazgos
  concretos y menores: una afirmación desactualizada en `README.md`
  sobre el estado del corpus (ya no es cierto que "ninguna entrada" del
  mapa fue leída o citada — tres fuentes lo están) y la descripción del
  PR #12 en GitHub (documentaba solo 2 de 15 commits). No se encontraron
  identificadores duplicados, citas huérfanas, enlaces rotos,
  contradicciones metodológicas internas, ni registros de IA
  incompletos. El duplicado ya conocido `SRC-037`/`SRC-185` en
  `corpus-map.md` sigue correctamente documentado en el propio archivo,
  sin acción adicional requerida mientras ambos permanezcan
  `CANDIDATE`.
- **Consecuencias:** se **reporta sin ejecutar** un conflicto real: el
  encargo de auditoría pedía clasificar retroactivamente las ~194 citas
  ya integradas con un campo `QUALITY` nuevo, lo cual contradice
  directamente `DEC-007` (misma fecha, horas antes), que decidió que la
  auditoría de citas es opt-in y no retroactiva. Queda pendiente de que
  el investigador decida entre mantener `DEC-007`, reabrirlo, o aplicar
  clasificación solo incremental (ya soportado sin cambios). Se declara
  el cierre de esta ronda de auditoría/infraestructura: el repositorio
  entra en **Research Phase 1**, cuyo objetivo es producir conocimiento
  filosófico (leer, interpretar, argumentar, escribir) y no seguir
  ampliando infraestructura. Ningún agente de esta sesión debe crear
  nuevas herramientas, subagentes, carpetas, módulos o protocolos sin
  que una necesidad de investigación real y explícita lo justifique
  (mismo criterio ya vigente desde `DEC-003`, reafirmado aquí como
  cierre de esta fase de consolidación).

## DEC-010 — Refinamiento del título y de la jerarquía conceptual

- **Fecha:** 2026-08-09
- **Estado:** aceptada
- **Nota de reconciliación (2026-08-11):** esta decisión se tomó en una
  sesión paralela (Codex, directamente contra `main`) mientras esta rama
  seguía abierta como PR #12, y quedó registrada allí como «DEC-004»,
  colisionando con el DEC-004 de esta rama (Repository Authority
  Policy). Al fusionar ambas líneas de trabajo se renumeró a `DEC-010`
  sin alterar una palabra de su contenido — ver `ai/log/` de la sesión
  de reconciliación para el detalle completo.
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

## DEC-011 — Capa canónica de research lineage

- **Fecha:** 2026-08-10
- **Estado:** aceptada, pendiente de revisión humana sustantiva
- **Nota de reconciliación (2026-08-11):** misma situación que `DEC-010`
  — registrada originalmente como «DEC-004» en la sesión paralela de
  Codex, renumerada al fusionar sin alterar su contenido.
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

## DEC-012 — Reconciliación de dos líneas de trabajo paralelas (Codex + Claude Code)

- **Fecha:** 2026-08-11
- **Estado:** aceptada
- **Contexto:** entre el cierre de `DEC-009` y esta entrada, el
  investigador trabajó en paralelo con otra herramienta (Codex)
  directamente contra `main`, fusionando 18 PRs (#13–#30) mientras esta
  rama (PR #12) permanecía abierta y sin actualizar. Las dos líneas de
  trabajo resultaron casi completamente disjuntas: `main` ganó gobernanza
  de seguridad (`SECURITY.md`, `CODEOWNERS`), un dossier de investigación
  previa del autor (`research/background/`, dos PDF de tesis propias
  archivadas), un marco de publicaciones (`research/publications/`), un
  cambio de título de la tesis (`DEC-010`), y renombró
  `research/sources/corpus-map.md` a `library-manifest.md`; esta rama
  ganó tres fuentes primarias de Derrida verificadas y citadas (194
  citas), el primer argumento del repositorio (`ARG-001`), `ai/quote-audit/`
  y la política de integridad de autoría (`DEC-007`, `DEC-008`). Ninguna
  de las dos sesiones tenía visibilidad de la otra. Se detectaron dos
  colisiones semánticas reales que un merge automático no habría
  señalado: el identificador `DEC-004` usado tres veces para tres
  decisiones distintas, y las fuentes `SRC-002`/`SRC-004`/`SRC-005`
  revertidas a `CANDIDATE` en el `library-manifest.md` de `main` (porque
  Codex renombró el archivo a partir del estado anterior a que esta rama
  las marcara `CITED`).
- **Decisión:** el investigador autorizó expresamente resolver la
  reconciliación "según criterio" de esta sesión. Se aplicaron los
  siguientes criterios, en orden de prioridad: (1) preservar todo
  contenido sustantivo de ambas líneas, sin descartar trabajo; (2)
  renumerar en vez de sobrescribir cualquier identificador colisionado
  (`DEC-004` de Codex → `DEC-010`/`DEC-011`, contenido intacto); (3)
  adoptar el renombre `library-manifest.md` de Codex como ruta canónica
  hacia delante (ya fusionado en `main`, con contenido más amplio: 201
  candidatos) y reaplicarle las promociones a `CITED` de `SRC-002`,
  `SRC-004` y `SRC-005` más la anotación de traducción de `SRC-005`
  (Manantial 2010) y la relación `PI-07`, en vez de mantener un
  `corpus-map.md` paralelo; (4) combinar `bibliography.bib` (3 entradas
  Derrida + 2 entradas de investigación previa del autor, sin colisión
  de claves); (5) conservar los dos PDF de tesis propias archivadas
  (`research/background/**/originals/`) como excepción explícita, no
  tácita, a `.claude/rules/sources.md` — enmendada para distinguir obra
  de terceros (prohibida) de obra propia ya depositada del investigador
  (permitida con procedencia documentada); (6) actualizar el candado
  `validate_no_private_library_files()` (`scripts/auditar_repositorio.py`,
  añadido en esta misma rama antes de la reconciliación) con una lista de
  excepción explícita y acotada a esas rutas exactas, no una excepción
  genérica a la extensión `.pdf`.
- **Consecuencias:** ningún contenido de ninguna de las dos líneas se
  perdió. `research/sources/corpus-map.md` deja de existir como archivo;
  todo lo que lo referenciaba (fichas, scripts, `README.md`,
  `research/methodology.md`) se actualizó a `library-manifest.md`. Los
  scripts de ambas líneas (`auditar_repositorio.py`, con adiciones
  independientes de Codex y de esta rama) se combinaron a mano, no por
  fusión automática de Git, y se revalidaron con
  `python3 scripts/auditar_repositorio.py`, las suites de `ai/plaa/` y
  `ai/quote-audit/`, antes de darse por resuelta esta entrada. Detalle
  completo en el registro de intervención de IA correspondiente
  (`ai/log/`).

## DEC-013 — Método filosófico general: deconstrucción heredada como eje organizador

- **Fecha:** 2026-08-11
- **Estado:** aceptada
- **Contexto:** `research/methodology.md` §1 marcaba como `DECISIÓN HUMANA
  REQUERIDA` qué combinación de enfoques orienta la tesis, sin resolver.
- **Decisión:** la deconstrucción, tal como la practicó Derrida, es el
  enfoque organizador; genealogía, análisis comparado, lectura
  hermenéutica y reconstrucción normativa son auxiliares y subordinados,
  según el texto de §1.
- **Consecuencias:** define qué cuenta como argumento válido en la tesis;
  deja pendiente en §10 si esa lente heredada requiere justificación
  adicional para leer autores anteriores a Derrida.

## DEC-014 — Criterio de selección del corpus: centralidad genealógica, sin gate de edición ni límite temporal fijo

- **Fecha:** 2026-08-11
- **Estado:** aceptada
- **Contexto:** `research/methodology.md` §2 marcaba como `DECISIÓN HUMANA
  REQUERIDA` los criterios explícitos de inclusión/exclusión del corpus.
- **Decisión:** el criterio principal de inclusión es la centralidad de la
  obra para alguna de las cuatro genealogías que la lectura deconstructiva
  trabaja (soberanía, hospitalidad, animalidad, comunidad — coherente con
  `DEC-013`). La disponibilidad de edición verificable o traducción
  autorizada no condiciona la entrada al corpus como candidata, solo el
  avance a `CITED`. No hay límite temporal fijo: el corpus admite
  publicaciones nuevas mientras dure la investigación, sujetas al criterio
  de centralidad genealógica.
- **Consecuencias:** una obra puede registrarse como candidata en
  `library-manifest.md` con limitaciones de edición declaradas
  explícitamente, sin que eso la excluya; el corte 2020–2026 de la
  sección G deja de leerse como límite del corpus y pasa a ser solo el
  alcance de la búsqueda que lo generó.

## DEC-015 — Fuentes primarias y secundarias: criterio por tipo de contribución, no por categoría del manifiesto

- **Fecha:** 2026-08-11
- **Estado:** aceptada
- **Contexto:** `research/methodology.md` §3 marcaba como `DECISIÓN HUMANA
  REQUERIDA` la regla para distinguir fuente primaria de secundaria y las
  condiciones bajo las cuales una secundaria puede sostener una premisa.
- **Decisión:** una fuente es primaria si presenta un argumento filosófico
  original sobre alguna `PI-*`, sin importar si su autor pertenece a las
  cuatro genealogías de `DEC-013`; es secundaria si su contribución es
  comentar o criticar el argumento de otro. No coincide automáticamente
  con las etiquetas `PRIMARY_CORE`/`SECONDARY_CORE` del manifiesto. Una
  fuente secundaria puede sostener una premisa por sí sola.
- **Consecuencias:** no exige reclasificar de inmediato las 211 entradas
  de `library-manifest.md`; el criterio se aplica caso por caso, no como
  relabeling retroactivo.

## DEC-016 — Protocolo de lectura cercana: leído vs. consultado, registro de sesiones, citas bajo APA 7

- **Fecha:** 2026-08-11
- **Estado:** aceptada
- **Contexto:** `research/methodology.md` §4 marcaba como `DECISIÓN HUMANA
  REQUERIDA` el protocolo de lectura cercana.
- **Decisión:** un pasaje es "leído" cuando se trabaja en su contexto
  argumentativo, no solo localizado ("consultado" en ese caso). Cada
  sesión de lectura registra fecha, hora de inicio, hora de fin, página
  inicial y página final. Una cita solo se reconoce como tal si cumple
  APA 7.ª edición: menos de 40 palabras integrada con comillas; 40 o más,
  cita en bloque.
- **Consecuencias:** se añade una sección "Registro de sesiones de
  lectura" a `templates/ficha-fuente.md`. El umbral de 40 palabras, ya
  implementado como auditoría opcional en
  `ai/quote-audit/prompts/05-apa7-structural.md`, pasa a ser requisito de
  base para toda cita nueva. No se reaudita retroactivamente ninguna de
  las 194 citas ya registradas antes de esta fecha.

## DEC-017 — Disputas de interpretación: documentación por nivel y origen obligatorio

- **Fecha:** 2026-08-11
- **Estado:** aceptada
- **Contexto:** `research/methodology.md` §5 marcaba como `DECISIÓN
  HUMANA REQUERIDA` cómo documentar una disputa de interpretación entre
  dos lecturas plausibles de un mismo pasaje, y quién puede plantearla.
- **Decisión:** una disputa a nivel de pasaje (antes de usarse como
  evidencia) se registra en "Objeciones y límites" de la ficha de fuente;
  una disputa a nivel de argumento (cuestiona el uso evidencial ya hecho)
  se registra en "Objeciones y respuestas" del `ARG-*`, que referencia en
  vez de duplicar una disputa de nivel de pasaje ya registrada. Toda
  objeción, en cualquiera de los dos lugares, debe declarar su origen:
  `investigador`, `epistemic-auditor`, un tercero humano identificado por
  nombre, o una IA de terceros identificada por herramienta y modelo. Una
  objeción sin origen declarado no se considera completa.
- **Consecuencias:** se añade el campo `**Origen:**` al formato de
  objeciones en `templates/ficha-fuente.md` y `templates/ficha-argumento.md`;
  se corrigen retroactivamente las dos objeciones ya existentes en
  `ARG-001.md`, declarando su origen real (esta sesión de Claude Code, no
  el investigador ni el subagente `epistemic-auditor`).

## DEC-018 — Traducciones: disponibilidad real, preferencia por el idioma original cuando el archivo existe

- **Fecha:** 2026-08-11
- **Estado:** aceptada
- **Contexto:** `research/methodology.md` §6 marcaba como `DECISIÓN HUMANA
  REQUERIDA` si se cita en idioma original, traducción publicada, o
  ambas, antes de la primera cita textual del corpus.
- **Decisión:** se cita de cualquier edición autorizada, en cualquier
  idioma, siempre que sea publicación válida. El idioma original de
  composición tiene preferencia cuando el investigador tiene acceso al
  archivo; en la práctica, se cita de la obra efectivamente disponible,
  sin esperar a conseguir el original. El investigador puede registrar
  traducciones propias de un pasaje cuando lo considere necesario,
  distinguiéndolas de la cita en el idioma de la edición consultada.
- **Consecuencias:** no exige ninguna acción retroactiva sobre las tres
  fuentes ya citadas (dos en inglés, una en español, ninguna en
  francés); si en el futuro se consigue una edición francesa, esa
  edición se preferiría para nuevas citas sin invalidar las ya
  cotejadas.

## DEC-019 — Procedimiento de cotejo: edición física prioritaria, nivel uniforme, corpus doctoral 100% humano

- **Fecha:** 2026-08-11
- **Estado:** aceptada
- **Contexto:** `research/methodology.md` §7 dejaba pendiente solo el
  detalle del procedimiento de cotejo (edición física o digital, doble
  verificación en citas centrales), tras haberse usado en esta misma
  sesión, para material de trasfondo (`research/background/**`), un
  patrón de lectura de IA seguida de autorización explícita del
  investigador (`ai/log/IA-2026-08-11-24.md`) que no se había definido
  si aplicaba también al corpus doctoral.
- **Decisión:** la edición física, cuando el investigador tiene acceso a
  ella, prevalece sobre el PDF para el cotejo, y su uso debe declararse
  explícitamente (`**Edición cotejada:**` en `templates/ficha-fuente.md`);
  sin declaración se asume digital. El nivel de verificación es uniforme:
  cotejo humano directo para toda cita, sin un nivel reforzado aparte
  para citas centrales. El documento oficial de la tesis y cualquier
  artículo derivado exigen construcción 100% humana; el patrón de
  autorización usado para el trasfondo queda explícitamente excluido del
  corpus doctoral y sus citas.
- **Consecuencias:** se añade el campo `**Edición cotejada:**` a
  `templates/ficha-fuente.md` y se completa retroactivamente en las tres
  fichas ya cotejadas (`digital (PDF)`, dato ya constaba en
  `bibliography.bib`). Cierra explícitamente la pregunta, dejada abierta
  por `IA-2026-08-11-24.md`, de si el patrón de autorización del
  trasfondo podía extenderse al corpus doctoral: no puede.

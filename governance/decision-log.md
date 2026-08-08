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

# Marco de publicaciones derivadas

Este directorio transforma investigación doctoral **ya validada** en entregables científicos. No constituye una línea paralela: cada publicación consume los mismos `PI-*`, `ARG-*`, conceptos, citas verificadas, claves BibTeX y registros `IA-*` que la tesis.

## Autoridades canónicas

| Objeto | Autoridad | Regla |
|---|---|---|
| Preguntas | [`../questions.md`](../questions.md) | Enlazar `PI-*`; no reformular. |
| Argumentos | [`../argument-ledger/`](../argument-ledger/) | Enlazar `ARG-*`; no copiar. |
| Conceptos | Registro conceptual canónico del proyecto | Enlazar ficha/ancla; su ubicación estable está pendiente de decisión humana. No definir aquí. |
| Bibliografía | [`../sources/bibliography.bib`](../sources/bibliography.bib) | Referenciar claves; nunca crear otra bibliografía. |
| Citas verificadas | `../sources/notes/<clave>.md#citas-verificadas` | Enlazar ficha, sección y localizador; no crear otra base de citas. |
| IA | [`../../ai/`](../../ai/) | Enlazar `IA-*`; no duplicar logs. |
| PLAA | [`../../ai/plaa/`](../../ai/plaa/) | Enlazar el informe del `ARG-*`. |

Enlazar un objeto no altera su estado epistémico. Solo fuentes procesadas, citas cotejadas y argumentos validados pueden respaldar una publicación.

## Documentos

- [`publication-registry.md`](publication-registry.md): inventario único.
- [`publication-roadmap.md`](publication-roadmap.md): propuestas, no manuscritos.
- [`workflow-and-governance.md`](workflow-and-governance.md): estados, puertas, autoría y trazabilidad.
- [`article-template.md`](article-template.md): plantilla reutilizable.
- [`journal-registry.md`](journal-registry.md): destinos potenciales.
- [`framework-report.md`](framework-report.md): auditoría y decisiones pendientes.

No se crean subdirectorios vacíos por tipo. Un expediente se abre solo tras aprobación humana y cuando el entregable lo requiere.

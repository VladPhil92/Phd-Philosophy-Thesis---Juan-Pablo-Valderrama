# Auditoría arquitectónica integral — 2026-08-10

## Alcance y método

Se inspeccionó el árbol versionado completo: documentos raíz, gobernanza,
investigación, fuentes, bibliografía, antecedentes, análisis, argumentos,
plantillas, scripts, configuración de agentes, política y registros de IA, PLAA,
manuscrito, recursos y CI. Se revisaron responsabilidades, identificadores,
enlaces locales, duplicación bibliográfica y separación epistémica. La auditoría
no evalúa como verdaderas las formulaciones filosóficas ni sustituye decisiones
del investigador.

## Hallazgos y resolución

| Área | Hallazgo | Riesgo | Resolución mínima |
|---|---|---|---|
| Corpus y bibliografía | `corpus-map.md` y `bibliography.bib` podían leerse como catálogos competidores; el mapa usaba dos esquemas de tabla y categorías funcionales no exclusivas. | Doble identidad y estados ambiguos. | Un solo `library-manifest.md` gobierna obra, categoría y progreso; BibTeX queda limitado a ediciones citables. |
| Bibliografía | `SRC-037` y `SRC-185` nombraban la misma obra. | Duplicación futura de edición y citas. | Se conserva `SRC-037`; `SRC-185` se retira y documenta como alias fusionado. |
| Citas | Las citas vivían en fichas sin identificador reutilizable. | Duplicación al enlazar varios argumentos. | `quote-ledger.md` asigna `QUOTE-*` y apunta a una única transcripción. |
| Conceptos | PLAA define objetos de análisis conceptual, pero no un índice de investigación. El dossier histórico tiene evolución propia y limitada al antecedente. | Confundir auditoría automática, historia previa y posición doctoral. | `concept-registry.md` es el único índice doctoral; no contiene prosa ni reemplaza esos análisis. |
| Argumentos | `argument-ledger/` y `argument-map.md` tienen funciones complementarias: fichas frente a relaciones. | Bajo; los nombres podían sugerir duplicación. | Se conservan, declarando el ledger como autoridad y el mapa solo como vista relacional. |
| Preguntas | README presenta el problema, mientras `questions.md` mantiene IDs y estados. | Formulaciones narrativas confundidas con autoridad. | Se reafirma `questions.md` como única definición operativa; README solo presenta y enlaza. |
| Decisiones | El log ya existía, pero entradas antiguas no listaban siempre alternativas o problema con los mismos rótulos. | Inconsistencia retrospectiva menor. | Se fija forma mínima prospectiva sin reescribir la historia. |
| IA | Política, protocolo, plantilla y registros tienen papeles distintos. PLAA es herramienta auditora, no agente autoral. | Aparente redundancia normativa. | Se conservan: política detallada, resumen transversal, formato de evidencia y registros son responsabilidades no competidoras. |
| Procedencia | La cadena mencionaba `QUOTE`, pero negaba IDs propios. | Trazabilidad insuficiente cuando una cita sirve a varios argumentos. | Se incorpora el ledger, sin carpetas o base de datos nuevas. |
| Antecedentes | La tesis de maestría aparece en BibTeX y en su dossier; su PDF autoral está archivado. | Tratarla como fuente primaria o posición vigente. | Se registra una sola obra en el manifiesto como `PREVIOUS_RESEARCH_BY_AUTHOR`; BibTeX es solo representación citable y el dossier, análisis histórico. |
| Carpetas y enlaces | No se hallaron raíces obsoletas, carpetas huérfanas, marcadores de fusión ni enlaces locales rotos. `assets/`, `analysis/`, capítulos y ledger están vacíos intencionalmente y gobernados por README. | Bajo. | No se añaden niveles ni archivos de relleno. |
| Metadatos | Los candidatos contienen títulos y años exploratorios, algunos obtenidos por búsquedas previas y sin cotejo editorial. | Falsa precisión o atribución de lectura. | Se preservan como `PENDIENTE`, `CANDIDATE`/`IDENTITY_VERIFIED` y `NOT_REGISTERED`; no se fabrican ISBN, idioma o edición. |

## Matriz de autoridad canónica

| Objeto | Ubicación única de autoridad |
|---|---|
| Concepto | `research/concept-registry.md` |
| Cita | `research/sources/quote-ledger.md` (índice); transcripción única en la ficha enlazada |
| Argumento | `research/argument-ledger/ARG-*.md` |
| Obra y estado de lectura | `research/sources/library-manifest.md` |
| Edición y registro bibliográfico citable | `research/sources/bibliography.bib`, enlazado a un `SRC-*` |
| Pregunta de investigación | `research/questions.md` |
| Registro de IA | `ai/IA-*.md` |
| Decisión | `governance/decision-log.md` |
| Investigación previa y trasfondo autoral | `research/background/` |

Una ficha de lectura, un registro BibTeX o una presentación narrativa puede
referenciar una autoridad, pero no redefine el objeto ni su estado.

## Gobernanza del corpus

Las ocho categorías exclusivas del manifiesto eliminan la mezcla anterior entre
prioridad, función temática y tipo de fuente. La tesis de maestría se clasifica
exclusivamente como investigación previa del autor. Ningún candidato se presenta
como leído, adquirido o listo para uso doctoral. El archivo autoral local no
convierte el antecedente en fuente filosófica primaria.

## Simplificación aplicada

No se creó una base de datos, biblioteca digital, carpeta por concepto/cita ni
software de gestión. Se sustituyó un mapa heterogéneo, se fusionó un duplicado y
se añadieron dos tablas vacías que solo se poblarán con investigación real. Las
estructuras existentes con responsabilidades propias no se fusionaron por mera
semejanza nominal.

## Determinación

**READY FOR INFRASTRUCTURE FREEZE.**

La arquitectura ya cubre identidad y avance del corpus, preguntas, conceptos,
citas, notas, argumentos, decisiones, procedencia, IA, escritura y revisión con
una autoridad definida por objeto. Los pendientes son de contenido y validación
humana, no de estructura. Cinco años de trabajo pueden continuar agregando filas
y fichas sin otro rediseño.

## Roadmap exclusivamente investigativo

1. Integrar la tesis de grado como `PREVIOUS_RESEARCH_BY_AUTHOR`, sin convertirla en posición doctoral.
2. Terminar el cotejo y procesamiento de la tesis de maestría.
3. Registrar progresivamente el corpus completo y verificar cada edición.
4. Leer las fuentes filosóficas primarias seleccionadas.
5. Extraer y cotejar citas con página impresa.
6. Poblar el registro de conceptos con relaciones documentadas.
7. Construir el registro de argumentos y sus objeciones.
8. Comenzar la escritura doctoral solo desde argumentos revisados.

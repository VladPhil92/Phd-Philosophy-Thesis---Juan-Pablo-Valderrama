# PLAA — Módulo 1: Argument Miner — ARG-001

**Fuente auditada:** `research/argument-ledger/ARG-001.md`
**Método:** ejecución determinista de `plaa.miner.mine_argument_file` (sin
interpretación) seguida de segmentación manual guiada por
`ai/plaa/prompts/01-argument-miner.md` únicamente donde el texto libre de
una sección mezcla varios nodos (p. ej. "Objeciones y respuestas",
"Interpretaciones alternativas", "Inferencia"). No se completó ninguna
sección vacía; no se añadió contenido ausente del texto.

> Este informe no es un informe de juicio (no requiere frontmatter YAML
> del esquema `analysis-report`, según indica el prompt del módulo 1).
> Es un insumo trazable para los módulos 2, 5, 6 y 7.

## Salida determinista de `plaa.miner`

Secciones detectadas por encabezado (`##`) en el archivo, en orden:

1. Afirmación (claim)
2. Premisas
3. Respaldo de fuentes
4. Evidencia textual
5. Inferencia
6. Interpretaciones alternativas
7. Objeciones y respuestas
8. Alcance y límites
9. Uso de IA
10. Historial de revisión
11. Uso previsto en el manuscrito

Ninguna sección está vacía.

## Nodos extraídos

### CLAIM

| Texto literal (cita) | Sección |
|---|---|
| «La "Soberanía de la Hospitalidad" no designa un tercer concepto que sintetiza soberanía y hospitalidad, sino el nombre del tránsito por el cual una potencia soberana ilimitada ("yo puedo") se convierte, caso por caso, en una no-potencia que obliga éticamente ("no puedo, por tanto debo"). Extendido más allá de lo humano, ese tránsito —no la abolición de la soberanía, que los tres textos tratan como imposible o indeseable— es la tarea que una comunidad política interespecie tendría que realizar.» | Afirmación (claim) |

### PREMISE

| # | Texto literal | Sección |
|---|---|---|
| P1 | «En *La bestia y el soberano, Vol. I*, Derrida define la soberanía como potencia sin límite: "un poder, una potencia, un 'yo puedo'" (p. 306, retomado p. 352).» | Premisas |
| P2 | «En *Hospitality, Volume I*, Derrida define el límite empírico de la hospitalidad concreta por su reverso exacto: "I am not able, therefore I ought" (p. 232).» | Premisas |
| P3 | «En *The Animal That Therefore I Am*, el giro benthamita de la capacidad (razón) a la vulnerabilidad (sufrimiento) produce la misma estructura aplicada al viviente no-humano: "Being able to suffer is no longer a power; it is a possibility without power" (p. 27).» | Premisas |
| P4 | «Las tres fuentes pertenecen al mismo ciclo institucional de seminarios de Derrida en la EHESS (1991–2003) o son estrictamente contemporáneas de él (…) no son lecturas afines elegidas por semejanza temática, sino cortes de un mismo proyecto de pensamiento tardío.» | Premisas |

### CONCLUSION (segmentación manual de "Inferencia")

El miner determinista no mapea "Inferencia" a un tipo de nodo (no está en
`SECTION_HEADINGS`); se segmenta aquí manualmente porque el párrafo mezcla
una conclusión intermedia con una admisión explícita de salto no
demostrado (ver ASSUMPTION más abajo).

| Texto literal | Sección |
|---|---|
| «De 1–3: en las tres fuentes, el concepto que hace de eje normativo (…) se articula mediante la misma matriz lógica: una potencia sin límite (premisa 1) es lo que un sujeto ético *no tiene* respecto de aquello a lo que debe responder, y es precisamente esa carencia —no una capacidad— la que genera la obligación (premisas 2–3). De 4: dado que las tres fuentes son cortes de un mismo proyecto institucional, esta coincidencia estructural es más plausible como matriz de pensamiento deliberada o al menos consistente en Derrida tardío que como semejanza casual entre lecturas independientes.» | Inferencia |

Nótese que esta CONCLUSION intermedia (coincidencia estructural en las
tres fuentes) es distinta de la CLAIM normativa de la sección "Afirmación"
(que la "Soberanía de la Hospitalidad" *debería* nombrarse como ese
tránsito). El propio texto declara ese salto como no demostrado (ver
ASSUMPTION).

### ASSUMPTION (segmentación manual de "Inferencia")

| Texto literal | Sección |
|---|---|
| «**Paso no demostrado, señalado explícitamente:** de la coincidencia estructural (premisas 1–3) a la afirmación normativa de que la "Soberanía de la Hospitalidad" *debería* nombrarse como ese tránsito (la claim) hay un salto que ninguna de las tres fuentes da por sí sola — es una propuesta conceptual para la tesis, no una conclusión que Derrida extraiga en ningún pasaje. Este paso requiere justificación filosófica propia del investigador, no solo respaldo textual cruzado.» | Inferencia |

Este fragmento no es una premisa oculta inventada por esta auditoría: es
el propio `ARG-001.md` el que declara la laguna. Se extrae como ASSUMPTION
porque funciona como el supuesto no argumentado (la propuesta conceptual
en sí) del que depende el paso de la CONCLUSION intermedia a la CLAIM.

### DISTINCTION (segmentación manual de "Interpretaciones alternativas")

El miner determinista devuelve las tres viñetas como un solo nodo
`DISTINCTION`. Se segmentan aquí porque son tres lecturas alternativas
distintas, cada una dirigida a una premisa o inferencia distinta.

| # | Texto literal | Dirigida a |
|---|---|---|
| D1 | «**Coincidencia retórica, no matriz lógica compartida**: las tres fórmulas ("yo puedo", "no puedo por tanto debo", "posibilidad sin poder") podrían leerse como usos ad hoc del vocabulario potencia/impotencia en contextos argumentales distintos, sin que Derrida las presente como una sola estructura. Esta lectura reduciría el argumento a una observación estilística, no conceptual.» | Inferencia (paso premisas 1–3 → matriz común) |
| D2 | «**La hospitalidad y la ética animal no son homologables sin más**: `derrida-2008-animal.md` («Objeciones y límites») ya señala que Derrida es cuidadoso en no asimilar sin más la cuestión de la hospitalidad y la cuestión animal. Tratar las tres fuentes como una sola matriz podría forzar esa distinción que el propio Derrida preserva.» | Inferencia (premisas 2 y 3 tratadas como una matriz) |
| D3 | «**El "no puedo, por tanto debo" es límite, no fundamento**: en `derrida-2023-hospitality.md` esa fórmula aparece como reconocimiento honesto de un límite empírico (no se puede recibir a todos), no como definición positiva de la hospitalidad. Usarla como equivalente estructural del "yo puedo" soberano podría estar forzando una simetría que el texto no ofrece — el "yo puedo" es definición, el "no puedo" es constatación de límite; son categorías gramaticalmente distintas.» | Premisa 2 (uso de la fórmula P2) |

### OBJECTION / REBUTTAL (segmentación manual de "Objeciones y respuestas")

El miner determinista devuelve toda la sección como un solo nodo
`OBJECTION`. Se segmenta aquí en tres objeciones distintas, cada una con
su origen declarado y el estado de su respuesta — ninguna respuesta
sustantiva existe todavía para ninguna de las dos primeras (ambas quedan
explícitamente "pendiente"); esto se reporta tal cual, sin inventar un
`REBUTTAL` que el texto no contiene.

| # | Origen (declarado en el texto) | Texto literal de la objeción | Estado de la respuesta |
|---|---|---|---|
| OBJ1 | Claude Code, sesión `IA-2026-08-08-09` | «la premisa 4 (unidad institucional del ciclo de seminarios) es un dato biográfico-editorial, no un argumento filosófico — que tres textos compartan seminario no implica que compartan tesis.» | **Sin REBUTTAL.** Texto literal: «**Respuesta pendiente**: no resuelta en este documento; requiere que el investigador decida qué peso darle a la contigüidad institucional frente al contenido conceptual por sí solo.» — esto es la constatación de ausencia de respuesta, no una respuesta. |
| OBJ2 | Claude Code, sesión `IA-2026-08-08-09` | «la claim depende de tratar "posibilidad sin poder" (animal) y "no puedo, por tanto debo" (hospitalidad) como la misma figura, cuando la primera describe una capacidad pasiva (poder sufrir) y la segunda una limitación activa del anfitrión (no poder recibir a todos) — son estructuras gramaticalmente distintas (voz pasiva vs. primera persona activa) que podrían no ser homologables sin trabajo conceptual adicional.» | **Sin REBUTTAL.** Texto literal: «**Respuesta pendiente**: no resuelta; ver «Interpretaciones alternativas», tercer punto.» — remite a D3, que es ella misma otra objeción no resuelta, no una respuesta a OBJ2. |
| OBJ3 | No es una objeción dirigida a una premisa; es una nota de alcance sobre el propio listado | «Objeción pendiente de origen externo: ninguna objeción de este argumento ha pasado todavía por el subagente `epistemic-auditor` ni por la lectura manual del investigador. Este listado es un punto de partida, no una revisión completa.» | No aplica (nota de proceso, no objeción filosófica al argumento). |

### DISTINCTION adicional (segmentación manual de "Alcance y límites")

| Texto literal | Sección |
|---|---|
| «Este argumento cubre únicamente la coincidencia estructural potencia/no-potencia en las tres fuentes ya citadas en el corpus. No cubre (…) la homología bestia/soberano (…) ni la distinción dominio/nombrar de `derrida-2008-animal.md` (…). Son tres candidatos maduros distintos, no un solo argumento — no deben fusionarse sin justificación explícita.» | Alcance y límites |

## DEFINITION

No se detecta ninguna `DEFINITION` explícita dentro de `ARG-001.md` en el
sentido estricto exigido por el prompt (el texto no define "soberanía",
"hospitalidad" ni "potencia" dentro de esta ficha; cita definiciones que
las fuentes primarias formulan, pero no las convierte en definición propia
del argumento). Se reporta como ausente, no se completa por plausibilidad.

## QUESTION

No se detecta ninguna `QUESTION` explícita como nodo propio (las preguntas
relacionadas `PI-01, PI-02, PI-04, PI-07` se enlazan por identificador en
la cabecera, no se formulan como interrogación dentro del cuerpo del
argumento).

## COUNTEREXAMPLE

No se detecta ningún `COUNTEREXAMPLE` ya presente en el texto de
`ARG-001.md`. (La búsqueda del mejor contraejemplo posible es tarea del
módulo 7, no de este miner — este miner solo reporta lo que el texto ya
contiene.)

## Notas de trazabilidad

- Todas las citas de esta tabla son literales, copiadas del archivo
  auditado en la fecha de este informe.
- La segmentación de "Objeciones y respuestas", "Interpretaciones
  alternativas", "Alcance y límites" e "Inferencia" es la única
  intervención no estrictamente mecánica de este informe (permitida
  explícitamente por `01-argument-miner.md`, punto 3); no se reescribió
  ningún fragmento, solo se separaron viñetas y párrafos ya existentes.

# Lista de verificación de falacias — ARG-001

> Cada fila requiere justificación textual, no una intuición. `NOT_DETECTED`
> es el valor por defecto y no requiere justificación extensa; cualquier
> otro valor sí. Ninguna fila afirma certeza absoluta: vocabulario
> exactamente `POSSIBLE` / `LIKELY` / `UNLIKELY` / `NOT_DETECTED`.

| Falacia | Veredicto | Justificación (con ubicación textual) |
|---|---|---|
| Ad hominem | NOT_DETECTED | El argumento no ataca a ninguna persona ni posición por su origen; toda la evidencia es textual (citas de Derrida cotejadas). |
| Hombre de paja (strawman) | NOT_DETECTED | La sección "Interpretaciones alternativas" presenta las lecturas contrarias con razonable caridad (p. ej. D2 cita explícitamente la propia advertencia de `derrida-2008-animal.md` contra asimilar hospitalidad y ética animal); no se detecta una versión debilitada de una posición contraria construida solo para refutarla fácilmente. |
| Falso dilema | **POSSIBLE** | Ver justificación abajo. |
| Petición de principio (begging the question) | NOT_DETECTED | Las premisas 1–3 (citas verificadas independientes) no presuponen la claim normativa; de hecho la propia sección "Inferencia" declara ese paso «no demostrado», lo que es incompatible con que la claim ya esté presupuesta en las premisas. |
| Afirmación del consecuente | NOT_DETECTED | La estructura deóntica de P2 («I am not able, therefore I ought», p. 232) se usa en sentido modus-ponens (se afirma la carencia, se concluye la obligación), no se afirma la obligación para concluir la carencia. |
| Negación del antecedente | NOT_DETECTED | No aparece esta estructura en ningún tramo de "Inferencia". |
| Equivocación | **POSSIBLE** | Ver justificación abajo. |
| Falsa causa | **POSSIBLE** | Ver justificación abajo. |
| Falacia de composición | NOT_DETECTED | El patrón detectable en el texto (generalizar de 3 pasajes a un rasgo del "Derrida tardío") encaja mejor como generalización apresurada (fila siguiente) que como composición parte-todo en sentido estricto; clasificarlo también como composición sería doble conteo del mismo fragmento bajo una etiqueta menos precisa. |
| Falacia de división | NOT_DETECTED | No se detecta ningún paso que infiera una propiedad de una parte a partir de una propiedad ya afirmada del todo. |
| Circularidad | NOT_DETECTED | La claim no se usa en ningún punto del texto como respaldo de las premisas 1–4; la dirección de apoyo declarada va siempre de premisas a inferencia, nunca al revés. |
| Generalización apresurada | **POSSIBLE** | Ver justificación abajo. |
| Apelación a la autoridad | NOT_DETECTED | Las citas de Derrida se presentan como evidencia textual cotejada (según `.claude/rules/sources.md` y el propio "Respaldo de fuentes"), no como «Derrida lo dijo, por tanto es verdad» fuera de su ámbito — es precisamente el método de cita primaria que `RESEARCH-WORKFLOW.md` exige, no una apelación falaz (instrucción 3 del prompt del módulo 5). |

## Justificaciones extendidas

### Falso dilema — POSSIBLE

La sección "Afirmación (claim)" abre con una disyunción binaria no
argumentada: «La "Soberanía de la Hospitalidad" no designa un tercer
concepto que sintetiza soberanía y hospitalidad, sino el nombre del
tránsito por el cual (…)». Solo se presentan dos opciones —(a) concepto de
síntesis, (b) nombre de un tránsito— sin descartar explícitamente otras
caracterizaciones posibles (p. ej. una analogía heurística, una figura
retórica sin estatuto conceptual propio, un mero parecido de familia entre
tres usos). No se argumenta por qué (a) y (b) agotan el espacio de
lecturas posibles.

**Capa de seguridad hermenéutica:** ¿podría tratarse de una estipulación
definitoria legítima («aquí llamo X a Y») en vez de un falso dilema
retórico que cierre alternativas por la fuerza? Es plausible: el propio
enunciado tiene forma de definición de trabajo para la tesis («candidato
en desarrollo», según el "Origen de este argumento"), no de argumento que
elimine activamente otras lecturas mediante la disyunción. Esta lectura
como estipulación es al menos tan plausible como la lectura como falso
dilema, por lo que se marca `reviewed_as_possible_aporia: true` y la
confianza se mantiene en `POSSIBLE` (no se eleva a `LIKELY`).

### Equivocación — POSSIBLE

Las tres premisas usan vocabulario de "poder/potencia" en construcciones
gramaticales distintas: P1 «un poder, una potencia, un 'yo puedo'»
(capacidad activa, primera persona, definición del soberano); P2 «I am not
able, therefore I ought» (limitación activa del anfitrión, primera
persona); P3 «a possibility without power» (capacidad pasiva de sufrir,
tercera persona / voz pasiva). La sección "Inferencia" trata las tres como
la «misma matriz lógica», y esto es precisamente lo que la propia ficha ya
señala como objeción no resuelta (OBJ2, `ARG-001.md`, "Objeciones y
respuestas": «son estructuras gramaticalmente distintas (voz pasiva vs.
primera persona activa) que podrían no ser homologables sin trabajo
conceptual adicional») y en D3 de "Interpretaciones alternativas» («el
'yo puedo' es definición, el 'no puedo' es constatación de límite; son
categorías gramaticalmente distintas»). Tratar tres sentidos
gramaticalmente distintos de "(no) poder" como una única matriz
proposicional sin argumentar la equivalencia es exactamente la forma de
una equivocación.

**Capa de seguridad hermenéutica:** ¿podría ser una ambigüedad deliberada
del autor citado, propia de su estilo? Muy plausible: Derrida explota de
forma conocida y reiterada la polisemia de *pouvoir* (sustantivo "poder" /
verbo "poder-hacer") a lo largo de su obra tardía, y el juego "yo puedo" /
"no puedo" pertenece a ese registro estilístico deliberado, no a un
descuido lógico de Derrida. Ahora bien, quien produce el movimiento
auditado no es Derrida dentro de un solo texto, sino la síntesis del
investigador entre tres obras distintas (el propio "Origen de este
argumento" lo llama «lectura sintética propuesta para la tesis», no
hallazgo de Derrida) — el riesgo de equivocación recae sobre esa síntesis
inter-textual, no sobre el estilo de Derrida en sí. Por ser la lectura
como juego estilístico deliberado al menos tan plausible como la lectura
como equivocación involuntaria, la confianza inicial (`LIKELY`, dada la
fuerza de la evidencia textual) se rebaja a `POSSIBLE` y se marca
`reviewed_as_possible_aporia: true`.

### Falsa causa — POSSIBLE

La premisa 4 («las tres fuentes pertenecen al mismo ciclo institucional…»)
se usa en "Inferencia" para argumentar que la coincidencia estructural «es
más plausible como matriz de pensamiento deliberada (…) que como
semejanza casual». Esto infiere una causa común (un proyecto de
pensamiento deliberado y unificado) a partir de una correlación temporal e
institucional (contemporaneidad de los seminarios), sin evidencia textual
directa de que Derrida haya concebido las tres formulaciones como una sola
estructura.

**Capa de seguridad hermenéutica:** ¿podría tratarse de una inferencia
abductiva explícitamente declarada como no necesaria, en vez de un
razonamiento que confunda correlación con causa? El propio texto ya marca
esta inferencia como de plausibilidad, no de necesidad («es más plausible
(…) que como semejanza casual», no «por lo tanto es»), lo que reduce el
riesgo de que se presente como demostración causal. Esto es
sustancialmente el mismo punto que la objeción ya registrada en
`ARG-001.md` (OBJ1: «es un dato biográfico-editorial, no un argumento
filosófico»); este hallazgo no la repite como objeción nueva, solo la
nombra con la etiqueta de falacia formal que mejor la describe. Se
mantiene en `POSSIBLE` (no se eleva a `LIKELY`) porque el propio texto ya
matiza el estatuto de esta inferencia como probabilístico, y
`reviewed_as_possible_aporia: true` porque la inferencia de una causa
común de "proyecto de pensamiento" a partir de proximidad institucional es
un tipo de argumento habitual y aceptado en historia intelectual, no
necesariamente falaz por sí solo.

### Generalización apresurada — POSSIBLE

La sección "Inferencia" generaliza de tres pasajes verificados (uno por
fuente) a un rasgo de «Derrida tardío» como proyecto de pensamiento, y la
"Afirmación (claim)" extiende esa generalización aún más lejos —a una
tarea normativa para «una comunidad política interespecie»— sin evidencia
textual adicional más allá de las tres citas ya citadas. El corpus de
Derrida tardío incluye otras obras no examinadas por esta ficha (p. ej.
*Politics of Friendship*, *Specters of Marx*, *Rogues*), de modo que la
generalización a "Derrida tardío" en general se apoya en una muestra
pequeña y ya seleccionada por su afinidad temática con la tesis.

**Capa de seguridad hermenéutica:** ¿podría no ser una generalización
apresurada porque el propio texto se abstiene de presentarla como
concluida? Es plausible y atenúa el hallazgo: la sección "Inferencia"
etiqueta explícitamente el paso final como «no demostrado» y pide
«justificación filosófica propia del investigador». Una generalización
apresurada, en su forma clásica, presenta una conclusión insuficientemente
apoyada *como si* estuviera ya establecida; aquí el texto hace lo
contrario en "Inferencia". Sin embargo, la sección "Afirmación (claim)" —
leída de forma aislada, sin el matiz de "Inferencia"— sí formula la
identificación en tono asertivo y sin cobertura equivalente («no designa…
sino el nombre del tránsito…»), lo que mantiene cierta tensión entre ambas
secciones. Por esta tensión no resuelta entre el tono asertivo de la claim
y el reconocimiento expreso de laguna en la inferencia, se marca
`reviewed_as_possible_aporia: true` y la confianza se mantiene en
`POSSIBLE`, no se eleva a `LIKELY`.

## Capa de seguridad hermenéutica (resumen)

Para las cuatro filas marcadas `POSSIBLE` (falso dilema, equivocación,
falsa causa, generalización apresurada): en los cuatro casos se consideró
explícitamente si el patrón detectado podría ser una aporía, una
ambigüedad deliberada o una lectura demasiado literal de una definición de
trabajo, en vez de un defecto argumental — y en los cuatro casos esa
lectura alternativa resultó al menos tan plausible como la lectura como
falacia, lo que ya se refleja en que ninguna fila se marcó `LIKELY`. Véase
`ai/plaa/prompts/08-hermeneutic-safety-layer.md`.

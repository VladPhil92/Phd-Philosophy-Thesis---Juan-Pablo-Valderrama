# Metodología

**Estado:** idea — andamiaje de decisiones pendientes, no un método adoptado.

Este documento no fija el método filosófico de la tesis. Estructura las
decisiones metodológicas que el investigador debe tomar y registrar, para
que ninguna quede implícita o se presuponga por defecto. Cada sección marca
`DECISIÓN HUMANA REQUERIDA` mientras no exista una elección explícita del
investigador, con fecha y justificación, idealmente registrada también como
entrada en `governance/decision-log.md` si afecta a todo el corpus.

La investigación no presupone de entrada una comunidad política interespecie;
examina primero los límites antropológicos que estructuran la pertenencia
política y evalúa qué consecuencias se derivan de su problematización. Esta
delimitación conceptual no resuelve ninguna de las decisiones metodológicas
pendientes que siguen.

## 1. Método filosófico general

**Decisión (2026-08-11).** El enfoque organizador es la **deconstrucción**,
heredada de la practicada por Jacques Derrida: no es un método que la tesis
aplique por primera vez sobre el corpus, sino un procedimiento ya elaborado
que se adopta como lente para leer a los demás autores (Bodin, Hobbes,
Schmitt, Kant, Lévinas, Heidegger, Agamben, Nancy, Esposito, Donaldson,
Kymlicka). Derrida ocupa así una posición distinta a la de los demás autores
del corpus: es la fuente del método, no solo un objeto sometido a él en el
mismo sentido que los demás.

Los demás enfoques listados son auxiliares, subordinados a ese eje:

- **Genealogía** y **análisis comparado** proveen el material preparatorio
  (reconstrucción de las tríadas de autores en soberanía, hospitalidad,
  animalidad y comunidad) sobre el que se ejerce la lectura deconstructiva.
- **Lectura hermenéutica** (close reading cotejado) es la base evidencial:
  sin cita verificada no hay lectura deconstructiva legítima, solo
  intuición filosófica sin apoyo textual.
- **Reconstrucción normativa** es el resultado, no el punto de partida: los
  ocho principios normativos se justifican *a partir de* lo que la lectura
  deconstructiva muestra sobre los límites antropológicos de la comunidad
  política, no al revés.

Registrada también en `governance/decision-log.md` (`DEC-013`), por afectar
a todo el corpus.

**Pendiente para §10 (límites metodológicos):** queda por decidir, aparte,
si adoptar la deconstrucción derridiana como método heredado exige
justificar también por qué esa lente es apta para autores muy anteriores a
Derrida (Bodin, Hobbes, Kant) — no se resuelve aquí.

## 2. Selección del corpus

**Decisión (2026-08-11).** El criterio principal de inclusión es la
**centralidad de la obra para alguna de las cuatro genealogías** que la
lectura deconstructiva trabaja (`DEC-013`): soberanía (Bodin, Hobbes,
Schmitt...), hospitalidad (Kant, Lévinas, Derrida...), animalidad
(Heidegger, Derrida, Agamben...) o comunidad (Nancy, Esposito...). Una obra
ajena a las cuatro genealogías —aunque relevante para el giro político de
la cuestión animal en términos generales— requiere justificación aparte
para entrar al corpus.

La disponibilidad de edición verificable o traducción autorizada **no es
condición de entrada al corpus como candidata**: una obra central para
alguna genealogía puede registrarse como `CANDIDATE` en
[`research/sources/library-manifest.md`](sources/library-manifest.md) con
esa limitación declarada explícitamente. Sí es condición para avanzar en
la escala de verificación — ninguna obra pasa de `CANDIDATE` a `CITED` sin
edición confirmada y cotejo directo (véase la convención de estados en
`library-manifest.md`).

No hay límite temporal fijo. El corpus permanece abierto a incorporar
publicaciones nuevas que aparezcan mientras dure la investigación, siempre
que satisfagan el criterio de centralidad genealógica; el rango 2020–2026
de la sección G del manifiesto fue el alcance de una búsqueda puntual en su
momento, no un corte definitivo del corpus.

Registrada también en `governance/decision-log.md` (`DEC-014`).

`research/sources/library-manifest.md` reúne actualmente 211 obras
candidatas (seis categorías funcionales A–F, más la ampliación 2020–2026 de
la sección G y el contexto de formación de la sección H). Es el inventario
de trabajo para esta decisión, no una lista cerrada: ningún candidato ha
sido verificado en edición ni leído más allá de las tres fuentes ya
promovidas a `bibliography.bib`.

## 3. Fuentes primarias y secundarias

**Decisión (2026-08-11).** Una fuente es **primaria** cuando presenta un
argumento filosófico original sobre alguna de las preguntas de
investigación (`PI-*`), independientemente de si su autor pertenece a
alguna de las cuatro genealogías de `DEC-013` o a otra categoría del
manifiesto. Es **secundaria** cuando su contribución consiste en comentar,
interpretar o criticar el argumento de otro autor, sin sostener una
posición filosófica propia sobre la pregunta misma.

Este criterio corta transversalmente la clasificación funcional de
`library-manifest.md`: no coincide automáticamente con las etiquetas
`PRIMARY_CORE`/`SECONDARY_CORE` de ese documento, que distinguen dominio
temático, no tipo de contribución. En particular, la literatura del giro
político de la cuestión animal (categoría `STATE_OF_ART`: Garner,
O'Sullivan, Cochrane, Meijer, Donaldson y Kymlicka) cuenta como
**primaria** bajo este criterio, porque argumenta posiciones propias sobre
la comunidad política interespecie, no comenta la obra de otro. Del mismo
modo, un texto de cualquier categoría del manifiesto —incluidas `CONTEXT`,
`DEEPENING` o `METHODOLOGY`— es secundario si su función es interpretar o
criticar a otro autor, y primario si argumenta una posición propia.

Una fuente secundaria **puede sostener una premisa por sí sola**, sin
requerir respaldo adicional de una fuente primaria. No hay jerarquía de
peso evidencial fijada entre ambas: la fuerza de la premisa depende del
argumento, no del tipo de fuente que la sostiene.

Registrada también en `governance/decision-log.md` (`DEC-015`). Este
criterio no exige reclasificar de inmediato las 211 entradas de
`library-manifest.md`: se aplica caso por caso cuando una obra se
promueve a `CITED` y se usa en un `ARG-*`.

## 4. Procedimiento de lectura cercana (close reading)

**Decisión (2026-08-11).** Un pasaje se considera **leído** cuando el
investigador lo trabajó en su contexto argumentativo inmediato — no cuando
fue solo localizado (por ejemplo, mediante búsqueda de texto, índice o
referencia de una fuente secundaria) sin trabajar el argumento que lo
rodea. Un pasaje localizado pero no trabajado en contexto se registra como
**consultado**, no como leído.

Cada sesión de lectura se registra con: fecha, hora de inicio, hora de fin,
página inicial y página final — permite calcular tanto las páginas leídas
por sesión como el ritmo de lectura. El campo único `Fecha de consulta` de
`templates/ficha-fuente.md` no basta para esto: se añade una sección
"Registro de sesiones de lectura" (tabla con esas columnas), acumulativa a
lo largo de las sesiones que use cada ficha.

Una cita textual solo se reconoce como tal si cumple las normas de la
edición vigente de APA (7.ª edición): citas de **menos de 40 palabras** se
integran en el texto con comillas; citas de **40 palabras o más** se
presentan como cita en bloque, sin comillas. Esto formaliza como requisito
de base, para toda cita nueva, el mismo umbral que
`ai/quote-audit/prompts/05-apa7-structural.md` ya implementa como
auditoría opcional (`BLOCK_QUOTE_REQUIRED`) — deja de ser solo una capa de
auditoría más profunda y pasa a ser condición mínima de reconocimiento de
la cita.

Registrada también en `governance/decision-log.md` (`DEC-016`). No exige
reauditar retroactivamente las 194 citas ya registradas antes de esta
decisión; se aplica hacia adelante, salvo que el investigador pida
explícitamente una revisión retroactiva.

## 5. Disputas de interpretación

**Decisión (2026-08-11).** Una disputa de interpretación se documenta
según el nivel al que pertenece, siguiendo la cadena de procedencia
(`governance/provenance.md`):

- **Nivel de pasaje** (antes de que se use como evidencia en ningún
  argumento): se registra en la sección "Objeciones y límites" de la
  ficha de fuente (`templates/ficha-fuente.md`).
- **Nivel de argumento** (el pasaje ya se usa como evidencia y la disputa
  cuestiona esa lectura evidencial): se registra en "Objeciones y
  respuestas" de la ficha de argumento (`templates/ficha-argumento.md`).

Si una disputa registrada a nivel de pasaje se vuelve relevante para un
`ARG-*` posterior, la ficha de argumento **referencia** la entrada de la
ficha de fuente en vez de duplicar su contenido.

**Origen obligatorio.** Toda objeción registrada en cualquiera de los dos
lugares debe declarar quién la plantea:

- `investigador` — el propio Juan Pablo Valderrama Pino;
- `epistemic-auditor` — el subagente, cuando genera una objeción de
  prueba;
- un tercero humano, identificado por nombre;
- una IA de terceros, identificada por herramienta y modelo (por ejemplo,
  "ChatGPT / GPT-5.6").

Una objeción sin origen declarado no se considera completa. Se añade el
campo `**Origen:**` como parte del formato de cada entrada de objeción en
ambas plantillas.

Registrada también en `governance/decision-log.md` (`DEC-017`).

## 6. Traducciones

**Decisión (2026-08-11).** Se cita de cualquier edición autorizada, en
cualquier idioma, siempre que sea una publicación válida (no una
transcripción no autorizada ni un manuscrito sin editar). Cuando el
investigador tiene acceso al archivo de la edición en el idioma original
de composición (francés, en el caso de Derrida), esa edición tiene
preferencia. Pero la regla operativa es la disponibilidad real: el
investigador cita de la obra que tenga efectivamente a su disposición, sin
esperar a conseguir el original si ya cuenta con una edición autorizada en
otro idioma.

Esto no exige ninguna acción retroactiva sobre las tres fuentes ya
citadas: `derrida-2008-animal` (inglés, Fordham UP) y
`derrida-2023-hospitality` (inglés, Chicago UP) se citan de la edición que
el investigador tiene disponible, no del francés; lo mismo aplica a
`derrida-2010-bestia-soberano-1` (español, Manantial). Si en el futuro el
investigador consigue la edición francesa de alguna, esa edición pasaría a
preferirse para nuevas citas, sin invalidar las ya cotejadas.

El investigador puede registrar **traducciones propias** de un pasaje
cuando lo considere necesario, distinguiéndolas explícitamente de la cita
en el idioma de la edición consultada — ya previsto en
`templates/ficha-fuente.md` ("incluir localizador exacto y distinguir la
cita de la traducción propia").

Registrada también en `governance/decision-log.md` (`DEC-018`).

## 7. Verificación de citas

Ya existe una regla operativa mínima: toda cita textual requiere localizador
exacto y cotejo con el original antes de usarse como evidencia (véase
`RESEARCH-WORKFLOW.md`, `.claude/rules/sources.md`). **Decisión (2026-08-11).**
El detalle del procedimiento de cotejo queda fijado así:

- **Edición física frente a digital.** Cuando el investigador tiene acceso a
  la edición física de una fuente, esa edición prevalece sobre el PDF para
  el cotejo; su uso debe declararse explícitamente en la ficha de fuente
  (`**Edición cotejada:**` en `templates/ficha-fuente.md`), no darse por
  supuesto. Si no se declara, se asume cotejo contra edición digital (PDF),
  como en las tres fichas ya existentes.
- **Nivel de verificación uniforme.** Toda cita, sin distinción entre
  evidencia central y de apoyo, requiere cotejo humano directo del
  investigador contra la edición declarada antes de usarse como evidencia.
  No hay un nivel reducido para citas secundarias ni uno reforzado aparte
  para citas centrales: el cotejo humano directo es, en todos los casos, el
  estándar único.
- **El corpus doctoral no admite el patrón de autorización usado para el
  trasfondo.** Para el documento oficial de la tesis y cualquier artículo
  derivado (`research/publications/`), solo se acepta y verifica
  construcción **100% humana**. El patrón usado en `research/background/**`
  (lectura de IA seguida de autorización explícita del investigador,
  `ai/log/IA-2026-08-11-24.md`) es exclusivo del material de trasfondo, que
  no es evidencia doctoral — no se extiende al corpus doctoral ni a sus
  citas: ahí el cotejo debe ser siempre el propio investigador leyendo y
  comparando directamente contra la edición declarada, sin que una
  autorización general lo sustituya.

Registrada también en `governance/decision-log.md` (`DEC-019`).

Existe además, desde 2026-08-08, herramienta (opcional, no obligatoria)
para auditar una cita ya cotejada más allá de su autenticidad —integridad
contextual, pertinencia filosófica, riesgo de extracción engañosa, fuerza
argumentativa— en [`ai/quote-audit/`](../ai/quote-audit/README.md). Esa
herramienta no resuelve ni el detalle de cotejo de esta sección ni la
sección 6 (traducciones): da soporte al procedimiento que el investigador
decida, no lo sustituye.

## 8. Papel de las objeciones

**Decisión (2026-08-11).** Se exige al menos una objeción registrada
("Objeciones y respuestas", con `Origen` declarado según `DEC-017`) antes
de que un argumento pueda alcanzar el estado `READY_FOR_HUMAN_REVIEW`
(véase `templates/ficha-argumento.md`). Basta con que la objeción esté
registrada, sin importar su origen: no se exige que provenga de un origen
distinto al que redactó el argumento, ni que pase necesariamente por el
subagente `epistemic-auditor` o por el investigador. Tampoco se exige que
la objeción esté respondida — este requisito es de objeción registrada, no
de objeción resuelta.

Quién puede plantear objeciones ya está fijado por `DEC-017`: el
investigador, el subagente `epistemic-auditor`, un tercero humano
identificado por nombre, o una IA de terceros identificada por herramienta
y modelo.

`ARG-001` ya satisface este requisito con sus dos objeciones existentes
(origen: Claude Code, sesión `IA-2026-08-08-09`), aunque sigue en
`DEVELOPING` por otras razones y ninguna de las dos objeciones esté
todavía respondida.

Registrada también en `governance/decision-log.md` (`DEC-020`).

## 9. Papel de la IA en el método

Ya regulado de forma transversal por `ai/policy.md` y
`AI-RESEARCH-PROTOCOL.md`: la IA no decide interpretación ni conclusiones.
**Decisión (2026-08-11).** El detalle metodológico queda fijado
consolidando, en un solo lugar, lo que ya se seguía de decisiones previas
de esta sesión — no es sustancia nueva:

**Tareas exploratorias que se delegan de forma habitual:**

- Localización de literatura secundaria candidata
  (`research/sources/library-manifest.md`).
- Generación de objeciones de prueba, con `Origen` declarado
  (`DEC-017`/`DEC-020`).
- Auditoría de citas más allá de su autenticidad
  ([`ai/quote-audit/`](../ai/quote-audit/README.md), `DEC-007`).
- Auditoría de argumentos, fuentes y procedencia
  (subagente `epistemic-auditor`).
- Lectura y análisis de material de **trasfondo** (`research/background/**`,
  no corpus doctoral), solo con autorización explícita del investigador
  para cada intervención (`DEC-019`).
- Redacción del *texto* de una decisión metodológica ya tomada por el
  investigador: la IA formaliza y presenta el texto para aprobación antes
  de escribirlo; el investigador decide la sustancia, nunca la IA.

**Tareas que nunca se delegan en esta investigación** (ya fijado por
decisiones previas, reunido aquí sin cambiar nada):

- Cotejo de citas del corpus doctoral — 100% humano, sin excepción
  (`DEC-019`).
- Redacción de la prosa final del manuscrito o de los capítulos
  (*Human Manuscript Principle*, `ai/policy.md`).
- Elegir conclusiones filosóficas o fijar una interpretación como
  asentada.
- Validar un argumento (`human_validation: validated` — exclusivo del
  investigador).
- Decidir la sustancia de una decisión metodológica — la IA redacta,
  nunca decide qué se decide.

Registrada también en `governance/decision-log.md` (`DEC-021`).

## 10. Límites metodológicos

**DECISIÓN HUMANA REQUERIDA.** Declaración explícita de qué queda fuera del
alcance del método elegido: por ejemplo, si la reconstrucción normativa de
los ocho principios (véase `README.md`) se somete a un procedimiento de
justificación filosófica distinto del usado para la genealogía conceptual.

## Regla de cierre

Ninguna sección de este documento se completa por conjetura, plausibilidad
filosófica o para que el documento «se vea» más desarrollado. Una sección se
completa solo cuando el investigador la decide y la registra aquí, con fecha.

# PLAA — Módulo 6: fichas de consistencia conceptual — ARG-001

Cuatro fichas `concept-consistency.md` (una por término solicitado:
soberanía, potencia, hospitalidad, responsabilidad), siguiendo
`schemas/concept.schema.yaml`. Enlazadas desde
`ai/plaa/reports/ARG-001-concept-consistency.md`.

---

## Ficha 1

```yaml
term: "soberanía"
module: concept_consistency
possible_drift: POSSIBLE
human_review_required: true
```

# Consistencia conceptual — soberanía

## Apariciones

| Ubicación | Fragmento citado | Sentido aparente |
|---|---|---|
| `research/argument-ledger/ARG-001.md`, sección "Premisas" (P1) | «Derrida define la soberanía como potencia sin límite: "un poder, una potencia, un 'yo puedo'"» | Soberanía política/filosófica general: capacidad activa sin límite, sentido "clásico" definido por el propio seminario sobre la bestia y el soberano. |
| `research/argument-ledger/ARG-001.md`, sección "Afirmación (claim)" | «"Soberanía de la Hospitalidad" (…) el nombre del tránsito por el cual una potencia soberana ilimitada ("yo puedo") se convierte (…) en una no-potencia que obliga éticamente» | Aplica el sentido de P1 (potencia ilimitada) al dominio de la hospitalidad concreta, sin declarar explícitamente si se apoya también en el sentido doméstico registrado en la fila siguiente. |
| `research/sources/notes/derrida-2023-hospitality.md`, sección "Conceptos relevantes" | «Ipseidad y soberanía doméstica: ser anfitrión presupone ser soberano de la propia casa; hospitalidad y soberanía no son opuestas, están coimplicadas.» | Soberanía doméstica/ipseidad: no la potencia política general de P1, sino la posición estructural de quien recibe en su propia casa — un sentido más acotado y relacional. |
| `research/sources/notes/derrida-2010-bestia-soberano-1.md`, cita 56 (Bataille, p. 272) | «en Bataille, "la soberanía… excede la soberanía clásica, a saber, el dominio, el señorío, el poder absoluto"» | Un tercer sentido, expresamente distinguido por el propio Derrida de su propio análisis: soberanía como exceso improductivo, no como dominio. |

## Evaluación de deriva

**Veredicto:** `POSSIBLE`

**Justificación:** las filas 1 y 3 de la tabla anterior citan sentidos de
"soberanía" genuinamente distintos — potencia política general sin límite
(P1, `ARG-001.md`) frente a soberanía doméstica/ipseidad ligada
específicamente a la posición de anfitrión (`derrida-2023-hospitality.md`).
`ARG-001.md` construye su premisa 1 y su claim explícitamente sobre el
primer sentido (fila 1), pero el propio nombre de la claim
("Soberanía de la *Hospitalidad*", fila 2) evoca temáticamente el segundo
sentido (soberanía del anfitrión) sin declarar si lo está usando también o
sigue apoyándose solo en el primero. No se trata necesariamente de un
error: podría ser una especificación legítima del sentido general de P1 al
dominio de la hospitalidad. Pero el argumento no lo aclara explícitamente,
y esa falta de aclaración es una laguna citable, distinta de la fila 4
(Bataille), que es un contraste **entre autores/lecturas** ya señalado y
matizado por el propio Derrida — no una deriva del argumento del
investigador. Fila 4 se registra aquí solo como contexto: no participa del
veredicto `POSSIBLE`, que se apoya únicamente en las filas 1 y 2 (deriva
dentro del argumento del investigador, no contraste entre autores).

---

## Ficha 2

```yaml
term: "potencia / poder"
module: concept_consistency
possible_drift: POSSIBLE
human_review_required: true
```

# Consistencia conceptual — potencia / poder

## Apariciones

| Ubicación | Fragmento citado | Sentido aparente |
|---|---|---|
| `research/argument-ledger/ARG-001.md`, sección "Premisas" (P1) | «"un poder, una potencia, un 'yo puedo'"» (p. 306/352) | Potencia activa, sin límite, en primera persona — capacidad plena de un sujeto soberano. |
| `research/argument-ledger/ARG-001.md`, sección "Premisas" (P3) | «"Being able to suffer is no longer a power; it is a possibility without power"» (p. 27) | Potencia negada/ausente en un sujeto paciente (capacidad de sufrir descrita como "posibilidad sin poder") — voz distinta (tercera persona/pasiva), sentido opuesto en valencia al de P1. |
| `research/sources/notes/derrida-2010-bestia-soberano-1.md`, cita 13 (Nietzsche, p. 22) | «"tienes el poder (Macht) y no quieres reinar (du willst nicht herrschen)"» | Un tercer sentido: poder poseído pero voluntariamente no ejercido — ni la potencia plena de P1 ni la ausencia de poder de P3. |
| `research/sources/notes/derrida-2010-bestia-soberano-1.md`, cita 56 (Bataille, p. 272) | «"la soberanía… excede… el poder absoluto"» | Un cuarto sentido: exceso que sobrepasa el poder, no coincide ni con "potencia ilimitada" (P1) ni con "ausencia de poder" (P3). |

## Evaluación de deriva

**Veredicto:** `POSSIBLE`

**Justificación:** P1 y P3 de `ARG-001.md` usan "poder"/"potencia" en
sentidos que la propia ficha (`ARG-001.md`, "Objeciones y respuestas",
objeción de origen `IA-2026-08-08-09`) ya reconoce como estructuralmente
distintos («son estructuras gramaticalmente distintas (voz pasiva vs.
primera persona activa)»). Este hallazgo del módulo 6 corrobora, desde el
ángulo de consistencia conceptual (no de falacia formal — ver
`ARG-001-fallacy-analyzer.md` para el hallazgo de posible equivocación
sobre el mismo material), que "poder" no se usa de forma unívoca entre P1
y P3 dentro del propio argumento. Las citas 13 y 56 de
`derrida-2010-bestia-soberano-1.md` no participan del veredicto de deriva
(pertenecen a Bataille y a una lectura de Nietzsche que Derrida comenta,
no al uso del propio `ARG-001.md`); se listan como contexto que muestra
que el corpus de fuentes trabaja con más de dos sentidos de "poder", lo
que hace más plausible, no menos, que la homologación P1/P3 dentro de
`ARG-001` requiera justificación explícita que todavía no está escrita.

---

## Ficha 3

```yaml
term: "hospitalidad"
module: concept_consistency
possible_drift: POSSIBLE
human_review_required: true
```

# Consistencia conceptual — hospitalidad

## Apariciones

| Ubicación | Fragmento citado | Sentido aparente |
|---|---|---|
| `research/argument-ledger/ARG-001.md`, sección "Premisas" (P2) | «Derrida define el límite empírico de la hospitalidad concreta por su reverso exacto: "I am not able, therefore I ought"» | Hospitalidad en su polo condicional/finito: el límite empírico de lo que un anfitrión puede ofrecer. |
| `research/argument-ledger/ARG-001.md`, sección "Afirmación (claim)" | «"Soberanía de la Hospitalidad" (…) Extendido más allá de lo humano (…) es la tarea que una comunidad política interespecie tendría que realizar.» | Uso más amplio y programático, sin especificar si "hospitalidad" en la claim remite solo al polo condicional citado en P2 o a la estructura aporética completa (condicional + incondicional) que la propia fuente describe. |
| `research/sources/notes/derrida-2023-hospitality.md`, sección "Tesis y propósito de la obra" | «entre una **hospitalidad condicional** (…) y una **hospitalidad incondicional**, abierta sin reserva al recién llegado. (…) No es una dialéctica resoluble en síntesis: es una aporía en sentido estricto.» | La fuente citada define "hospitalidad" como una estructura de dos polos irreductibles, no como un término unívoco. |

## Evaluación de deriva

**Veredicto:** `POSSIBLE`

**Justificación:** `ARG-001.md` solo cita explícitamente, en su respaldo
textual (P2), el polo condicional/finito de la hospitalidad («I am not
able, therefore I ought», p. 232) — la propia ficha de fuente
(`derrida-2023-hospitality.md`) advierte que ese polo no es la
hospitalidad en sí, sino uno de sus dos términos aporéticos, y que
tratarlos como resolubles en síntesis traicionaría el gesto derrideano
(«no se resuelve — se sostiene»). La claim de `ARG-001.md`, al hablar de
"hospitalidad" en un sentido más amplio y programático (extendida a lo
no-humano, como tarea de una comunidad política), no aclara si sigue
refiriéndose solo al polo condicional ya citado o convoca también el polo
incondicional que P2 no cita. No se afirma que esto sea un error: podría
ser una elección deliberada de trabajar solo con el polo condicional, dado
que es el que sostiene la figura "no puedo, por tanto debo" central al
argumento — pero esa elección no está declarada como tal en el texto.

---

## Ficha 4

```yaml
term: "responsabilidad"
module: concept_consistency
possible_drift: NOT_DETECTED
human_review_required: true
```

# Consistencia conceptual — responsabilidad

## Apariciones

| Ubicación | Fragmento citado | Sentido aparente |
|---|---|---|
| `research/argument-ledger/ARG-001.md` (todas las secciones) | — | **Sin apariciones.** El término "responsabilidad" no aparece en ningún lugar de `ARG-001.md` (verificado por búsqueda literal en esta sesión). |
| `research/sources/notes/derrida-2023-hospitality.md`, líneas 19, 372, 396, 398 | «del ciclo mayor "Cuestiones de responsabilidad"» / «(decisión y responsabilidad): "no puedo, por tanto debo" (…) formulaciones directas de una soberanía/responsabilidad obligada» | Usado como título del ciclo institucional de seminarios y como etiqueta de la pregunta `PI-07`, no como concepto definido dentro de la propia ficha de fuente. |
| `research/sources/notes/derrida-2010-bestia-soberano-1.md`, línea 501 | «PI-07 (decisión y responsabilidad): la soberanía como "yo puedo" (…)» | Mismo uso: etiqueta de pregunta de investigación, no definición propia. |

## Evaluación de deriva

**Veredicto:** `NOT_DETECTED`

**Justificación:** no hay evidencia de deriva ni de consistencia que
evaluar, porque el término no aparece en el objeto auditado
(`ARG-001.md`). Este `NOT_DETECTED` reporta **ausencia de datos**, no
verificación de uso consistente — no debe leerse como «el argumento usa
"responsabilidad" de forma correcta», sino como «el argumento no usa este
término en absoluto», pese a que el propio contenido normativo del
argumento («obliga éticamente», «debo») es temáticamente adyacente a la
responsabilidad y a la pregunta `PI-07` que la ficha declara relacionada
en su cabecera. Se señala como posible vacío terminológico a considerar
por el investigador, no como hallazgo de deriva (no hay al menos dos
apariciones con `quoted_context` distinto que lo permitan, por regla del
propio `concept.schema.yaml`).

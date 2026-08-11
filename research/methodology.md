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

**DECISIÓN HUMANA REQUERIDA.** Criterios explícitos para incluir o excluir
una obra del corpus: ¿centralidad del autor en la pregunta de investigación,
disponibilidad de edición verificable, existencia de traducción autorizada,
límite temporal o de escuela filosófica? El README actual nombra autores de
referencia (Bodin, Hobbes, Schmitt, Kant, Lévinas, Derrida, Heidegger,
Agamben, Nancy, Esposito, Donaldson y Kymlicka), pero **eso no constituye
todavía un criterio de selección justificado por escrito**.

Existe una propuesta de arquitectura de corpus (200 candidatos, seis
categorías funcionales más una ampliación 2020–2026) en
[`research/sources/library-manifest.md`](sources/library-manifest.md). Es un punto de
partida para esta decisión, no su resolución: ningún candidato de ese mapa
ha sido verificado en edición ni leído, y los criterios de inclusión que
implícitamente usa (centralidad en el «giro político» animal, cercanía a
Derrida, recencia 2020–2026) siguen pendientes de ratificación explícita
por el investigador.

## 3. Fuentes primarias y secundarias

**DECISIÓN HUMANA REQUERIDA.** Regla explícita para distinguir lectura
primaria de secundaria en este proyecto, y condiciones bajo las cuales una
fuente secundaria puede sostener una premisa (¿nunca por sí sola?, ¿solo con
respaldo adicional?).

## 4. Procedimiento de lectura cercana (close reading)

**DECISIÓN HUMANA REQUERIDA.** Protocolo concreto: ¿qué se registra de cada
sesión de lectura (edición, páginas, fecha), cómo se distingue paráfrasis de
cita, cuándo se considera «leído» un pasaje frente a simplemente
«consultado»?

## 5. Disputas de interpretación

**DECISIÓN HUMANA REQUERIDA.** Cuando dos lecturas plausibles de un mismo
pasaje entran en conflicto, ¿cómo se documenta la disputa? ¿Se registra como
objeción dentro de la ficha de argumento, como nota de lectura alternativa,
o ambas?

## 6. Traducciones

**DECISIÓN HUMANA REQUERIDA.** ¿Se cita en el idioma original con traducción
propia, se usa una traducción publicada y autorizada, o ambas con nota de
discrepancia? Esto debe fijarse antes de la primera cita textual del corpus,
no caso por caso.

## 7. Verificación de citas

Ya existe una regla operativa mínima: toda cita textual requiere localizador
exacto y cotejo con el original antes de usarse como evidencia (véase
`RESEARCH-WORKFLOW.md`, `.claude/rules/sources.md`). **DECISIÓN HUMANA
REQUERIDA** solo en el detalle del procedimiento de cotejo: ¿verificación
directa sobre el original físico o edición digital autorizada, doble
verificación en citas centrales, etc.?

Existe además, desde 2026-08-08, herramienta (opcional, no obligatoria)
para auditar una cita ya cotejada más allá de su autenticidad —integridad
contextual, pertinencia filosófica, riesgo de extracción engañosa, fuerza
argumentativa— en [`ai/quote-audit/`](../ai/quote-audit/README.md). Esa
herramienta no resuelve ni el detalle de cotejo de esta sección ni la
sección 6 (traducciones): da soporte al procedimiento que el investigador
decida, no lo sustituye.

## 8. Papel de las objeciones

**DECISIÓN HUMANA REQUERIDA.** ¿Se exige al menos una objeción seria por
argumento antes de que pueda alcanzar el estado `READY_FOR_HUMAN_REVIEW`
(véase `templates/ficha-argumento.md`)? ¿Quién puede plantear objeciones
además del investigador (el auditor epistémico, revisores externos)?

## 9. Papel de la IA en el método

Ya regulado de forma transversal por `ai/policy.md` y
`AI-RESEARCH-PROTOCOL.md`: la IA no decide interpretación ni conclusiones.
**DECISIÓN HUMANA REQUERIDA** únicamente en el detalle metodológico de qué
tareas exploratorias se delegan de forma habitual (por ejemplo, localización
de literatura secundaria candidata, generación de objeciones de prueba) y
cuáles nunca se delegan en esta investigación en particular.

## 10. Límites metodológicos

**DECISIÓN HUMANA REQUERIDA.** Declaración explícita de qué queda fuera del
alcance del método elegido: por ejemplo, si la reconstrucción normativa de
los ocho principios (véase `README.md`) se somete a un procedimiento de
justificación filosófica distinto del usado para la genealogía conceptual.

## Regla de cierre

Ninguna sección de este documento se completa por conjetura, plausibilidad
filosófica o para que el documento «se vea» más desarrollado. Una sección se
completa solo cuando el investigador la decide y la registra aquí, con fecha.

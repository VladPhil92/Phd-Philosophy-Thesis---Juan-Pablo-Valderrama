# Ejemplo de extremo a extremo (ficticio)

> **Todo el contenido de este archivo es ficticio.** No corresponde a
> ningún `ARG-*` real del repositorio, a ninguna fuente real, ni a
> ninguna posición filosófica atribuida a Juan Pablo Valderrama. Su único
> propósito es mostrar la forma que debe tener un análisis PLAA completo
> antes de que exista el primer argumento sustantivo real. Corresponde a
> la ficha ficticia `ARG-900001` (identificador fuera de rango a propósito)
> usada también en `tests/fixtures/ARG-EXAMPLE-000.md`.

## Argumento auditado (ficticio)

**Afirmación:** «La hospitalidad ficticia F implica una responsabilidad
ficticia R.»

**Premisas:**

1. Toda hospitalidad ficticia F presupone una apertura al otro.
2. Toda apertura al otro genera una responsabilidad ficticia R.

## Módulo 1 — Argument Miner

| Tipo | Texto | Sección |
|---|---|---|
| CLAIM | «La hospitalidad ficticia F implica una responsabilidad ficticia R.» | Afirmación (claim) |
| PREMISE | «Toda hospitalidad ficticia F presupone una apertura al otro.» | Premisas |
| PREMISE | «Toda apertura al otro genera una responsabilidad ficticia R.» | Premisas |
| DISTINCTION | «Una lectura alternativa ficticia sostendría que R no se sigue necesariamente de la apertura, sino de una decisión posterior.» | Interpretaciones alternativas |
| OBJECTION | «Objeción ficticia: la premisa 2 no está demostrada de forma general. Respuesta ficticia: se restringe el alcance…» | Objeciones y respuestas |

Producido de forma determinista por `plaa.miner.mine_argument_file`.

## Módulo 5 — Fallacy Analyzer (informe de análisis)

```yaml
argument_id: ARG-900001
module: fallacy_analyzer
logical_status: INCOMPLETE
confidence: POSSIBLE
human_review_required: true
report_status: DEVELOPMENT_REQUIRED
```

**Falacias evaluadas (extracto, resto `NOT_DETECTED`):**

| Falacia | Veredicto | Justificación |
|---|---|---|
| Petición de principio | `POSSIBLE` | La premisa 2 («toda apertura al otro genera R») y la afirmación («F implica R») son estructuralmente próximas; no está claro si la premisa 2 se sostiene independientemente de la conclusión o la presupone. Ver `research/argument-ledger/ARG-EXAMPLE-000.md#Premisas` (ficticio). |
| Generalización apresurada | `UNLIKELY` | El propio argumento restringe su alcance en la sección «Alcance y límites» (ficticia); el cuantificador universal de la premisa 1 podría matizarse, pero el texto ya reconoce el límite. |

**Capa de seguridad hermenéutica:** para la fila «Petición de principio»,
se consideró si la proximidad entre premisa 2 y conclusión podría ser una
explicitación deliberada de un círculo hermenéutico en vez de un error.
`reviewed_as_possible_aporia: true`. Se mantiene `POSSIBLE` (no se sube a
`LIKELY`) porque el texto ficticio no ofrece señales claras de que la
circularidad sea intencional.

## Módulo 7 — Argument Stress Test (extracto)

**Mejor objeción posible (ficticia):** la apertura al otro (premisa 1)
podría generar una responsabilidad *distinta* de R —por ejemplo, una mera
disposición a escuchar sin compromiso normativo alguno—, en cuyo caso la
premisa 2 sería falsa tal como está formulada.

**Confianza:** `POSSIBLE`. **Revisión humana requerida:** sí (siempre).

## Qué NO hace este ejemplo

No emite ningún estado `VALIDATED`. No decide si el argumento ficticio es
correcto. No sustituye la lectura del investigador. Un informe real,
aplicado a un `ARG-*` sustantivo, seguiría exactamente esta forma pero con
contenido filosófico genuino, revisado por Juan Pablo Valderrama antes de
tener cualquier efecto sobre el estado epistémico del argumento.

---
reconstruction_id: FORM-ARG-001-01
argument_id: ARG-001
level: deontic
provisional: true
human_approved: false
---

# Reconstrucción formal de ARG-001

> Esta reconstrucción es una interpretación, no el argumento mismo
> (Principio 2 de `00-core-principles.md`). Se conserva separada del texto
> original en `research/argument-ledger/ARG-001.md`, que no se ha
> modificado ni se modificará por este informe. `provisional: true` hasta
> que el investigador cambie `human_approved` a `true` de forma explícita,
> editando este archivo directamente.

## Texto original citado

> «1. En *La bestia y el soberano, Vol. I*, Derrida define la soberanía
> como potencia sin límite: "un poder, una potencia, un 'yo puedo'" (p.
> 306, retomado p. 352). 2. En *Hospitality, Volume I*, Derrida define el
> límite empírico de la hospitalidad concreta por su reverso exacto: "I
> am not able, therefore I ought" (p. 232). 3. En *The Animal That
> Therefore I Am*, el giro benthamita (…) produce la misma estructura
> aplicada al viviente no-humano: "Being able to suffer is no longer a
> power; it is a possibility without power" (p. 27). 4. Las tres fuentes
> pertenecen al mismo ciclo institucional de seminarios (…)» y, de la
> sección "Inferencia": «De 1–3: (…) una potencia sin límite (…) es lo que
> un sujeto ético *no tiene* respecto de aquello a lo que debe responder,
> y es precisamente esa carencia (…) la que genera la obligación (…). De
> 4: (…) esta coincidencia estructural es más plausible como matriz de
> pensamiento deliberada (…) que como semejanza casual (…). **Paso no
> demostrado, señalado explícitamente:** de la coincidencia estructural
> (…) a la afirmación normativa de que la "Soberanía de la Hospitalidad"
> *debería* nombrarse como ese tránsito (la claim) hay un salto que
> ninguna de las tres fuentes da por sí sola (…)».

## Notación

Nivel: **deontic**, con componentes propositionales y de predicados.

**Justificación del nivel elegido:** el movimiento central del argumento
— «I am not able, therefore I ought» (P2) y su generalización a P1 y P3 —
es literalmente una fórmula deóntica (de la ausencia de capacidad se
deriva una obligación), no solo una implicación material. Un nivel
puramente proposicional perdería precisamente esa estructura, que es lo
que el argumento afirma compartir entre los tres dominios.

**Predicados y dominios:**

- Dominios: `S` (soberanía, `derrida-2010-bestia-soberano-1`), `H`
  (hospitalidad, `derrida-2023-hospitality`), `A` (ética animal,
  `derrida-2008-animal`).
- `Pow(x)`: x se define por una potencia/capacidad sin límite («yo
  puedo»).
- `Can(x)`: el sujeto ético x puede (respecto de aquello a lo que debe
  responder).
- `Ought(x)`: x está obligado éticamente.
- `PossWithoutPow(x)`: x es «una posibilidad sin poder» (formulación de
  P3, gramaticalmente distinta de `¬Can(x)`; ver «Decisiones de
  formalización»).
- `Inst(S, H, A)`: las tres fuentes pertenecen al mismo ciclo
  institucional / son contemporáneas entre sí (premisa biográfico-editorial,
  no lógica).
- `M`: la matriz estructural común, definida como
  `M := λx. (¬Can(x) → Ought(x))`.
- `Instantiates(D, M)`: el dominio D instancia la matriz M.
- `Deliberate(M)` / `Coincidental(M)`: predicados contrarios sobre el
  estatuto de M (matriz de pensamiento deliberada o coincidencia
  retórica casual — esta disyunción retoma literalmente la primera
  interpretación alternativa del propio `ARG-001.md`).
- `Name(c, M)`: el concepto c ("Soberanía de la Hospitalidad") se nombra
  correctamente como M.
- `NP` (principio de nominación, **no formulado por el texto** — ver
  «Premisa faltante»): un principio no explícito del tipo «una matriz
  estructural que se muestra deliberada a través de un mismo proyecto de
  pensamiento tardío justifica nombrar un concepto normativo nuevo en su
  honor».

## Reconstrucción

```text
P1: Pow(S)                                  [cita p. 306/352]
P2: ¬Can(H) → Ought(H)                      [cita p. 232, "I am not able, therefore I ought"]
P3: PossWithoutPow(A)                       [cita p. 27]
P4: Inst(S, H, A)                           [premisa biográfico-editorial]

--- inferencia intermedia (declarada por el propio texto como abductiva/plausibilidad,
    NO como entailment deductivo — ver "Decisiones de formalización") ---

De P1, P2, P3 (por analogía estructural, no por deducción formal):
  I1: Instantiates(S, M) ∧ Instantiates(H, M) ∧ Instantiates(A, M)
       donde M := λx.(¬Can(x) → Ought(x))

De P4 (inferencia de plausibilidad, explícitamente no necesaria):
  I2: Inst(S, H, A) ⊃ [P(Deliberate(M)) > P(Coincidental(M))]
      es decir: P4 hace más plausible Deliberate(M) que Coincidental(M),
      sin excluir Coincidental(M).

--- paso no demostrado (el propio ARG-001.md lo señala así explícitamente) ---

[NP, premisa faltante, no formulada en el texto]
  NP: (Instantiates(S,M) ∧ Instantiates(H,M) ∧ Instantiates(A,M) ∧ Deliberate(M))
       → Name(SdlH, M)  para un concepto nuevo SdlH ("Soberanía de la
       Hospitalidad")

C:  De I1, I2 y NP:
    Name(SdlH, M) ∧ Extends(M, no-humano) → Task(comunidad política
    interespecie, M)
```

## Decisiones de formalización

1. **El paso de P1–P3 a I1 no es deducción, es analogía estructural
   declarada como tal por el propio texto** («la misma matriz lógica»,
   «matriz de pensamiento (…) consistente»). Formalizarlo con `⊢` o `→`
   estrictos traicionaría el texto, que en ningún momento presenta esto
   como entailment lógico entre las tres citas — de ahí la notación
   explícita "por analogía estructural, no por deducción formal" en vez de
   un operador de inferencia estándar.
2. **`¬Can(x)` (P2, hospitalidad) y `PossWithoutPow(x)` (P3, animal) se
   formalizan como predicados distintos, no como el mismo predicado
   negado.** Esta es una decisión deliberada, no un descuido: la propia
   ficha registra una objeción (OBJ2 en `ARG-001-miner.md`) que señala que
   «poder sufrir» es una capacidad pasiva y «no poder recibir a todos» es
   una limitación activa del anfitrión — voz pasiva frente a primera
   persona activa. Colapsar ambos predicados en uno solo (`¬Can`) para
   simplificar la notación habría ocultado formalmente la objeción más
   fuerte que el propio argumento ya reconoce contra sí mismo. Se prefiere
   la notación menos elegante que preserva esa distinción.
3. **El estatuto modal de I2 (plausibilidad, no necesidad) se preserva
   explícitamente** con notación probabilística informal (`P(...)`) en vez
   de un operador modal `◇`/`□` que sugeriría una relación lógica más
   fuerte que la que P4 (un dato biográfico-editorial) puede sostener por
   sí sola. Esto refleja directamente la objeción OBJ1 ya registrada en el
   propio `ARG-001.md`.
4. **Se pierde en la formalización:** el tono («*yo puedo*» entre
   comillas, con la ironía derrideana que eso implica sobre la propia
   suficiencia del sujeto soberano), el «quizás»/incertidumbre modal que
   otras fuentes del corpus (`derrida-2010-bestia-soberano-1.md`, cita 39)
   asocian a Derrida tardío, y la diferencia de género textual entre una
   definición de seminario (P1), una nota de sesión (P2) y una fórmula de
   conferencia (P3) — la notación las trata como enunciados
   equivalentes en estatus epistémico, cuando el propio corpus las
   distingue.
5. **`NP` no es una premisa inventada por esta auditoría para "completar"
   el argumento.** Se marca explícitamente como faltante y no defendida
   (ver Principio: «nunca inventes una premisa (…) para completar el
   argumento»); se formula aquí únicamente para hacer visible, en
   notación, exactamente el lugar donde el propio `ARG-001.md` ya declara
   el salto («Paso no demostrado, señalado explícitamente»). No se
   propone un contenido definitivo para `NP`; el candidato dado es
   ilustrativo de la forma que tendría que tener, no una reconstrucción de
   lo que el investigador querría decir.

## Confianza

`LIKELY` — que la reconstrucción arriba refleja con fidelidad razonable la
estructura declarada por el propio texto (incluyendo su propio
reconocimiento del salto). `POSSIBLE` en cuanto a si `NP` es exactamente
la premisa que haría falta, dado que el propio argumento no la formula ni
siquiera de forma tentativa — cualquier reconstrucción de `NP` es en sí
misma una interpretación de esta auditoría, no un hallazgo textual.

## Revisión humana

- [ ] El investigador revisó esta reconstrucción.
- [ ] El investigador la aprueba (`human_approved: true`) o la rechaza con
      comentario.

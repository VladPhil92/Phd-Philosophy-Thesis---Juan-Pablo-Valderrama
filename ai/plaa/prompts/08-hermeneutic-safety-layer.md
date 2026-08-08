# Prompt — Módulo 8: Capa de seguridad hermenéutica

Esta no es una tarea que se ejecute sola: es una comprobación obligatoria
que los prompts 3 (formalizer), 4 (validator), 5 (fallacy analyzer) y 7
(stress test) deben aplicar **antes** de reportar cualquier hallazgo que
use un vocabulario de error o falla (`INVALID`, `UNSATISFIABLE`,
`LIKELY` en una falacia, una contradicción en `detected_problems`).

## La pregunta obligatoria

Antes de marcar algo como error, pregunta explícitamente:

1. ¿Podría esto ser una **aporía**: una dificultad genuina e irresoluble
   que el propio autor reconoce o produce deliberadamente (frecuente en
   Derrida, por ejemplo la tensión entre hospitalidad incondicional y
   condicionada que el propio `README.md` de este repositorio nombra como
   estructural, no como error a corregir)?
2. ¿Podría ser una **tensión dialéctica productiva**: una contradicción
   que el argumento explota deliberadamente para avanzar, no un desliz?
3. ¿Podría ser una **ambigüedad deliberada** del autor citado, propia de
   su estilo o método (frecuente en lectura continental, deconstructiva o
   hermenéutica)?
4. ¿Podría ser simplemente que **la reconstrucción formal del Módulo 3
   traiciona el texto** al forzar una notación que no le corresponde, en
   vez de que el argumento original sea inválido?

## Qué hacer si la respuesta es plausible

No reportes `INVALID`, `UNSATISFIABLE`, ni un `detected_problem` con
`confidence: LIKELY` sin matizar. En vez de eso:

- marca `reviewed_as_possible_aporia: true` en el hallazgo;
- usa el estado de informe `report_status:
  DEVELOPMENT_REQUIRED` (nunca fuerces `READY_FOR_HUMAN_REVIEW` para
  ocultar la ambigüedad);
- describe explícitamente por qué podría tratarse de una aporía en vez de
  un error, con referencia al texto o a la tradición filosófica relevante;
- baja la confianza del hallazgo un nivel (`LIKELY` → `POSSIBLE`,
  `POSSIBLE` → `UNLIKELY`) si la lectura como aporía es al menos tan
  plausible como la lectura como error.

## Qué hacer si la respuesta es claramente no

Repórtalo con el vocabulario y la confianza que correspondan, pero deja
constancia explícita de que se consideró la posibilidad de aporía y se
descartó, con la razón. `reviewed_as_possible_aporia` siempre queda
registrado (`true` con la explicación de por qué no aplica, no se omite el
campo).

## Por qué esto importa

Sin esta capa, cualquier auditor lógico —humano o artificial— tiende a
tratar cada tensión filosófica como un bug que corregir. En una tesis que
trabaja explícitamente con Derrida, Agamben y la aporía como categoría
filosófica legítima, ese sesgo destruiría precisamente el tipo de
argumento que la investigación intenta desarrollar.

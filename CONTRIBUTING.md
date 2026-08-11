# Guía de contribución

## Autoría y responsabilidad

La tesis es obra y responsabilidad del investigador. Toda contribución debe
preservar su voz, distinguir evidencia, interpretación y texto provisional, y
respetar derechos de autor, privacidad y normas institucionales. La IA no puede
figurar como autora ni decidir la interpretación, la argumentación o las
conclusiones.

## Fuentes, evidencia y citas

- No invente referencias, citas, paginación, traducciones ni datos editoriales.
- Registre cada obra en `research/sources/bibliography.bib` y use una ficha en
  `research/sources/notes/` para la lectura analítica.
- Coteje toda cita textual con el original e incluya página, sección o párrafo.
- Distinga fuentes primarias de secundarias; no atribuya lectura directa de una
  obra a partir de un resumen, una cita indirecta, OCR o transcripción.
- Enlace cada afirmación sustantiva con una fuente comprobada o identifíquela
  claramente como hipótesis, interpretación u objeción.

Una salida de IA nunca es evidencia. Una referencia o afirmación sugerida por
IA solo puede utilizarse después de su verificación en una fuente fiable.

## Transparencia del uso de IA

Registre todo uso que influya materialmente en el corpus, análisis, estructura,
texto o código con `templates/registro-ia.md`. Indique herramienta y versión si
se conocen, propósito, salida utilizada, verificación humana, cambios y archivos
afectados. No cargue a servicios externos material protegido, privado,
confidencial o con datos personales sin autorización. Consulte
[`AI-RESEARCH-PROTOCOL.md`](AI-RESEARCH-PROTOCOL.md) y
[`ai/policy.md`](ai/policy.md).

## Flujo de trabajo del repositorio

1. Cree una rama y mantenga el cambio acotado.
2. Use nombres de archivo en minúsculas, sin espacios y separados por guiones;
   use claves bibliográficas `apellido-anio-palabra`.
3. Use las plantillas para fuentes, argumentos y registros de IA; conserve la
   trazabilidad `PI-*` → fuente → `ARG-*` → capítulo.
4. Use enlaces relativos y marque lo no resuelto con `PENDIENTE:`; no complete
   vacíos académicos mediante conjeturas.
5. No versione fuentes protegidas, bibliotecas privadas, OCR, transcripciones,
   secretos, datos sensibles o productos generados.
6. Ejecute las validaciones indicadas abajo antes de solicitar integración.
7. Describa qué cambió, su justificación o evidencia, cómo se verificó y todo
   uso relevante de IA.

## Validación y revisión

Ejecute:

```bash
python3 scripts/auditar_repositorio.py
```

La auditoría también impide versionar cachés, archivos temporales, copias de
respaldo y residuos habituales del sistema operativo o del editor. Antes de
confirmar cambios, revise además `git status --short --ignored`: los archivos
ignorados deben permanecer locales y no deben forzarse con `git add -f`.

Además, revise `git diff --check`, los enlaces Markdown, la sintaxis YAML y la
ausencia de binarios restringidos. No se integra un cambio con referencias sin
verificar, datos sensibles, conflictos sin resolver, enlaces rotos o
afirmaciones sustantivas sin fuente o justificación. Los borradores incompletos
son admisibles solo si declaran su estado.

Si el cambio toca `research/argument-ledger/**` o `ai/plaa/**`, ejecute
también `python3 -m unittest discover -s ai/plaa/tests -p "test_*.py"`. Si
toca `research/sources/**` o `ai/quote-audit/**`, ejecute
`python3 -m unittest discover -s ai/quote-audit/tests -p "test_*.py"`. Ambas
suites, junto con `auditar_repositorio.py`, corren automáticamente en cada
`push`/`pull_request` (`.github/workflows/auditoria.yml`); correrlas en local
antes de subir el cambio ahorra una vuelta de CI.

Para evaluar la integridad de un argumento (`ARG-*`) o una cita concreta más
allá de lo que valida `auditar_repositorio.py` —relevancia filosófica,
integridad contextual, fuerza argumentativa, procedencia de autoría—, delegue
en el subagente `epistemic-auditor`
(`.claude/agents/epistemic-auditor.md`); nunca simule esa auditoría usted
mismo con juicio no declarado como tal.

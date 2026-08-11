# APA 7 — reglas estructurales implementadas (y las que no)

Versión normativa del proyecto: *Publication Manual of the American
Psychological Association*, 7.ª edición. **No se inventan reglas**: lo que
sigue distingue explícitamente lo que `quote_audit/schema_check.py`
valida hoy de lo que sigue requiriendo revisión humana.

## Distinción previa: SOURCE RECORD vs. MANUSCRIPT CITATION

Una cita almacenada como evidencia interna (`research/sources/notes/**`,
sección «Citas verificadas») **no necesita todavía** la puntuación final
de manuscrito — sirve para investigación, no para publicación. Antes de
integrarse a un capítulo (`thesis/chapters/`), debe alcanzar
`recommended_status: APA7_READY`.

## Reglas implementadas (deterministas, `quote_audit/schema_check.py`)

1. **Umbral de cita en bloque.** 40 palabras o más → `apa7_quote_type`
   debe ser `block` (formato de bloque, sin comillas en la presentación
   final). Menos de 40 → `short` (integrada en el texto, con comillas).
   Si el conteo no coincide con `apa7_quote_type`, es error estructural
   (`BLOCK_QUOTE_REQUIRED`).
2. **Localizador presente.** `apa7_locator_present` debe ser verdadero
   cuando la fuente lo permite (p. ej. `p. 25`, `pp. 25–27`, `para. 4`
   según el tipo de fuente). Sin localizador, no es `APA7_READY`.
3. **Correspondencia bibliográfica.** `source` (clave BibTeX) debe
   resolver contra una entrada real de
   `research/sources/bibliography.bib`. `apa7_bibliography_entry_found`
   se deriva automáticamente de esa comprobación cuando no se declara a
   mano.
4. **Vocabulario cerrado.** `apa7_compliant` solo admite `true`, `false`
   o `partial` — ningún otro valor.

## Requiere revisión humana explícita (no implementado como regla determinista)

Estas reglas de APA 7 dependen de decisiones que `research/methodology.md`
§6 (traducciones) todavía marca `DECISIÓN HUMANA REQUERIDA`, o de datos
que este componente no puede verificar automáticamente. Se marcan
`APA7_HUMAN_REVIEW` en `risks` en vez de simularse:

- resolución exacta de `author`/`year` para citas en traducción publicada
  frente a traducción propia del investigador (pendiente de §6);
- formato de citas de fuentes con múltiples autores, sin autor, o
  institucionales;
- formato de citas indirectas (fuente secundaria citando a la primaria);
- puntuación final exacta al integrarse en la prosa del manuscrito (uso
  de comas, punto y coma, orden autor-año) — se verifica en el momento de
  integración a capítulo, no antes.

No completar ninguna de estas por plausibilidad. Si una cita necesita una
de estas reglas antes de poder llamarse `APA7_READY`, repórtalo como
`APA7_HUMAN_REVIEW`, no como `compliant: true`.

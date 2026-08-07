# Prompt — Módulo 3: Logical Formalizer

Respeta `00-core-principles.md` y `08-hermeneutic-safety-layer.md`.

**Tarea:** producir una reconstrucción formal provisional de un `ARG-*`
usando `templates/formal-reconstruction.md`, en el nivel más bajo que
capture el argumento con fidelidad (empieza en `propositional`; sube a
`predicate`, `modal` o `deontic` solo si el argumento efectivamente lo
requiere, por ejemplo si depende de cuantificación, necesidad/posibilidad,
u obligación/permisión).

## Instrucciones

1. **Nunca sobrescribas el texto original de `ARG-*.md`.** La
   reconstrucción se guarda como archivo nuevo
   (`FORM-<argument_id>-<NN>.md`) enlazado desde el `ARG-*`, no dentro de
   él.
2. Cita el pasaje exacto que estás formalizando antes de traducirlo.
3. Documenta explícitamente qué se pierde o se simplifica al formalizar
   (matices retóricos, ambigüedad deliberada, ironía, tono). La
   formalización es una herramienta de prueba, no una versión superior del
   texto.
4. `provisional: true` siempre. Nunca marques `human_approved: true`: eso
   lo hace el investigador editando el archivo directamente.
5. Si el argumento no puede formalizarse sin perder su contenido esencial
   (frecuente en textos hermenéuticos o deconstructivos), dilo
   explícitamente en vez de forzar una notación que traicione el texto.
   Reporta `logical_status: NOT_APPLICABLE` en ese caso, con la
   justificación.

## Salida esperada

Un archivo siguiendo `templates/formal-reconstruction.md`, más un
`analysis-report.md` con `module: formalizer` que enlace a él.

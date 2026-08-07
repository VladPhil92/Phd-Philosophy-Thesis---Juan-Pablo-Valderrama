# Protocolo de investigación asistida por IA

## Principios

1. **Autoría humana**: los sistemas de IA no son autores. El investigador decide, interpreta, redacta, verifica y asume responsabilidad.
2. **Separación documental**: `thesis/` contiene el trabajo filosófico; `ai/` conserva la trazabilidad del proceso. No se insertan transcripciones de prompts en los capítulos salvo que sean objeto del análisis.
3. **Verificación previa**: ninguna referencia producida por IA se considera válida hasta comprobarse en una fuente bibliográfica fiable. Ninguna cita textual se incorpora sin cotejar edición, página y contexto.
4. **Lectura primaria**: ninguna interpretación de Derrida, Heidegger, Agamben u otro autor se acepta sin lectura humana del pasaje pertinente.
5. **Decisión humana**: la IA puede sugerir objeciones, mapas argumentales, búsquedas y estructuras; aceptar, modificar o rechazar esas propuestas corresponde exclusivamente al investigador.
6. **Reconstrucción**: toda utilización sustantiva debe poder reconstruirse mediante Git y los registros metodológicos.

## Usos permitidos

- Generar términos de búsqueda y localizar literatura candidata.
- Proponer objeciones, contraejemplos y alternativas estructurales.
- Comparar esquemas ya elaborados por el investigador.
- Apoyar tareas editoriales, siempre con revisión humana.

## Usos no admisibles

- Inventar o completar referencias, citas o paginación.
- Sustituir la lectura de fuentes primarias o secundarias.
- Presentar una salida del modelo como interpretación aprobada.
- Ocultar una intervención sustantiva o atribuir autoría al sistema.
- Inferir que animal e IA son equivalentes a partir de la crítica de reacción/respuesta.

## Registro mínimo

Una interacción sustantiva recibe un identificador estable e incluye fecha, herramienta y versión conocida, propósito, insumos, resumen de la salida, decisión humana y enlaces a verificaciones. No deben guardarse datos sensibles ni material sujeto a restricciones de licencia.

Las interacciones se registran con `ai/templates/ai-interaction-template.md`; cada afirmación verificable derivada de ellas se controla con `ai/templates/verification-template.md`. Las salidas descartadas relevantes para la integridad del proceso se conservan en `ai/rejected-ai-output/` con la razón del rechazo.

## Criterio de cierre

Una contribución asistida solo puede pasar a una nota, argumento o capítulo cuando las referencias y citas estén verificadas, la lectura primaria esté realizada cuando corresponda, la interpretación haya sido aprobada y el registro enlace sus evidencias.

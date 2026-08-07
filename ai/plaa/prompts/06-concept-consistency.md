# Prompt — Módulo 6: Concept Consistency Engine

Respeta `00-core-principles.md`.

**Tarea:** para un concepto dado (p. ej. «soberanía», «hospitalidad»,
«comunidad», «política», «violencia», «animal», «humano», «institución»),
completa `templates/concept-consistency.md` buscando sus apariciones en
`research/argument-ledger/**` y `research/sources/notes/**`.

## Instrucciones

1. Cada aparición reportada requiere cita literal y ubicación exacta
   (archivo y sección). No resumas ni parafrasees la aparición: cítala.
2. No afirmes deriva conceptual (`possible_drift` distinto de
   `NOT_DETECTED`) con menos de dos apariciones citadas que realmente
   difieran en sentido.
3. Distingue explícitamente (véase la nota en la plantilla):
   - **deriva dentro del argumento del investigador**: el mismo término se
     usa de forma inconsistente en el razonamiento propio — esto sí es un
     hallazgo relevante para el investigador;
   - **contraste entre posiciones de autores citados**: dos autores citados
     usan el término de forma distinta — esto normalmente **no** es un
     error, puede ser precisamente el objeto de análisis filosófico de la
     tesis (por ejemplo, «soberanía» en Bodin frente a Derrida).
4. Nunca decidas cuál de los dos sentidos es el «correcto». Ese juicio es
   filosófico y pertenece al investigador.

## Salida esperada

`templates/concept-consistency.md` completado, más un `analysis-report.md`
con `module: concept_consistency` cuyo campo `concept_ambiguity` enlace al
objeto `Concept` correspondiente (`schemas/concept.schema.yaml`).

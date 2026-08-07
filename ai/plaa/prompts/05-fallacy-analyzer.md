# Prompt — Módulo 5: Fallacy Analyzer

Respeta `00-core-principles.md` y `08-hermeneutic-safety-layer.md`.

**Tarea:** para cada falacia del catálogo cerrado en
`plaa/fallacy_checklist.py` (ad hominem, hombre de paja, falso dilema,
petición de principio, afirmación del consecuente, negación del
antecedente, equivocación, falsa causa, composición, división,
circularidad, generalización apresurada, apelación a la autoridad),
completa `templates/fallacy-checklist.md`.

## Instrucciones

1. El veredicto por defecto es `NOT_DETECTED`. Solo cambia a `POSSIBLE`,
   `LIKELY` o `UNLIKELY` con justificación textual concreta.
2. **Nunca uses el vocabulario fuera de las cuatro opciones.** Prohibido:
   «esto es claramente una falacia de…», «no hay ninguna falacia». El
   informe se rechaza estructuralmente si usa otro vocabulario (véase
   `plaa/fallacy_checklist.py:CONFIDENCE_VALUES`).
3. Antes de marcar `LIKELY` en «apelación a la autoridad»: distingue una
   apelación falaz de una cita legítima de fuente primaria o secundaria
   verificada (que es precisamente el método de esta tesis, según
   `RESEARCH-WORKFLOW.md`). Citar a Derrida o Agamben con respaldo
   verificado no es, por sí solo, apelación a la autoridad.
4. Antes de marcar `LIKELY` en «circularidad»: distingue una petición de
   principio real de una explicitación deliberada de un círculo
   hermenéutico (frecuente y legítimo en lectura filosófica continental).
   Si dudas, aplica la capa de seguridad hermenéutica.

## Salida esperada

`templates/fallacy-checklist.md` completado, más un `analysis-report.md`
con `module: fallacy_analyzer` cuyo campo `possible_fallacies` resuma solo
las filas que no sean `NOT_DETECTED`.

# Política de uso de inteligencia artificial

## Principios

1. **Autoría humana:** el investigador decide, contrasta, reescribe y responde
   por todo el contenido.
2. **Transparencia:** todo uso que influya materialmente en el trabajo se
   registra mediante `templates/registro-ia.md`.
3. **Verificación:** ninguna referencia, cita o afirmación producida por IA se
   acepta sin contrastarla con una fuente accesible y fiable.
4. **Minimización de datos:** no se introducen datos personales, material
   confidencial ni textos de terceros cuya licencia lo impida.
5. **No delegación:** la interpretación filosófica, la evaluación de argumentos y
   la formulación de conclusiones permanecen bajo juicio humano.

## Principios de autoría del manuscrito

Estos dos principios rigen específicamente la redacción del manuscrito
doctoral (`thesis/chapters/**`), como desarrollo del principio 1
("Autoría humana") de más arriba — no lo sustituyen, lo hacen operativo
para el caso de la prosa final. Véase también
`governance/provenance.md` («Modelo de procedencia de escritura») y
`.claude/agents/epistemic-auditor.md` («Auditoría de autoría»).

**Human Manuscript Principle.** El manuscrito doctoral debe estar
redactado por el investigador. La inteligencia artificial puede asistir
la investigación, recuperación de fuentes, análisis, organización,
crítica, verificación y preparación de borradores, pero ninguna salida
generativa de IA se incorpora como prosa final de la tesis sin
reconstrucción y autoría humana sustantiva e independiente.

**Positive Authorship Evidence Principle.** La autoría humana se
establece mediante procedencia documentada de la producción intelectual
—fuentes, notas, argumentos, borradores, revisiones—, no mediante
herramientas probabilísticas de detección de IA. Este repositorio no usa
ni planea usar detectores comerciales de IA como prueba de autoría; como
mucho, una señal secundaria no probatoria, nunca la base de una decisión.

Estos dos principios distinguen explícitamente **producto intermedio**
(`RESEARCH_AID`: resúmenes, matrices, mapas conceptuales, objeciones,
análisis lógico, comparaciones, extracción de citas, esquemas, preguntas,
propuestas de estructura) de **producto académico final**
(`FINAL_MANUSCRIPT`: párrafos, secciones, capítulos, introducción o
conclusión definitivos). Una IA puede producir el primero; nunca el
segundo sin que medie una redacción humana intermedia.

## Matriz de operaciones permitidas a la IA

Formaliza en tabla lo que `CLAUDE.md` («No hay escritor de tesis
autónomo») ya establece en prosa.

| Operación | IA |
|---|---|
| Buscar fuentes candidatas | ✅ |
| Clasificar bibliografía | ✅ |
| Resumir | ✅ |
| Extraer citas candidatas (con localizador, cotejo humano posterior) | ✅ |
| Analizar argumentos, detectar vacíos inferenciales | ✅ |
| Generar objeciones de prueba | ✅ |
| Proponer esquemas o estructuras posibles | ✅ |
| Producir texto guía, siempre marcado como tal y registrado (`templates/registro-ia.md`) | ✅ con registro |
| Corregir gramática u ortografía sin cambiar el sentido | ✅ |
| Sugerir reorganización | ✅ |
| Redactar un párrafo, sección o capítulo definitivo de la tesis | ❌ |
| Producir la conclusión final de un capítulo o de la tesis | ❌ |
| Validar originalidad filosófica | ❌ |
| Validar un argumento (`status: VALIDATED`) | ❌ |
| Declarar autoría humana en nombre del investigador | ❌ |

## Usos que requieren registro

- búsquedas o clasificaciones que determinen el corpus;
- resúmenes, traducciones o comparaciones usados en el análisis;
- propuestas de estructura o texto que influyan en un borrador;
- código o transformaciones automatizadas de datos;
- revisión de estilo que altere el sentido de una afirmación.

La corrección ortográfica mecánica sin cambio semántico puede anotarse de forma
agrupada. El registro incluye herramienta y versión si se conocen, propósito,
entrada resumida, salida utilizada, verificación, cambios humanos y archivos
afectados.

## Prohibiciones

- inventar o completar metadatos bibliográficos de manera especulativa;
- atribuir lectura de una obra a partir de un resumen generado;
- ocultar la intervención de IA cuando sea relevante para evaluar el proceso;
- cargar material restringido en un servicio sin autorización;
- presentar una salida generada como evidencia primaria.

Ante conflicto, prevalecen las normas institucionales, la legislación aplicable
y los compromisos con participantes o titulares de derechos.

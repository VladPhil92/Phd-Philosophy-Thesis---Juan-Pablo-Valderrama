# Arquitectura del repositorio

## Objetivo

La arquitectura separa el material por función epistémica, no por formato de
archivo. Su propósito es permitir reconstruir cómo una afirmación del manuscrito
se relaciona con una pregunta, una fuente y una decisión analítica.

## Capas y dependencias

1. **Gobernanza (`00-gobernanza`)**: define reglas transversales y registra
   decisiones. No contiene argumentos de la tesis.
2. **Investigación (`01-investigacion`)**: formula preguntas, conceptos y
   métodos que determinan qué fuentes y análisis son pertinentes.
3. **Fuentes (`02-fuentes`)**: contiene metadatos bibliográficos y fichas de
   lectura. Es la base documental del análisis.
4. **Análisis (`03-analisis`)**: transforma evidencia y lectura crítica en
   argumentos y estudios de caso identificables.
5. **Escritura (`04-escritura`)**: integra argumentos en el manuscrito. No es
   el lugar canónico de metadatos de fuentes.
6. **Revisión (`05-revision`)**: registra controles, comentarios y respuestas
   que retroalimentan todas las capas anteriores.

`assets` sirve exclusivamente a productos del manuscrito; `plantillas` fija
campos mínimos; `scripts` comprueba invariantes estructurales. Un directorio
numérico posterior puede depender de uno anterior, pero no debe duplicarlo.

## Unidad de trazabilidad

Se emplean identificadores estables:

- preguntas: `PI-01`, `PI-02`, etc.;
- argumentos: `ARG-001`, `ARG-002`, etc.;
- registros de IA: `IA-AAAA-MM-DD-NN`;
- fuentes: clave BibTeX `apellido-anio-palabra`.

Una ficha de argumento enlaza al menos una pregunta y enumera sus fuentes. Un
capítulo se remite a argumentos por identificador. Si una ruta cambia, deben
actualizarse los enlaces, no los identificadores.

## Estados documentales

Todo documento sustantivo debe indicar uno de estos estados: `idea`,
`en desarrollo`, `en revisión` o `aprobado`. La aprobación significa revisión
humana, no verdad definitiva. Las incertidumbres se conservan de forma
explícita en vez de resolverse mediante texto especulativo.

## Cambios de arquitectura

Una modificación estructural requiere: motivación, impacto sobre rutas y
trazabilidad, plan de migración y una entrada en `registro-decisiones.md`. La
automatización valida la presencia de piezas mínimas, pero la calidad filosófica
continúa siendo objeto de revisión humana.

# Soberanía de la hospitalidad y comunidad política interespecie

Repositorio de investigación doctoral en Filosofía de Juan Pablo Valderrama. El
proyecto estudia la **soberanía de la hospitalidad** y las condiciones de una
comunidad política interespecie.

El repositorio organiza fuentes, notas, argumentos, borradores y decisiones
metodológicas. La inteligencia artificial puede apoyar tareas de búsqueda,
análisis, organización y redacción, pero no es la autora de la tesis ni sustituye
la interpretación, la verificación o la responsabilidad académica del
investigador.

## Estado del proyecto

La infraestructura documental está preparada y todavía no contiene resultados
de investigación ni capítulos sustantivos. La auditoría inicial, sus hallazgos y
las decisiones adoptadas se documentan en
[`00-gobernanza/auditoria-inicial.md`](00-gobernanza/auditoria-inicial.md).

## Arquitectura del repositorio

El flujo de conocimiento va de las preguntas y fuentes hacia el análisis, la
escritura y la revisión:

```text
00-gobernanza/   normas, decisiones, auditorías y uso de IA
01-investigacion/ preguntas, conceptos y metodología
02-fuentes/      bibliografía y fichas verificables
03-analisis/     mapas argumentales y casos
04-escritura/    esquema, capítulos y anexos
05-revision/     retroalimentación y control de calidad
assets/          figuras y otros recursos del manuscrito
plantillas/      formatos reutilizables
scripts/         comprobaciones automatizadas
library/         biblioteca doctoral local y materiales de trabajo no versionados
tools/library/   herramientas y salidas generadas para procesar la biblioteca
```

Cada directorio documental contiene un `README.md` que define su alcance. La
explicación de las capas, sus dependencias y las convenciones de trazabilidad
está en [`00-gobernanza/arquitectura.md`](00-gobernanza/arquitectura.md). La
biblioteca local complementa esas capas: conserva los documentos de consulta y
sus derivados operativos, mientras que `02-fuentes/` mantiene los metadatos y
las fichas que sí forman parte del registro académico versionado.

## Biblioteca doctoral y flujo de OCR

Cuando se utilice `library/`, cada obra puede disponer de un espacio propio para
el original en `source/`, resultados de OCR en `ocr/` y transcripciones en
`transcription/` o `transcriptions/`. Estos materiales son insumos locales, no
evidencia validada por el mero hecho de haber sido procesados. Las salidas
automatizadas de las herramientas se guardan en `tools/library/output/`.

Los originales, los textos protegidos, los archivos privados y los derivados de
OCR o transcripción no se versionan. Las reglas de `.gitignore` protegen esas
rutas, pero no reemplazan la comprobación de derechos, confidencialidad y
permisos antes de incorporar cualquier material. El flujo recomendado es:

1. Conservar el original autorizado en la carpeta local `source/` de la obra.
2. Ejecutar OCR o transcripción sin modificar el original y mantener la salida
   en las rutas privadas correspondientes.
3. Revisar el resultado contra el documento fuente; registrar errores,
   paginación y decisiones de corrección relevantes.
4. Registrar los metadatos en `02-fuentes/bibliografia.bib` y elaborar una ficha
   verificable en `02-fuentes/fichas/`, sin copiar material restringido.
5. Citar y analizar la fuente comprobada, no una salida automática sin revisar.

## Metodología y trazabilidad

Las preguntas de investigación orientan la selección de fuentes; las fichas
distinguen datos bibliográficos, notas de lectura y citas verificadas; y los
argumentos enlazan preguntas y fuentes mediante identificadores estables. Los
borradores integran esos argumentos y la revisión documenta observaciones y
respuestas. Las incertidumbres, limitaciones y desacuerdos se registran en vez
de resolverse mediante inferencias no comprobadas.

El diseño metodológico se mantiene en
[`01-investigacion/metodologia.md`](01-investigacion/metodologia.md), y las
convenciones completas de trazabilidad se describen en el documento de
arquitectura. La presencia de una fuente en la biblioteca, una transcripción o
un resumen no acredita por sí sola su lectura, pertinencia ni validez.

## Flujo de investigación asistido por IA

La IA puede facilitar búsquedas exploratorias, clasificación, comparación,
resumen, revisión de estilo y automatización. Toda contribución material debe
registrarse y verificarse contra fuentes fiables. No se deben cargar a servicios
externos textos restringidos, datos personales ni material confidencial sin
autorización.

La interpretación filosófica, la selección de evidencia, la evaluación de
argumentos, la redacción final y las conclusiones corresponden al investigador.
Consulte la [`política de IA`](00-gobernanza/politica-ia.md) y documente los usos
relevantes con `plantillas/registro-ia.md`.

## Inicio rápido

1. Formular o actualizar preguntas en `01-investigacion/preguntas.md`.
2. Registrar cada obra en `02-fuentes/bibliografia.bib` y crear su ficha desde
   `plantillas/ficha-fuente.md`.
3. Vincular los argumentos con sus fuentes y preguntas de investigación.
4. Redactar en `04-escritura/capitulos/`, sin incorporar texto generado por IA
   sin revisión y registro.
5. Ejecutar la auditoría estructural antes de integrar cambios:

   ```bash
   python3 scripts/auditar_repositorio.py
   ```

## Contribución y responsabilidad

Consulte [`CONTRIBUTING.md`](CONTRIBUTING.md) antes de proponer cambios. No deben
versionarse datos personales, material protegido sin permiso, exportaciones
completas de gestores bibliográficos, archivos temporales de editores ni
productos privados o generados de la biblioteca doctoral.

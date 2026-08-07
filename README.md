# Soberanía de la hospitalidad y comunidad política interespecie

Repositorio de investigación doctoral en Filosofía de Juan Pablo Valderrama. El
proyecto estudia la **soberanía de la hospitalidad** y las condiciones de una
comunidad política interespecie.

Este repositorio organiza fuentes, notas, argumentos, borradores y decisiones
metodológicas. La inteligencia artificial puede apoyar tareas de búsqueda,
análisis y redacción, pero no sustituye la autoría, la verificación ni la
responsabilidad académica humanas.

## Estado del proyecto

La infraestructura documental está preparada y todavía no contiene resultados
de investigación ni capítulos sustantivos. La auditoría inicial, sus hallazgos y
las decisiones adoptadas se documentan en
[`00-gobernanza/auditoria-inicial.md`](00-gobernanza/auditoria-inicial.md).

## Arquitectura

El flujo de conocimiento va de las preguntas y fuentes hacia el análisis, la
escritura y la revisión:

```text
00-gobernanza/  normas, decisiones, auditorías y uso de IA
01-investigacion/ preguntas, conceptos y metodología
02-fuentes/     bibliografía y fichas verificables
03-analisis/    mapas argumentales y casos
04-escritura/   esquema, capítulos y anexos
05-revision/    retroalimentación y control de calidad
assets/         figuras y otros recursos del manuscrito
plantillas/     formatos reutilizables
scripts/        comprobaciones automatizadas
```

Cada directorio contiene un `README.md` que define su alcance. La explicación
completa de las capas, sus dependencias y las convenciones de trazabilidad está
en [`00-gobernanza/arquitectura.md`](00-gobernanza/arquitectura.md).

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

Consulte [`CONTRIBUTING.md`](CONTRIBUTING.md) antes de proponer cambios y la
[`política de IA`](00-gobernanza/politica-ia.md) antes de utilizar herramientas
generativas. No deben versionarse datos personales, material protegido sin
permiso, exportaciones completas de gestores bibliográficos ni archivos
temporales de editores.

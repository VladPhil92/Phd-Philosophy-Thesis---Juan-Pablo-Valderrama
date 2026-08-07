# Guía de contribución

## Principios

- Conservar la voz y la responsabilidad autoral del investigador.
- Diferenciar evidencia, interpretación propia y texto provisional.
- No inventar referencias, citas, paginación ni datos editoriales.
- Mantener trazabilidad entre pregunta, fuente, argumento y capítulo.
- Respetar derechos de autor, privacidad y requisitos institucionales.

## Flujo de trabajo

1. Trabajar en una rama con un cambio acotado.
2. Usar las plantillas del repositorio para nuevas fuentes, argumentos y
   registros de IA.
3. Emplear nombres de archivo en minúsculas, sin espacios y separados por
   guiones; conservar las claves bibliográficas en formato
   `apellido-anio-palabra`.
4. Enlazar rutas relativas y marcar contenidos incompletos con `PENDIENTE:`.
5. Ejecutar `python3 scripts/auditar_repositorio.py`.
6. Explicar en la propuesta qué cambió, qué evidencia lo respalda y cómo se
   verificó. Si hubo IA, enlazar su registro.

## Citas y fuentes

Cada ficha debe corresponder a una entrada de `02-fuentes/bibliografia.bib`.
Las citas textuales requieren localizador (página, sección o párrafo) y una
comprobación contra el original. Las fuentes secundarias no deben presentarse
como lectura directa de una fuente primaria.

## Revisión

No se integra un cambio si contiene referencias no verificadas, datos sensibles
o afirmaciones sustantivas sin fuente o justificación. Los borradores pueden
estar incompletos, pero deben declarar su estado.

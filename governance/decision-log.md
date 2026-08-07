# Registro de decisiones

## DEC-001 — Arquitectura por función epistémica

- **Fecha:** 2026-08-07
- **Estado:** aceptada
- **Contexto:** el repositorio no distinguía fuentes, análisis, escritura y
  controles, lo cual impedía demostrar procedencia.
- **Decisión:** adoptar las seis capas numeradas descritas en `arquitectura.md`
  y conservar recursos auxiliares fuera de ellas.
- **Consecuencias:** las rutas comunican el papel de cada documento; cualquier
  migración futura debe mantener los identificadores y actualizar enlaces.

## DEC-002 — Consolidación en arquitectura semántica

- **Fecha:** 2026-08-07
- **Estado:** aceptada
- **Contexto:** dos arquitecturas paralelas duplicaban gobernanza, investigación,
  escritura y plantillas.
- **Decisión:** adoptar `governance/`, `research/`, `thesis/`, `ai/` y
  `templates/` como rutas canónicas; migrar mediante renombres todos los archivos
  sustantivos de las capas numeradas.
- **Consecuencias:** existe una sola ubicación por función; se actualizaron
  enlaces, auditoría y documentación sin alterar los identificadores.

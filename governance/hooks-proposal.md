# Propuesta de hooks de Claude Code (no activados)

**Estado:** propuesta, no implementada. Ningún hook descrito aquí está
configurado en `.claude/settings.json`. No se activa nada automáticamente
por la existencia de este documento.

## Por qué no se activan todavía

Un hook `PreToolUse` mal calibrado puede bloquear trabajo legítimo del
investigador (por ejemplo, un `Write` en `thesis/` que sí cuenta con
respaldo argumental) o dar una falsa sensación de seguridad si sus reglas
son demasiado permisivas. Antes de imponer un hook obstructivo hace falta
probarlo en modo de solo advertencia y documentar sus falsos positivos.

## Candidatos propuestos

### 1. Bloquear binarios de biblioteca protegidos

- **Evento:** `PreToolUse` sobre `Write`/`Edit`.
- **Regla:** rechazar rutas que coincidan con `*.pdf`, `*.epub`, `*.djvu`,
  `*.mobi` fuera de `assets/` con licencia documentada.
- **Motivación:** `.gitignore` ya excluye estas rutas del control de
  versiones, pero un hook añadiría una segunda barrera explícita en el
  momento de la escritura, no solo en el commit.

### 2. Advertir sobre escritura en `thesis/` sin `ARG-*` de respaldo

- **Evento:** `PreToolUse` sobre `Write`/`Edit` en `thesis/chapters/**`.
- **Regla:** si el contenido añadido no menciona ningún identificador
  `ARG-*` existente, emitir advertencia (no bloqueo duro) recordando la regla
  de `.claude/rules/thesis.md`.
- **Motivación:** detectar temprano texto de capítulo sin trazabilidad,
  sin impedir borradores exploratorios que el investigador marque como tales.

### 3. Proteger archivos de gobernanza de borrado

- **Evento:** `PreToolUse` sobre `Bash` cuando el comando contiene `rm` y una
  ruta bajo `governance/` o `CLAUDE.md`.
- **Motivación:** estos archivos son la constitución operativa del
  repositorio; su borrado accidental debe requerir confirmación explícita
  fuera del flujo normal de edición.

### 4. Advertir sobre cambios en `research/questions.md`

- **Evento:** `PreToolUse` sobre `Edit`/`Write` en `research/questions.md`.
- **Regla:** advertir (no bloquear) que cualquier cambio de identificador
  `PI-*` o de alcance de una pregunta requiere instrucción humana explícita,
  según `CLAUDE.md`.

## Condición para activar cualquiera de estos hooks

1. Redactar la configuración exacta en `.claude/settings.json` (o
   `.claude/settings.local.json`) por separado de este documento.
2. Probarla en modo de advertencia (log, sin bloqueo) durante uso real.
3. Registrar aquí los falsos positivos observados y ajustar la regla.
4. Solo entonces convertir la advertencia en bloqueo, con acuerdo explícito
   del investigador.

Ninguna sesión de Claude Code debe activar estos hooks de forma autónoma.

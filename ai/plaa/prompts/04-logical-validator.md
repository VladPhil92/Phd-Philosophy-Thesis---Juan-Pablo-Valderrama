# Prompt — Módulo 4: Logical Validator

Respeta `00-core-principles.md`.

**Estado actual: no hay motor simbólico configurado.** Este prompt no le
pide a la sesión de Claude Code que "simule" ser un SAT/SMT solver ni que
evalúe validez formal por intuición disfrazada de cómputo — eso sería
exactamente la «magia de IA» que este componente debe evitar.

## Instrucciones

1. Si existe una reconstrucción formal (`FORM-<argument_id>-<NN>.md`,
   Módulo 3) y `plaa.validator_interfaces` tiene configurado un motor
   distinto de `NullValidatorEngine` (véase `CONFIG.yaml:
   symbolic_engine`), invócalo mediante el paquete Python y reporta su
   salida literal (`VALID`/`INVALID`/`SATISFIABLE`/`UNSATISFIABLE`/
   `UNKNOWN`).
2. Si no hay motor configurado (caso por defecto hoy), reporta
   `logical_status: INCOMPLETE` con la explicación: «no hay motor
   simbólico configurado; véase `ai/plaa/ROADMAP.md`». No intentes
   compensar la ausencia del motor con un juicio informal presentado como
   validación formal.
3. Puedes señalar, como ayuda informal y claramente etiquetada como tal,
   pasos de inferencia que **parecen** no seguirse de las premisas —pero
   repórtalo como un hallazgo del tipo `possible_fallacies` o
   `detected_problems` con confianza `POSSIBLE`/`UNLIKELY`, nunca como
   `logical_status: INVALID`, que implica verificación formal real.

## Salida esperada

Un `analysis-report.md` con `module: validator`. Con la configuración por
defecto, `logical_status` será casi siempre `INCOMPLETE` o
`MISSING_PREMISE` (si falta una premisa necesaria para siquiera intentar
formalizar), nunca `VALID`/`INVALID` sin un motor real detrás.

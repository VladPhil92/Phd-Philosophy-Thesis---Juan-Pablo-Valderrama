---
description: Reglas para los registros de transparencia de IA
paths:
  - "ai/**"
---

# Reglas para `ai/**`

- Todo registro en `ai/**` debe describir una intervención de IA
  materialmente relevante, conforme a los criterios de `ai/policy.md`; no
  documentes correcciones mecánicas triviales que la política excluye.
- La salida de un modelo registrada aquí nunca es evidencia académica ni
  sustituye la verificación en una fuente fiable.
- Un registro no debe insinuar verificación humana que no ocurrió. Si la
  salida no fue contrastada, el registro debe decirlo explícitamente en vez
  de omitir el campo de verificación.
- No fusiones este directorio con `research/` ni `thesis/`: aquí se guarda
  trazabilidad del proceso, no hallazgos ni argumentos de la tesis.
- Usa `templates/registro-ia.md` para cada intervención nueva y conserva su
  identificador estable `IA-AAAA-MM-DD-NN`.

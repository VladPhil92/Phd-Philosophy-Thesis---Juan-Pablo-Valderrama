# Repository Authority Policy

**Estado:** aprobada por el investigador (2026-08-08). Declarada en
[`governance/decision-log.md`](decision-log.md), DEC-004.

## Sole Research Authority

The sole authority entitled to approve, modify, integrate, reject, or
validate changes in the canonical doctoral research repository is:

Juan Pablo Valderrama Pino

GitHub identity:

VladPhil92

## Third parties

Third parties may:

- read public material;
- cite the repository;
- create forks;
- propose issues;
- submit pull requests where GitHub permits it;
- provide scholarly criticism.

Third parties may not:

- modify canonical research content directly;
- merge changes;
- validate arguments;
- modify research questions;
- alter the hypothesis;
- change methodological decisions;
- modify AI governance rules.

## Artificial Intelligence

AI agents have delegated technical capabilities only.

They have no independent repository authority and no academic authority.

## Relación con otras reglas del repositorio

Este documento formaliza, en un solo lugar, una autoridad que ya estaba
implícita y dispersa en [`CLAUDE.md`](../CLAUDE.md) («Autoría académica»),
[`ai/policy.md`](../ai/policy.md) («Autoría humana») y
[`CONTRIBUTING.md`](../CONTRIBUTING.md) («Autoría y responsabilidad»). No
sustituye esas reglas ni crea un sistema paralelo: es la referencia
canónica a la que las demás deben remitir. En particular:

- Ningún script, agente o sesión de Claude Code puede escribir
  `human_validation: validated` ni un estado epistémico `VALIDATED`
  (`templates/ficha-argumento.md`, `governance/provenance.md`) — eso ya
  se seguía de esta autoridad y sigue vigente sin cambios.
- El subagente `epistemic-auditor` sigue siendo de solo lectura y sigue
  sin poder validar argumentos, exactamente como establece este
  documento para «Artificial Intelligence».
- Fusionar (`merge`) cambios en la rama canónica sigue siendo, en la
  práctica de GitHub, una acción que solo Juan Pablo Valderrama Pino
  (VladPhil92) ejecuta o autoriza explícitamente.

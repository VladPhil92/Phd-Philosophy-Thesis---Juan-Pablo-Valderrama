# Flujo y gobernanza

## Estados

```text
PROPOSED (fuera del flujo; aprobación humana obligatoria)
  ↓
IDEA → OUTLINE → EVIDENCE READY → FIRST HUMAN DRAFT → INTERNAL REVIEW
  → READY FOR SUBMISSION → SUBMITTED → UNDER REVIEW → ACCEPTED
  → PUBLISHED → POST-PUBLICATION UPDATES
```

Los avances son secuenciales; todo retroceso e historial editorial se conserva. `FIRST HUMAN DRAFT` significa escritura intelectual del investigador, no prosa generada y luego aceptada.

## Puertas

| Transición | Evidencia exigida |
|---|---|
| `PROPOSED → IDEA` | Aprobación expresa del investigador, alcance y derivación doctoral. |
| `OUTLINE → EVIDENCE READY` | Todos los `ARG-*`, conceptos, BibTeX y citas enlazados; fuentes primarias procesadas. |
| `EVIDENCE READY → FIRST HUMAN DRAFT` | Argumentos validados y contribución delimitada por el investigador. |
| `FIRST HUMAN DRAFT → INTERNAL REVIEW` | Manuscrito humano completo y usos materiales de IA enlazados mediante `IA-*`. |
| `INTERNAL REVIEW → READY FOR SUBMISSION` | Checklist completo, RIA y PLAA documentados, formato comprobado. |
| `READY FOR SUBMISSION → SUBMITTED` | Decisión humana final y fecha, versión y destino registrados. |
| Estados posteriores | Comunicación editorial y versión enlazadas, sin material confidencial. |

## Checklist obligatorio antes del envío

Ningún ítem puede omitirse ni marcarse automáticamente:

- [ ] Todas las fuentes primarias procesadas en fichas canónicas.
- [ ] Todas las citas cotejadas con edición y localizador.
- [ ] Todos los argumentos utilizados validados por el investigador.
- [ ] Todos los conceptos utilizados estabilizados en su registro canónico.
- [ ] RIA (*epistemic-auditor*) revisó y el investigador resolvió o aceptó expresamente sus observaciones.
- [ ] PLAA revisó cada argumento aplicable y sus informes están enlazados; PLAA no valida.
- [ ] Escritura intelectual final completada y aprobada por el humano.
- [ ] Destino, alcance, idioma, límite y formato verificados.
- [ ] Uso material de IA registrado y compatible con políticas institucionales/editoriales.
- [ ] Registro canónico e historial de envío actualizados.

## Trazabilidad

```text
PUB-* → PI-* → ARG-* → clave BibTeX → ficha#citas-verificadas
      → concepto canónico → IA-* → informe RIA/PLAA → commit/versión
```

Se enlazan objetos existentes, sin copiar su contenido. Git conserva la versión usada. Un campo faltante queda `PENDING` y bloquea la puerta correspondiente. El mismo `ARG-*` validado puede respaldar capítulo, artículo y ponencia simultáneamente: esa reutilización preserva una sola fuente de verdad.

## Autoría e IA

**Human intellectual responsibility: Juan Pablo Valderrama Pino.**

La IA nunca escribe el manuscrito final ni es autora intelectual. Puede asistir con resúmenes, esquemas, reconstrucción argumental, verificación de citas, formato APA, sugerencias lingüísticas y formato de revista. Toda asistencia material se registra en [`../../ai/`](../../ai/) y se somete a verificación, reescritura y decisión humanas según [`../../ai/policy.md`](../../ai/policy.md).

La IA nunca puede formular o aprobar la contribución o conclusión final; inventar fuentes, citas o datos; conceder validación humana; producir texto final presentado como escritura del investigador; ni figurar como autora.

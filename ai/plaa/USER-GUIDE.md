# Guía de uso de PLAA para el investigador

PLAA audita la forma lógica y conceptual de un argumento **ya escrito**.
No lo escribe por ti. Úsalo cuando una ficha `ARG-*` tenga contenido real
en sus secciones de premisas, inferencia y objeciones, y quieras una
segunda mirada crítica antes de marcarla `READY_FOR_HUMAN_REVIEW`.

## Antes de empezar

- El argumento debe existir como archivo en
  `research/argument-ledger/ARG-*.md`, usando
  `templates/ficha-argumento.md`.
- PLAA no verifica si las citas son reales ni si las fuentes existen: eso
  lo hace `epistemic-auditor` (`.claude/agents/epistemic-auditor.md`) y las
  reglas de `.claude/rules/sources.md`. PLAA asume que la evidencia textual
  ya fue verificada y se concentra en la forma del razonamiento.

## Cómo pedir un análisis

1. Elige el módulo que te interesa (ver tabla abajo) y abre el archivo de
   prompt correspondiente en `prompts/`.
2. En una sesión de Claude Code, pide algo como: «Aplica
   `ai/plaa/prompts/05-fallacy-analyzer.md` a
   `research/argument-ledger/ARG-014.md` y guarda el resultado en un
   archivo temporal para revisar antes de decidir si lo incorporo».
3. Lee el resultado como lo que es: una hipótesis de auditoría con nivel
   de confianza declarado, no un veredicto. Tú decides si es correcto.
4. Si aceptas parcial o totalmente el resultado y afecta materialmente el
   argumento, regístralo con `templates/registro-ia.md` y actualiza el
   campo «Uso de IA» del `ARG-*` correspondiente, exactamente igual que
   cualquier otra intervención de IA en el repositorio.

## Módulos disponibles

| Módulo | Prompt | Qué obtienes |
|---|---|---|
| 1. Extracción de estructura | `prompts/01-argument-miner.md` | Lista de premisas, conclusión, definiciones y objeciones ya identificadas en el texto, sin interpretación añadida. |
| 2. Grafo de argumentos | `prompts/02-argument-graph.md` | Relaciones (`supports`, `depends-on`, `objects-to`…) entre este argumento y otros ya existentes en `research/argument-map.md`. |
| 3. Formalización lógica | `prompts/03-logical-formalizer.md` | Una reconstrucción formal provisional del argumento (proposicional, predicados, modal o deóntica), guardada aparte del texto original. |
| 4. Validación lógica | `prompts/04-logical-validator.md` | Hoy siempre `INCOMPLETE`: no hay motor simbólico configurado (véase `ROADMAP.md`). El informe explica qué se necesitaría para completarlo. |
| 5. Análisis de falacias | `prompts/05-fallacy-analyzer.md` | Para cada falacia del catálogo, un veredicto `POSSIBLE`/`LIKELY`/`UNLIKELY`/`NOT_DETECTED` con justificación textual. |
| 6. Consistencia conceptual | `prompts/06-concept-consistency.md` | Si un concepto clave (p. ej. «soberanía») se usa de forma distinta en dos lugares del argumento o del corpus. |
| 7. Prueba de resistencia | `prompts/07-stress-test.md` | La mejor objeción posible, el mejor contraejemplo posible y el supuesto oculto más importante — generados para atacar el argumento, nunca para confirmarlo. |
| 8. Capa de seguridad hermenéutica | aplicada automáticamente dentro de 3, 4, 5 y 7 | Antes de reportar `ERROR`/`INVALID`/`CONTRADICTION`, el prompt exige preguntar si podría tratarse de una aporía o tensión productiva, y marcarlo `PHILOSOPHICAL_REVIEW_REQUIRED` en ese caso. |

## Qué hacer con el resultado

- Un hallazgo con confianza baja o vocabulario `POSSIBLE`/`UNLIKELY` no
  autoriza ningún cambio de estado del argumento.
- Ningún resultado de PLAA cambia por sí mismo `status` ni
  `human_validation` en la cabecera del `ARG-*`. Ese cambio lo escribes tú.
- Si PLAA marca `PHILOSOPHICAL_REVIEW_REQUIRED`, esa es información para
  que decidas si el argumento contiene una aporía deliberada (en cuyo
  caso, documéntalo como tal) o si realmente hay un problema que corregir.

## Validar la forma de un informe ya producido

Si guardaste un informe de análisis en Markdown+YAML siguiendo
`templates/analysis-report.md`, puedes comprobar que tiene la forma
correcta (no que su contenido sea filosóficamente correcto) con:

```bash
python3 -c "
import sys
sys.path.insert(0, 'ai/plaa')
from plaa import schema_check
errors = schema_check.validate_analysis_report_file(sys.argv[1])
print('\n'.join(errors) if errors else 'Forma del informe correcta.')
" ruta/al/informe.md
```

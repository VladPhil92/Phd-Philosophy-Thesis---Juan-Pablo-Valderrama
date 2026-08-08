# Mapa de argumentos

**Estado:** idea — el catálogo de argumentos está vacío.

Este documento no es un lugar para filosofía nueva. Es un índice de
relaciones entre fichas `ARG-*` ya existentes en
[`research/argument-ledger/`](argument-ledger/), independiente de su
integración en la prosa capitular. Permite inspeccionar la estructura
argumental de la tesis sin leer el manuscrito completo.

## Cómo registrar una relación

Añade una línea por relación en la tabla siguiente cuando ambos `ARG-*`
referenciados existan ya como fichas reales en `research/argument-ledger/`.
No anticipes relaciones entre argumentos que todavía no existen.

Relaciones admitidas: `supports`, `depends-on`, `objects-to`, `revises`,
`contradicts`, `distinguishes`, `applies-to`.

| Origen | Relación | Destino | Nota |
|---|---|---|---|
| — | — | — | Sin argumentos registrados todavía. |

## Ejemplo (ficticio, solo para ilustrar el formato)

> El siguiente ejemplo es deliberadamente ficticio. No corresponde a fichas
> reales del repositorio y no debe interpretarse como contenido filosófico
> de la tesis.

| Origen | Relación | Destino | Nota |
|---|---|---|---|
| `ARG-002` | `supports` | `ARG-010` | Ejemplo ficticio de formato. |
| `ARG-010` | `objects-to` | `ARG-004` | Ejemplo ficticio de formato. |

## Regla de mantenimiento

Cuando se cree, retire o cambie de estado una ficha `ARG-*`, revisa si este
mapa sigue siendo exacto. Una relación hacia un argumento retirado
(`REJECTED`) debe conservarse con una nota, no borrarse en silencio: el
mapa también documenta el historial del razonamiento, no solo su estado
final.

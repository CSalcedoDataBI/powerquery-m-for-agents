# Las fichas solo citan textos con licencia

**Fecha:** 2026-10-01
**Estado:** aceptada (#1, opción B)
**Modifica:** [2026-09-28-shared-as-upstream](2026-09-28-shared-as-upstream.md), en lo que
toca a descripciones y ejemplos

## Contexto

Las fichas citaban tres textos de `#shared`: `Documentation.Description` (una línea),
`Documentation.LongDescription` (el párrafo) y `Documentation.Examples`. Ninguno tiene una
licencia declarada. El camino CC BY 4.0 del hermano DAX (`MicrosoftDocs/query-docs`) ya no
existe: el repositorio devuelve 404.

Microsoft sí publica parte del mismo texto bajo MIT. En
[`microsoft/vscode-powerquery`](https://github.com/microsoft/vscode-powerquery), el archivo
`server/src/library/standard/standard-enUs.json` describe en una línea 638 de las 659
funciones de biblioteca y 188 de las 201 constantes. No describe ningún conector, no trae el
párrafo largo y no trae ejemplos. Para 551 funciones, su línea es idéntica a la de `#shared`.

## Decisión

- **Hechos de `#shared`:** nombres, firmas, tipos de parámetros y de retorno, categorías y
  hosts. Son hechos del motor y no textos que citar.
- **Descripción de una línea:** solo la del archivo MIT de Microsoft, con atribución en cada
  ficha y en `THIRD_PARTY_NOTICES.md`. Una función que ese archivo no describe se queda sin
  descripción.
- **Lo que se deja de citar:** el párrafo largo y los ejemplos del motor.
- **Enlace a Microsoft Learn:** cada ficha lo lleva solo si `lab/shared-export/learn_links.py`
  comprobó que la página existe.
- **Lo que sigue intacto:** los ejemplos ejecutados, las notas y los conceptos, que se
  escriben en este repositorio.

## Consecuencias

- Las fichas pierden el párrafo largo. Sigue estando en Learn, que la ficha enlaza.
- Los conectores se quedan sin descripción en las fichas y en `connectors.md`.
- `sync_shared.py` lee dos entradas nuevas de `exports/`: el archivo de Microsoft, fijado a
  un commit, y `learn-links.json`.
- Este era el bloqueo para hacer público el repositorio (#13).

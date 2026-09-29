# El upstream de `m-reference` es `#shared`, no la documentación

**Fecha:** 2026-09-28
**Estado:** aceptada

## Contexto

`dax-for-agents` derivó sus fichas de `MicrosoftDocs/query-docs`, que devuelve 404 desde
2026-08. La referencia de M vivía en ese mismo repositorio, así que no hay una fuente de
documentación clonable para M.

## Decisión

El catálogo se genera exportando `#shared` desde cada host con
`skills/m-reference/scripts/export_shared.pq` y fusionando los exports con
`sync_shared.py`. Firmas, tipos y categorías salen de los tipos de función; descripciones y
ejemplos, de los metadatos `Documentation.*`.

## Consecuencias

- **A favor:** que una función esté en el catálogo prueba que existe en ese host. Se obtiene
  la disponibilidad por host (flag ⌂), que ninguna fuente pública da. Regenerar no depende de
  que nadie publique docs.
- **En contra:** exportar es un paso manual por host hasta verificar si `PQTest.exe` puede
  evaluar la consulta sin abrir Desktop. No hay páginas conceptuales en `#shared`: esas se
  escriben a mano.
- **Abierto:** la licencia de los textos `Documentation.*`. Hasta resolverla, el repo no pasa
  a público.

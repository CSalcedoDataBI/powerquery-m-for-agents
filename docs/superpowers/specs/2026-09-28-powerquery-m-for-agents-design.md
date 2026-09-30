# powerquery-m-for-agents — diseño

**Fecha:** 2026-09-28
**Estado:** borrador, pendiente de revisión
**Repo destino:** `CSalcedoDataBI/powerquery-m-for-agents` (privado al inicio, público al liberar)
**Repo hermano:** [`CSalcedoDataBI/dax-for-agents`](https://github.com/CSalcedoDataBI/dax-for-agents),
cuya spec (`2026-08-06-dax-for-agents-design.md`) dejó escrito *«M va en repo y plan aparte»*.
Este es ese repo.

---

## 1. Por qué

El hueco es el mismo que en DAX: el ecosistema de agentes para Power BI está cubierto en
*tooling* y vacío en *lenguaje*. Para M todavía más: no hay equivalente a `dax.guide` con
autoridad comparable, y el skill `power-query` de data-goblin cubre el modelo (particiones,
expresiones, TMDL), no el lenguaje función a función.

Lo que falla un agente escribiendo M, por orden de coste:

1. **Rompe el folding sin saberlo.** El código funciona en la vista previa con 1.000 filas y
   trae 10 millones al refrescar. Ningún error, solo un refresh de 40 minutos.
2. **Inventa funciones.** `Table.AddIndexColumn` existe; `Table.AddRowNumber` no. En M los
   nombres son `Categoría.Verbo`, que suena plausible siempre, y eso facilita inventar.
3. **Usa funciones que no existen en el host.** Algo que corre en Power BI Desktop puede no
   existir en Excel o en Dataflows Gen2.
4. **Cultura y tipos.** `Number.From("1,5")` da resultados distintos según la cultura; columnas
   que quedan `any` porque se omitió el 4.º argumento de `Table.AddColumn`.

### Frase de identidad

> La referencia canónica del lenguaje Power Query M para agentes de IA: cada función con su
> firma y su tipo, dónde existe y las trampas que la documentación no cuenta.

---

## 2. La decisión que separa este repo del de DAX: el upstream es el motor

`dax-for-agents` derivó sus fichas de `MicrosoftDocs/query-docs`, que devuelve 404 desde
2026-08. La documentación de M vivía en el mismo repositorio, así que esa fuente tampoco está.

**M no la necesita.** El motor expone todo lo que tiene cargado en `#shared`, y cada función
lleva su documentación como metadatos de su tipo:

| Dato | Dónde se lee |
|---|---|
| Nombre, categoría, descripción | `Value.Metadata(Value.Type(f))` → `Documentation.Name`, `Documentation.Category`, `Documentation.Description`, `Documentation.LongDescription` |
| Ejemplos | `Documentation.Examples` (lista de `[Description, Code, Result]`) |
| Parámetros | `Type.FunctionParameters(Value.Type(f))`, `Type.FunctionRequiredParameters` |
| Tipo de retorno | `Type.FunctionReturn(Value.Type(f))` |

Consecuencias:

- **El catálogo sale del motor, no de una web.** Una función que aparece en `catalog.json`
  existe en ese host, en esa versión. Es la prueba más fuerte que puede tener la eval de
  alucinación (§7).
- **Disponibilidad por host.** Se exporta `#shared` desde cada host y se cruza. Cada ficha
  lleva `hosts: [desktop, excel, dataflow-gen2, …]`. Ningún documento público da ese dato.
- **Se regenera con cada versión de Desktop**, sin depender de que alguien publique docs.

**Riesgo abierto — licencia de los textos.** Las descripciones que devuelve `#shared` vienen
del producto, no de un repo con CC BY 4.0. Antes de liberar hay que decidir si las fichas
citan esos textos tal cual o solo guardan la firma y los tipos (hechos, no expresión) y
redactan la descripción por su cuenta. Queda como decisión pendiente (ver §9).

---

## 3. Decisiones tomadas

| Decisión | Valor | Fundamento |
|---|---|---|
| Nombre del repo y del marketplace | `powerquery-m-for-agents` | Coincide con el slug de Microsoft (`learn.microsoft.com/powerquery-m/`). `m-for-agents` no aparece en ninguna búsqueda |
| Nombre del plugin | **`m`** | Es prefijo de cada skill para siempre; corto, como `dax` |
| Prefijo de skills | `m-` | Misma convención que `dax-` (ver INDEX.md del hermano, punto 5) |
| Licencia raíz | MIT © CSalcedoDataBI | Igual que el hermano |
| Idioma del repo | Inglés; specs y ADRs en español | Igual que el hermano (su ADR 2026-08-25) |
| Arquitectura de acceso | Índice plano + fichas bajo demanda | Probado en `dax-reference`: el agente lee `catalog.md`, abre **una** ficha |
| Layout | `generated/` (lo escribe el sync, se reemplaza entero) frente a `notes/` y `examples/` (a mano) | La frontera que impide que el sync se coma el trabajo manual |
| Visibilidad | Privado hasta tener `m-reference` generado y la primera eval | Después público (repos públicos no consumen cuota de Actions, R8) |

---

## 4. Skills

| Skill | Cubre | Estado en el esqueleto |
|---|---|---|
| **`m-reference`** | Una ficha por función desde `#shared`; páginas conceptuales (`let/in`, `each`/`_`, records/lists/tables, tipos, metadatos, `try/otherwise/catch`, evaluación perezosa, streaming); field notes | Generador + fixture listos, catálogo pendiente del primer export |
| **`m-folding`** | Qué pliega y qué rompe el folding por conector; `Value.NativeQuery` + `EnableFolding`; `Table.View`; cómo verificarlo (indicadores de paso, *View Native Query*, Query Diagnostics) | Stub |
| **`m-custom-functions`** | Parámetros tipados y opcionales, `Value.ReplaceType` + `Documentation.*` para documentar tus propias funciones, recursión con `@` | Stub |
| **`m-iteration`** | `List.Generate`, `List.Accumulate`, `Table.Buffer`/`List.Buffer`, `GroupKind.Local`, paginación de APIs | Stub |

**Fase 2:** `m-lib`, un índice de funciones de la comunidad al estilo `dax-lib`. No existe un
registro tipo daxlib.org para M: hay que investigar qué repos valen (licencia, mantenimiento)
antes de prometer nada.

### Fuera de alcance

- Modelado, particiones, TMDL, incremental refresh → skill `power-query` de data-goblin.
- Conectores custom (`.mez`, Power Query SDK como producto) → no es lenguaje.
- Rendimiento del refresh más allá del folding y el buffering.

---

## 5. Layout de `m-reference`

| Ruta | Qué es |
|---|---|
| `generated/catalog.md` | Índice que lee el agente: una fila por función. **Generado** |
| `generated/catalog.json` | El mismo índice para scripts. **Generado**, nunca entra al contexto |
| `generated/library/<fn>.md` | Una ficha por función. **Generado — nunca editar a mano** |
| `notes/<fn>.md` | Field notes. **A mano**; el sync nunca las toca |
| `examples/<categoria>/<fn>.md` | Ejemplos ejecutados, cada uno con el resultado que devolvió el motor. **A mano** |
| `scripts/export_shared.pq` | Consulta M que vuelca `#shared` a JSON |
| `scripts/sync_shared.py` | JSON → `generated/`. Construye en scratch y hace swap atómico |

Nombre de fichero de ficha: el nombre de la función en minúsculas con el punto como guion
(`Table.AddColumn` → `table-addcolumn.md`). Funciones con `#` (`#date`, `#table`) →
`hash-date.md`.

Flags de catálogo, heredados del hermano: **★** hay nota, **▶** hay ejemplos ejecutados. Uno
nuevo: **⌂** la función no existe en todos los hosts exportados (la ficha dice en cuáles).

---

## 6. El flujo de export

1. Abrir un host (empezando por Power BI Desktop), pegar `scripts/export_shared.pq` en una
   consulta en blanco. Devuelve una tabla de una fila y una columna con el JSON.
2. Extraer ese texto a `exports/<host>-<version>.json`. En Desktop, por el puerto local de
   Analysis Services (skill `connect-pbid`); en Excel, cargándolo a una celda.
3. `python skills/m-reference/scripts/sync_shared.py exports/*.json --write`.

Puertas antes de escribir, las mismas que en DAX:

| Puerta | Falla cuando |
|---|---|
| Nota huérfana | Existe `notes/<fn>.md` sin ficha |
| Desviación de conteo | El número de funciones se mueve más de un 5 % respecto al último sync, salvo `--accept-count-change` |
| Export vacío | Un export trae menos de 100 funciones (consulta mal pegada, host equivocado) |

**Por verificar:** si `PQTest.exe` del Power Query SDK puede evaluar la consulta de export
sin abrir Desktop. Si puede, el export pasa a ser un script y deja de ser un paso manual.

---

## 7. Evidencia: evals y lab

**Eval A/B de alucinación**, igual que el hermano: N preguntas, cada una respondida dos veces
por el mismo modelo, sin catálogo y con las filas del catálogo de su categoría. Se cuentan los
identificadores M dentro de bloques de código que no están en `catalog.json`.

En M el conteo es **más fácil que en DAX**: los nombres de biblioteca llevan punto
(`Table.AddColumn`, `List.Zip`) o son literales `#` (`#date`). El regex
`\b[A-Z][A-Za-z]+\.[A-Z][A-Za-z0-9]*\b` más la lista de `#`-literales basta; no hace falta
distinguir funciones de columnas como en DAX. Nadie juzga a nadie: es un lookup.

**Lab:** escenarios `.pbip` con datos en *Enter Data* o CSV pequeños, sin fuentes externas.
Cada field note lleva la consulta y el valor que devolvió el motor. Primeros candidatos:

- `Table.Sort` + `Table.Distinct` no conserva la primera fila sin `Table.Buffer`
- La misma conversión con `Culture` es-ES frente a en-US
- `Table.AddColumn` sin 4.º argumento → columna `any`
- Errores de celda que solo aparecen al refrescar
- `each` anidado y el `_` sombreado
- `Table.Join` frente a `Table.NestedJoin` + `ExpandTableColumn`

---

## 8. CI

Portado del hermano, con las reglas de coste de Actions (`check_workflow_cost.py`):

- `validate_skills.py`: frontmatter, INDEX, compilación, integridad catálogo ↔ fichas ↔ notas
- `check_plugin_manifest.py`: `plugin.json` coincide con los skills en disco
- `check_workflow_cost.py`: `timeout-minutes`, ubuntu, crons semanales
- Tests unitarios de `scripts/` y del sync

Se añadirán al llegar su contenido: `check_doc_claims`, `check_examples` con piso
`MIN_COVERED`, `check_eval_claims` y `render_readme_assets` (mapa de cobertura).

---

## 9. Pendiente

| # | Pregunta | Bloquea |
|---|---|---|
| 1 | Licencia de los textos de `Documentation.*`: ¿citar o redactar? | Liberar el repo |
| 2 | ¿PQTest.exe evalúa `export_shared.pq` sin Desktop? | Automatizar el export |
| 3 | ¿Qué hosts se exportan en la v1? (propuesta: Desktop + Excel) | Flag ⌂ |
| 4 | Páginas conceptuales: sin upstream, ¿de dónde salen? (propuesta: a mano, cortas, con ejemplo ejecutado) | `generated/concepts.md` |
| 5 | Repos candidatos para `m-lib` | Fase 2 |

| 6 | ✅ **Constantes** (`GroupKind.Local`, `JoinKind.*`, `Occurrence.*`): decidido (2026-09-29) — el export también toma los miembros de `#shared` que no son funciones, y `sync_shared.py` genera `constants.md` (nombre, tipo, valor, resumen; sin cards). | — |
| 7 | ✅ **Conectores frente a biblioteca:** decidido (2026-09-29) — `connectors.md` aparte. Regla: función **sin** `Documentation.Category` cuyo prefijo no usa ninguna función categorizada. «Accessing data» (`Csv.Document`, `Web.Contents`…) es categoría documentada de la biblioteca y se queda en `catalog.md`. | — |

### Primer export (2026-09-28) — lo que enseñó

- Desktop 2.157.879.0, **932 funciones, 0 errores de export**, refresco en 5 s. Las firmas
  coinciden con las de Microsoft (`Table.AddColumn(..., optional columnType as nullable type)
  as table`), así que `TypeName` es correcto.
- La primera versión de la consulta **no parseaba**: usaba `meta` y `type` como
  identificadores (palabras reservadas de M) y tenía `name = name` dentro de un record, que
  se refiere al propio campo. Desktop lo reporta como «Se esperaba el token Identifier» al
  abrir el `.pbip`, no al refrescar. Es exactamente la clase de error que este repo quiere
  evitar en los agentes, cometida escribiéndolo.
- Los textos `Documentation.*` son **HTML** (`<code>`, `<ul><li>`, `&quot;`) con sangría de
  código C#. Cuatro espacios iniciales en Markdown son un bloque de código, así que
  `sync_shared.py` convierte a Markdown y quita la sangría.
- `#date`, `#table` y compañía **no están en `#shared`**: son sintaxis. La eval de §7 tiene
  que tratarlos como palabras clave, no buscarlos en el catálogo.
- El export de Desktop está automatizado: `lab/shared-export/` genera un `.pbip` cuya única
  partición **es** `export_shared.pq`, lo abre, refresca por TMSL y lee el JSON por ADOMD
  usando el cliente que trae el propio Desktop. La pregunta 2 (PQTest) deja de bloquear para
  Desktop; sigue abierta para Excel y dataflows.

### Constantes y conectores (2026-09-29) — lo que enseñó

- El mismo Desktop 2.157.879.0 expone **201 miembros que no son funciones**: 118 números
  (enums como `JoinKind.Inner = 0`, `Number.PI`), 69 valores de tipo (`Int64.Type`,
  `JoinKind.Type`), 9 textos, 3 nulos y 2 records. 192 traen `Documentation.Description`,
  a veces en el valor y a veces en su tipo; la consulta mira los dos.
- La primera frase de la descripción de un enum suele ser la misma para todos sus valores
  («A possible value for the optional `JoinKind` parameter in `Table.Join`»), así que
  `constants.md` guarda hasta 200 caracteres en vez de la primera frase.
- `Culture.Current` y `TimeZone.Current` no son constantes sino la configuración de la
  máquina que exporta: el primer export publicó la zona horaria del equipo como si fuera un
  valor de M. La consulta deja en null el valor de todo miembro `*.Current`.
- La regla de conectores separa **273** de las 932 funciones, no las ~353 que estimaba §9.7.
  El resto de las 275 sin categoría (`Value.ResourceExpression`, una de `Cdm`) comparte
  prefijo con la biblioteca. `catalog.md` pasa de 106.079 a 81.257 bytes.

---

## 10. Plan por fases

1. ✅ **Esqueleto**: manifiestos, INDEX, 4 `SKILL.md`, generador con fixture, CI.
2. ✅ **Primer export** de Desktop → `generated/` real (2026-09-28). Falta: Excel como
   segundo host. §9.6 y §9.7 decididos el 2026-09-29.
3. **Eval A/B** con 4 modelos → tabla del README.
4. **`m-folding`** completo, con lab.
5. Field notes y ejemplos por categorías completas (Text, List, Table).
6. Pasar a público.

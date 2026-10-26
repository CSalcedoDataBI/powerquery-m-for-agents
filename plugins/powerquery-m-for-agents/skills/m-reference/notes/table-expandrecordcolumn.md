<!-- lab: desktop 2.158.1304.0 -->

# Table.ExpandRecordColumn: the new columns are any

**What happens:** expanding a column of records gives every new column the type `any`, even
when the values inside the records were dates or numbers. A common pattern loses its types
this way: "one row per key" with `Table.Group(..., each _, type table)`, then `[rows]{0}`, then
expand. The types set before grouping are gone, and Power BI loads those columns as text.

```m
let
    T = #table(type table [k = text, d = date], {{"a", #date(2024, 1, 2)}, {"a", #date(2024, 1, 3)}}),
    G = Table.Group(T, {"k"}, {{"rows", each _, type table}}),
    First = Table.AddColumn(G, "first", each [rows]{0}),
    E = Table.ExpandRecordColumn(First, "first", {"d"})
in
    Value.Type(E)
```

```text
type table [k = text, rows = table [], d = any]
```

The values are still dates; only the column type says `any`:

```m
let
    T = #table(type table [k = text, d = date], {{"a", #date(2024, 1, 2)}}),
    G = Table.Group(T, {"k"}, {{"rows", each _, type table}}),
    E = Table.ExpandRecordColumn(Table.AddColumn(G, "first", each [rows]{0}), "first", {"d"})
in
    Value.Type(E{0}[d])
```

```text
type date
```

The expand takes its column types from the record column's type. Give that column a record
type when you add it, and the expanded columns carry it:

```m
let
    T = #table(type table [k = text, d = date], {{"a", #date(2024, 1, 2)}}),
    G = Table.Group(T, {"k"}, {{"rows", each _, type table}}),
    First = Table.AddColumn(G, "first", each [rows]{0}, type [k = text, d = date]),
    E = Table.ExpandRecordColumn(First, "first", {"d"})
in
    Value.Type(E)
```

```text
type table [k = text, rows = table [], d = date]
```

**Do this:** after `Table.ExpandRecordColumn`, either type the record column when you create it
(`Table.AddColumn(..., type [d = date])`, as above) or retype the expanded columns with
`Table.TransformColumnTypes`. Do not trust the types set before a `Table.Group`.

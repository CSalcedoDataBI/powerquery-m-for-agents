<!-- lab: desktop 2.157.879.0 -->

# Table.AddColumn without its fourth argument

Without `columnType`, the new column's type is `any`, whatever the function returns.

```m
let
    T = #table(type table [Qty = Int64.Type], {{1}, {2}})
in
    {Value.Type(Table.AddColumn(T, "D", each [Qty] * 2)), Value.Type(Table.AddColumn(T, "D", each [Qty] * 2, Int64.Type))}
```

```text
{type table [Qty = Int64.Type, D = any], type table [Qty = Int64.Type, D = Int64.Type]}
```

The schema says the same: `Any.Type`, kind `any`.

```m
let
    T = #table(type table [Qty = Int64.Type], {{1}, {2}}),
    Added = Table.AddColumn(T, "D", each [Qty] * 2)
in
    Table.SelectColumns(Table.Schema(Added), {"Name", "TypeName", "Kind"})
```

```text
#table(type table [Name = text, TypeName = text, Kind = text], {{"Qty", "Int64.Type", "number"}, {"D", "Any.Type", "any"}})
```

**Do this:** pass the type as the fourth argument whenever the column feeds a model or a later
typed step. It declares the type; it does not convert - see `concepts/types-metadata.md`.

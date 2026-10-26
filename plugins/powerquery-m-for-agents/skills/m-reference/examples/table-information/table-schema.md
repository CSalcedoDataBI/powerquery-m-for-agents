<!-- lab: desktop 2.157.879.0 -->

# Table.Schema

Column metadata (a few of its columns shown).

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.SelectColumns(Table.Schema(T), {"Name", "Position", "TypeName", "Kind"})
```

```text
#table(type table [Name = text, Position = number, TypeName = text, Kind = text], {{"Name", 0, "Text.Type", "text"}, {"Qty", 1, "Int64.Type", "number"}})
```

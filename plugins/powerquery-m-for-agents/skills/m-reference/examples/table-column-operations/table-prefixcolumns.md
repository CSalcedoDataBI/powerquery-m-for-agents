<!-- lab: desktop 2.157.879.0 -->

# Table.PrefixColumns

Every column name gets the prefix and a dot.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ColumnNames(Table.PrefixColumns(T, "T"))
```

```text
{"T.Name", "T.Qty"}
```

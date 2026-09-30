<!-- lab: desktop 2.157.879.0 -->

# Table.ReplaceKeys

Replace the key metadata.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Keys(Table.ReplaceKeys(T, {[Columns = {"Name"}, Primary = true]}))
```

```text
{[Columns = {"Name"}, Primary = true]}
```

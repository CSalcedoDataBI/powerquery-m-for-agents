<!-- lab: desktop 2.157.879.0 -->

# Table.AddKey

The key is metadata: rows are not checked.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Keys(Table.AddKey(T, {"Name"}, true))
```

```text
{[Columns = {"Name"}, Primary = true]}
```

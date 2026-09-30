<!-- lab: desktop 2.157.879.0 -->

# Table.First

The first row, or null when empty.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.First(T), Table.First(#table({"a"}, {}))}
```

```text
{[Name = "a", Qty = 1], null}
```

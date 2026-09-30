<!-- lab: desktop 2.157.879.0 -->

# Table.IsEmpty

Empty or not.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.IsEmpty(T), Table.IsEmpty(Table.FirstN(T, 0))}
```

```text
{false, true}
```

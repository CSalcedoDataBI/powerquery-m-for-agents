<!-- lab: desktop 2.157.879.0 -->

# Table.SingleRow

Exactly one row, or an error.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.SingleRow(#table({"a"}, {{1}})), Table.SingleRow(T)}
```

```text
{[a = 1], error: Expression.Error: There were too many elements in the enumeration to complete the operation. | Detail: {[Name = "a", Qty = 1], [Name = "b", Qty = 2], [Name = "a", Qty = 3]}}
```

<!-- lab: desktop 2.159.883.0 -->

# RowExpression.Column

The result is a record describing a column access, not the column's value.

```m
RowExpression.Column("Sales")
```

```text
[Kind = "FieldAccess", MemberName = "Sales", Expression = [Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}]]
```

It should describe the same access that `each [Sales]` produces.

```m
RowExpression.Column("Sales") = RowExpression.From(each [Sales])
```

```text
true
```

`columnName` is not optional, so `null` should raise an error. An empty name or one containing spaces is a separate case.

```m
[Null = try RowExpression.Column(null), Empty = try RowExpression.Column(""), Spaced = try RowExpression.Column("Unit Price")]
```

```text
[Null = [HasError = true, Error = [Reason = "Expression.Error", Message = "We cannot convert the value null to type Text.", Detail = [Value = null, Type = type text], #"Message.Format" = "We cannot convert the value #{0} to type #{1}.", #"Message.Parameters" = {"null", "Text"}, ErrorCode = "10277"]], Empty = [HasError = false, Value = [Kind = "FieldAccess", MemberName = "", Expression = [Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}]]], Spaced = [HasError = false, Value = [Kind = "FieldAccess", MemberName = "Unit Price", Expression = [Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}]]]]
```

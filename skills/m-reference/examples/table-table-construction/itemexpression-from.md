<!-- lab: desktop 2.159.883.0 -->

# ItemExpression.From

These examples show the record it returns for a one-parameter function's body, and what happens with field access and a two-parameter function.

```m
ItemExpression.From(each _ <> null)
```

```text
[Kind = "Binary", Operator = "NotEquals", Left = [Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}], Right = [Kind = "Constant", Value = null]]
```

Field access on the item becomes a `FieldAccess` node.

```m
ItemExpression.From(each [Price] > 10 and [Price] <= 100)
```

```text
[Kind = "Binary", Operator = "And", Left = [Kind = "Binary", Operator = "GreaterThan", Left = [Kind = "FieldAccess", MemberName = "Price", Expression = [Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}]], Right = [Kind = "Constant", Value = 10]], Right = [Kind = "Binary", Operator = "LessThanOrEquals", Left = [Kind = "FieldAccess", MemberName = "Price", Expression = [Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}]], Right = [Kind = "Constant", Value = 100]]]
```

A function with two parameters has no single item.

```m
ItemExpression.From((x, y) => x + y)
```

```text
[Kind = "Invocation", Function = [Kind = "Constant", Value = function (x as any, y as any) as any], Arguments = {[Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}]}]
```

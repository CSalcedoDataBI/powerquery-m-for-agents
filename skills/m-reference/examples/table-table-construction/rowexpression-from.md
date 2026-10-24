<!-- lab: desktop 2.159.883.0 -->

# RowExpression.From

These examples show the AST built from a row function's body, including nulls, captured variables and a function with more than one parameter.

```m
RowExpression.From(each [Units] > 20 and [Region] = null)
```

```text
[Kind = "Binary", Operator = "And", Left = [Kind = "Binary", Operator = "GreaterThan", Left = [Kind = "FieldAccess", MemberName = "Units", Expression = [Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}]], Right = [Kind = "Constant", Value = 20]], Right = [Kind = "Binary", Operator = "Equals", Left = [Kind = "FieldAccess", MemberName = "Region", Expression = [Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}]], Right = [Kind = "Constant", Value = null]]]
```

```m
let threshold = 10 in RowExpression.From(each [Units] >= threshold)
```

```text
[Kind = "Binary", Operator = "GreaterThanOrEquals", Left = [Kind = "FieldAccess", MemberName = "Units", Expression = [Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}]], Right = [Kind = "Constant", Value = 10]]
```

```m
RowExpression.From((a, b) => a + b)
```

```text
[Kind = "Invocation", Function = [Kind = "Constant", Value = function (a as any, b as any) as any], Arguments = {[Kind = "Invocation", Function = [Kind = "Constant", Value = function () as any], Arguments = {}]}]
```

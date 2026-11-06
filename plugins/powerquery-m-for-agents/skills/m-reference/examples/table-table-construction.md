<!-- lab: desktop 2.157.879.0 -->

# Executed examples: table-table-construction

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## ItemExpression.From

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

## RowExpression.Column

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

## RowExpression.From

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

## Table.FromColumns

One list per column.

```m
Table.FromColumns({{1, 2}, {"a", "b"}}, {"n", "t"})
```

```text
#table(type table [n = any, t = any], {{1, "a"}, {2, "b"}})
```

## Table.FromList

Split each item into columns.

```m
Table.FromList({"a,1", "b,2"}, Splitter.SplitTextByDelimiter(","), {"k", "v"})
```

```text
#table(type table [k = nullable text, v = nullable text], {{"a", "1"}, {"b", "2"}})
```

## Table.FromRecords

A missing field is an error unless told to use null.

```m
{Table.FromRecords({[a = 1, b = 2], [a = 3]}, null, MissingField.UseNull), Table.FromRecords({[a = 1, b = 2], [a = 3]})}
```

```text
{#table(type table [a = any, b = any], {{1, 2}, {3, null}}), error: Expression.Error: The field 'b' of the record wasn't found. | Detail: [a = 3]}
```

## Table.FromRows

One list per row.

```m
Table.FromRows({{1, "a"}, {2, "b"}}, {"n", "t"})
```

```text
#table(type table [n = any, t = any], {{1, "a"}, {2, "b"}})
```

## Table.FromValue

A scalar and a record.

```m
{Table.FromValue(5), Table.FromValue([a = 1, b = 2])}
```

```text
{#table(type table [Value = number], {{5}}), #table(type table [Name = text, Value = any], {{"a", 1}, {"b", 2}})}
```

## Table.View

A handler answers the row count instead of counting.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RowCount(Table.View(T, [GetRowCount = () => 99]))
```

```text
99
```

## Table.ViewError

An error record marked for a view handler.

```m
Table.ViewError(Error.Record("Reason", "Message"))
```

```text
[Reason = "Reason", Message = "Message", Detail = null, #"Message.Format" = null, #"Message.Parameters" = null, ErrorCode = null]
```

## Table.ViewFunction

The type of a function wrapped for view handlers.

```m
Value.Type(Table.ViewFunction((t as table) => Table.RowCount(t)))
```

```text
type function (t as table []) as any
```

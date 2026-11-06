<!-- lab: desktop 2.159.883.0 -->

# Executed examples: function

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Function.From

The wrapped function receives the supplied arguments as one list, and the declared parameter types may not be checked.

```m
Function.From(type function (a as number, b as number) as number, List.Sum)(2, 1)
```

```text
3
```

An omitted optional parameter is absent from the list rather than passed as null, so the list is shorter.

```m
Function.From(type function (a as number, optional b as number) as list, each _)(5)
```

```text
{5}
```

This passes text to a parameter declared `as number`, to show whether the declared type is enforced.

```m
Function.From(type function (a as number) as text, each Text.Upper(_{0}))("abc")
```

```text
"ABC"
```

## Function.Invoke

The list is spread into separate arguments, and optional parameters can be omitted or passed as null.

```m
Function.Invoke(List.Sum, {{1, 2, 3}})
```

```text
6
```

Without the outer list, each number becomes its own argument, so List.Sum gets too many arguments.

```m
Function.Invoke(List.Sum, {1, 2, 3})
```

```text
error: Expression.Error: 3 arguments were passed to a function which expects between 1 and 2. | Detail: [Pattern = null, Arguments = {1, 2, 3}]
```

Omitting an optional argument and passing null for one both use the default.

```m
{Function.Invoke(Text.PadStart, {"7", 3}), Function.Invoke(Text.PadStart, {"7", 3, null}), Function.Invoke(Text.PadStart, {"7", 3, "0"})}
```

```text
{"  7", "  7", "007"}
```

## Function.ScalarVector

The vector function gets a table of batched calls, with one column per parameter. It must return one result per row, in the same order.

```m
let
    f = Function.ScalarVector(
        type function (x as number) as number,
        (input) => List.Repeat({Table.RowCount(input)}, Table.RowCount(input))
    )
in
    Table.AddColumn(#table({"x"}, {{1}, {2}, {3}}), "BatchSize", each f([x]))
```

```text
#table(type table [x = any, BatchSize = any], {{1, error: Expression.Error: Vector functions passed to Function.ScalarVector may not enumerate their input table more than once.}, {2, error: Expression.Error: Vector functions passed to Function.ScalarVector may not enumerate their input table more than once.}, {3, error: Expression.Error: Vector functions passed to Function.ScalarVector may not enumerate their input table more than once.}})
```

Called directly, each call is a batch of one. A null argument reaches the vector function as a null cell.

```m
let
    f = Function.ScalarVector(
        type function (x as nullable number, y as nullable number) as nullable number,
        (input) => List.Transform(Table.ToRecords(input), each [x] + [y])
    )
in
    {f(1, 2), f(null, 2)}
```

```text
{3, null}
```

An omitted optional parameter still gets a column in the input table.

```m
let
    f = Function.ScalarVector(
        type function (x as number, optional y as number) as list,
        (input) => List.Transform(Table.ToRecords(input), each Record.FieldNames(_) & {[y]})
    )
in
    f(1)
```

```text
{"x", "y", null}
```

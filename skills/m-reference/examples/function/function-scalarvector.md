<!-- lab: desktop 2.159.883.0 -->

# Function.ScalarVector

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

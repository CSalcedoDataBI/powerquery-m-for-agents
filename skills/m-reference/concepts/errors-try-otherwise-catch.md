<!-- lab: desktop 2.157.879.0 -->

# Errors: try, otherwise, catch

An error is a value that propagates until something catches it. `try` turns it into a record
that says whether it failed and why.

```m
try Number.FromText("x")
```

```text
[HasError = true, Error = [Reason = "DataFormat.Error", Message = "We couldn't convert to Number.", Detail = "x", #"Message.Format" = "We couldn't convert to Number.", #"Message.Parameters" = null, ErrorCode = "10041"]]
```

```m
try Number.FromText("12")
```

```text
[HasError = false, Value = 12]
```

Division by zero is not an error in M: it is infinity.

```m
{1 / 0, try 1 / 0}
```

```text
{#infinity, [HasError = false, Value = #infinity]}
```

## otherwise and catch

`otherwise` replaces a failure with a value. `catch` receives the error record, so the fallback
can depend on what went wrong.

```m
{try Number.FromText("x") otherwise -1, try Number.FromText("x") catch (e) => e[Reason]}
```

```text
{-1, "DataFormat.Error"}
```

## Raising your own

`error` raises a text or an error record built with `Error.Record`.

```m
try error Error.Record("Validation", "Qty must be positive", [Qty = -3])
```

```text
[HasError = true, Error = [Reason = "Validation", Message = "Qty must be positive", Detail = [Qty = -3], #"Message.Format" = null, #"Message.Parameters" = null, ErrorCode = null]]
```

## Errors in cells

A table can hold an error in one cell and still be a valid table. Counting its rows or trying
the whole table succeeds; the error only surfaces when that cell is read, which in Power BI
means during refresh, not while you build the query.

```m
let
    T = Table.TransformColumnTypes(#table({"v"}, {{"1"}, {"x"}}), {{"v", Int64.Type}})
in
    {Table.RowCount(T), (try T)[HasError], T[v]}
```

```text
{2, false, {1, error: DataFormat.Error: We couldn't convert to Number. | Detail: "x"}}
```

Handle them per row: remove the rows, or replace the error values.

```m
let
    T = Table.TransformColumnTypes(#table({"v"}, {{"1"}, {"x"}}), {{"v", Int64.Type}})
in
    {Table.RemoveRowsWithErrors(T), Table.ReplaceErrorValues(T, {{"v", 0}})}
```

```text
{#table(type table [v = nullable number], {{1}}), #table(type table [v = nullable number], {{1}, {0}})}
```

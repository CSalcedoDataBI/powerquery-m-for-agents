<!-- lab: desktop 2.157.879.0 -->

# Executed examples: table-table-construction

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

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

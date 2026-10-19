<!-- lab: desktop 2.158.1304.0 -->

# Table.Join versus Table.NestedJoin

**What happens:** `Table.Join` puts both tables' columns side by side, so any name the two
share is an error - the key column included, when both sides call it the same. `Table.NestedJoin`
puts the right table in one nested column instead, and you choose names when you expand it.

Both tables have `Id` and `Name`. A flat join:

```m
let
    A = #table({"Id", "Name"}, {{1, "x"}, {2, "y"}}),
    B = #table({"Id", "Name"}, {{1, "p"}})
in
    Table.Join(A, "Id", B, "Id", JoinKind.LeftOuter)
```

```text
error: Expression.Error: A join operation cannot result in a table with duplicate column names ("Id"). | Detail: type table [Id = any, Name = any]
```

A nested join, then expanding with new names:

```m
let
    A = #table({"Id", "Name"}, {{1, "x"}, {2, "y"}}),
    B = #table({"Id", "Name"}, {{1, "p"}}),
    Nested = Table.NestedJoin(A, "Id", B, "Id", "B", JoinKind.LeftOuter)
in
    Table.ExpandTableColumn(Nested, "B", {"Name"}, {"B.Name"})
```

```text
#table(type table [Id = any, Name = any, #"B.Name" = any], {{1, "x", "p"}, {2, "y", null}})
```

A flat join works when the column names do not collide.

```m
let
    A = #table({"Id", "Name"}, {{1, "x"}, {2, "y"}}),
    B = #table({"Key", "Other"}, {{1, "p"}})
in
    Table.Join(A, "Id", B, "Key", JoinKind.LeftOuter)
```

```text
#table(type table [Id = any, Name = any, Key = any, Other = any], {{1, "x", 1, "p"}, {2, "y", null, null}})
```

**Do this:** use `Table.NestedJoin` + `Table.ExpandTableColumn` when names can collide or you
want only some right-hand columns; `Table.Join` when the names are already distinct.

## Keys of different types never match

**What happens:** `"10" = 10` is `false`, so a key read as text on one side and as a number on
the other matches nothing, with no error. It is the usual case when crossing sources: a CSV
read with `Csv.Document` gives every column as text, while an Excel workbook keeps the number
the cell holds. A left outer join leaves every row without a partner, and `Table.NestedJoin`
behaves the same.

```m
let
    FromCsv = #table({"Key"}, {{"10"}, {"11"}}),
    FromExcel = #table({"Id", "Code"}, {{10, "EUR"}, {11, "USD"}})
in
    Table.Join(FromCsv, "Key", FromExcel, "Id", JoinKind.LeftOuter)
```

```text
#table(type table [Key = any, Id = any, Code = any], {{"10", null, null}, {"11", null, null}})
```

Bring both keys to one type first. Text is the safe side, with the culture of the data:

```m
let
    FromCsv = #table({"Key"}, {{"10"}, {"11"}}),
    FromExcel = #table({"Id", "Code"}, {{10, "EUR"}, {11, "USD"}}),
    Keyed = Table.TransformColumns(FromExcel, {{"Id", each Text.From(_, "en-US"), type text}})
in
    Table.Join(FromCsv, "Key", Keyed, "Id", JoinKind.LeftOuter)
```

```text
#table(type table [Key = any, Id = nullable text, Code = any], {{"10", "10", "EUR"}, {"11", "11", "USD"}})
```

Pick one canonical form, because the number does not remember how the text wrote it:

```m
{Text.From(10.0, "en-US"), Text.From(10.0, "en-US") = "10.0", Number.From("10.0") = 10}
```

```text
{"10", false, true}
```

**Do this:** before joining sources of different origin, normalise both keys the same way -
`Text.Trim(Text.From(v, culture))` on both sides, or `Number.From` on both when the keys are
truly numeric. Check the match count after the join, since a miss is silent.

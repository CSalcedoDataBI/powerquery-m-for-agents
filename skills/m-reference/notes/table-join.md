<!-- lab: desktop 2.157.879.0 -->

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

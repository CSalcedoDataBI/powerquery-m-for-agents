<!-- lab: desktop 2.157.879.0 -->

# Table.NestedJoin

The matches as a nested table column, empty when none.

```m
Table.NestedJoin(#table({"Id", "A"}, {{1, "x"}, {2, "y"}}), "Id", #table({"Key", "B"}, {{1, "p"}}), "Key", "Right", JoinKind.LeftOuter)
```

```text
#table(type table [Id = any, A = any, Right = table [Key = any, B = any]], {{1, "x", #table(type table [Key = any, B = any], {{1, "p"}})}, {2, "y", #table(type table [Key = any, B = any], {})}})
```

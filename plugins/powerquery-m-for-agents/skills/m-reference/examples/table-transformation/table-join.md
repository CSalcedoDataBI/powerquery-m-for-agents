<!-- lab: desktop 2.157.879.0 -->

# Table.Join

A flat join; unmatched left rows get nulls.

```m
Table.Join(#table({"Id", "A"}, {{1, "x"}, {2, "y"}}), "Id", #table({"Key", "B"}, {{1, "p"}}), "Key", JoinKind.LeftOuter)
```

```text
#table(type table [Id = any, A = any, Key = any, B = any], {{1, "x", 1, "p"}, {2, "y", null, null}})
```

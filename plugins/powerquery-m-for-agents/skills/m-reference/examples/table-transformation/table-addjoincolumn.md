<!-- lab: desktop 2.157.879.0 -->

# Table.AddJoinColumn

A nested table of matches per row; empty when none.

```m
Table.AddJoinColumn(#table({"Id"}, {{1}, {2}}), "Id", #table({"Id", "V"}, {{1, "x"}}), "Id", "Match")
```

```text
#table(type table [Id = any, Match = table [Id = any, V = any]], {{1, #table(type table [Id = any, V = any], {{1, "x"}})}, {2, #table(type table [Id = any, V = any], {})}})
```

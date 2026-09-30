<!-- lab: desktop 2.157.879.0 -->

# Table.AddRankColumn

Dense ranking: ties share a rank and the next one is not skipped.

```m
Table.AddRankColumn(#table({"P", "S"}, {{"a", 10}, {"b", 20}, {"c", 20}}), "Rank", {"S", Order.Descending}, [RankKind = RankKind.Dense])
```

```text
#table(type table [P = any, S = any, Rank = nullable number], {{"b", 20, 1}, {"c", 20, 1}, {"a", 10, 2}})
```

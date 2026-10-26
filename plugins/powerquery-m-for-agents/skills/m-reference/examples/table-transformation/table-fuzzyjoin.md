<!-- lab: desktop 2.157.879.0 -->

# Table.FuzzyJoin

Key columns must be typed as text.

```m
Table.FuzzyJoin(#table({"A"}, {{"Seattle"}}), {"A"}, #table({"B"}, {{"seattle"}}), {"B"})
```

```text
error: Expression.Error: We only support text columns for fuzzy join operations. The column 'A' is not of type text.
```

Typed as text, a case difference still matches.

```m
Table.FuzzyJoin(#table(type table [A = text], {{"Seattle"}}), {"A"}, #table(type table [B = text], {{"seattle"}, {"Redmond"}}), {"B"})
```

```text
#table(type table [A = text, B = text], {{"Seattle", "seattle"}})
```

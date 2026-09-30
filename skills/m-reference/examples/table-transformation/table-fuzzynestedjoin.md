<!-- lab: desktop 2.157.879.0 -->

# Table.FuzzyNestedJoin

Key columns must be typed as text; the error surfaces inside the nested column.

```m
Table.FuzzyNestedJoin(#table({"A"}, {{"Seattle"}}), {"A"}, #table({"B"}, {{"seattle"}}), {"B"}, "M")
```

```text
#table(type table [A = any, M = nullable table [B = any]], {{"Seattle", error: Expression.Error: We only support text columns for fuzzy join operations. The column 'B' is not of type text.}})
```

Typed as text, the matches arrive as a nested table.

```m
Table.FuzzyNestedJoin(#table(type table [A = text], {{"Seattle"}}), {"A"}, #table(type table [B = text], {{"seattle"}, {"Redmond"}}), {"B"}, "M")
```

```text
#table(type table [A = text, M = nullable table [B = text]], {{"Seattle", #table(type table [B = any], {{"seattle"}})}})
```

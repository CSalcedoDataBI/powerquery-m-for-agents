<!-- lab: desktop 2.157.879.0 -->

# Table.FuzzyGroup

The key column must be typed as text.

```m
Table.FuzzyGroup(#table({"City"}, {{"Seattle"}}), "City", {{"Count", each Table.RowCount(_), Int64.Type}})
```

```text
error: Expression.Error: We only support text columns for fuzzy join operations. The column 'City' is not of type text.
```

Typed as text, similar spellings are grouped together.

```m
Table.FuzzyGroup(#table(type table [City = text], {{"Seattle"}, {"seattle"}, {"Redmond"}}), "City", {{"Count", each Table.RowCount(_), Int64.Type}})
```

```text
#table(type table [City = text, Count = Int64.Type], {{"Seattle", 2}, {"Redmond", 1}})
```

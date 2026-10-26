<!-- lab: desktop 2.157.879.0 -->

# Table.AddFuzzyClusterColumn

The column must be typed as text: a #table with bare column names is not.

```m
Table.AddFuzzyClusterColumn(#table({"City"}, {{"Seattle"}, {"seattle"}}), "City", "Cluster")
```

```text
error: Expression.Error: We only support text columns for fuzzy join operations. The column 'City' is not of type text.
```

Typed as text, similar spellings get one cluster value.

```m
Table.AddFuzzyClusterColumn(#table(type table [City = text], {{"Seattle"}, {"seattle"}, {"Seatle"}, {"Redmond"}}), "City", "Cluster")
```

```text
#table(type table [City = text, Cluster = text], {{"Seattle", "Seattle"}, {"seattle", "Seattle"}, {"Seatle", "Seattle"}, {"Redmond", "Redmond"}})
```

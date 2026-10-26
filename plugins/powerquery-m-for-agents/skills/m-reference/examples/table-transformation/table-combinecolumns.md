<!-- lab: desktop 2.157.879.0 -->

# Table.CombineColumns

Two columns into one text.

```m
Table.CombineColumns(#table({"F", "L"}, {{"Ana", "Diaz"}}), {"F", "L"}, Combiner.CombineTextByDelimiter(" "), "Full")
```

```text
#table(type table [Full = text], {{"Ana Diaz"}})
```

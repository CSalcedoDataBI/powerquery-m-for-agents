<!-- lab: desktop 2.157.879.0 -->

# Table.SplitColumn

Split a text column into two.

```m
Table.SplitColumn(#table({"Full"}, {{"Ana Diaz"}}), "Full", Splitter.SplitTextByDelimiter(" "), {"First", "Last"})
```

```text
#table(type table [First = nullable text, Last = nullable text], {{"Ana", "Diaz"}})
```

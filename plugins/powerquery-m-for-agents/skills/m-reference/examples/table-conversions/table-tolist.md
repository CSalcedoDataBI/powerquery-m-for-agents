<!-- lab: desktop 2.157.879.0 -->

# Table.ToList

Each row combined into one text.

```m
Table.ToList(#table({"a", "b"}, {{"x", "y"}, {"z", "w"}}), Combiner.CombineTextByDelimiter("|"))
```

```text
{"x|y", "z|w"}
```

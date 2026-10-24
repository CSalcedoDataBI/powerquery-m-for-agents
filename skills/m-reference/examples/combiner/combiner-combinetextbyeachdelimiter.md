<!-- lab: desktop 2.159.883.0 -->

# Combiner.CombineTextByEachDelimiter

Each delimiter is used once, in order, between consecutive items, and the examples show null items, running out of delimiters, and quoting.

```m
Combiner.CombineTextByEachDelimiter({"=", "+"})({"a", null, "c"})
```

```text
"a=+c"
```

With more items than delimiters, the items left over after the last delimiter show how the combiner handles the gaps it has no delimiter for.

```m
Combiner.CombineTextByEachDelimiter({"-"})({"a", "b", "c", "d"})
```

```text
"a-bcd"
```

With QuoteStyle.Csv, items that contain a delimiter or a quote character may be wrapped in quotes.

```m
Combiner.CombineTextByEachDelimiter({",", ";"}, QuoteStyle.Csv)({"x,y", "say ""hi""", "z;w"})
```

```text
"""x,y"",""say """"hi"""""";z;w"
```

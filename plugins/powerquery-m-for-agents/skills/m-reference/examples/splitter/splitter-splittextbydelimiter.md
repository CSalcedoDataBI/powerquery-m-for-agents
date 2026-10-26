<!-- lab: desktop 2.157.879.0 -->

# Splitter.SplitTextByDelimiter

Quotes group text even without `QuoteStyle.Csv`, and a null input gives an empty list.

```m
Splitter.SplitTextByDelimiter(",")("a,""b,c"",d")
```

```text
{"a", "b,c", "d"}
```

```m
Splitter.SplitTextByDelimiter(",", QuoteStyle.Csv)("a,""b,c"",d")
```

```text
{"a", "b,c", "d"}
```

```m
Splitter.SplitTextByDelimiter(",")(null)
```

```text
{}
```

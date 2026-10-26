<!-- lab: desktop 2.157.879.0 -->

# Splitter.SplitTextByAnyDelimiter

A null quote style acts like `QuoteStyle.Csv`: the quoted comma does not split. The last block shows `startAtEnd` with an unmatched quote, where the result does not follow a left-to-right reading.

```m
Splitter.SplitTextByAnyDelimiter({","}, null, null)("""a,b"",c")
```

```text
{"a,b", "c"}
```

```m
Splitter.SplitTextByAnyDelimiter({","}, QuoteStyle.Csv)("""a,b"",c")
```

```text
{"a,b", "c"}
```

```m
Splitter.SplitTextByAnyDelimiter({",", ";"}, QuoteStyle.Csv, true)("a,""b;c,d")
```

```text
{"a,b", "c", "d"}
```

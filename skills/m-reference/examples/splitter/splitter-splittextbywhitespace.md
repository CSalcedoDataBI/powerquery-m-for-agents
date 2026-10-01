<!-- lab: desktop 2.157.879.0 -->

# Splitter.SplitTextByWhitespace

These examples show how quote characters, the optional quote style, and a null quote-style argument change the split.

Without a quote style, quotes still group: the quoted run keeps its double space as one item.

```m
Splitter.SplitTextByWhitespace()("a ""b  c"" d")
```

```text
{"a", "b  c", "d"}
```

Passing `QuoteStyle.Csv` keeps a quoted section, including its internal whitespace, together as one item.

```m
Splitter.SplitTextByWhitespace(QuoteStyle.Csv)("a ""b c"" d")
```

```text
{"a", "b c", "d"}
```

A null quote style behaves like the default, a tab separates items too, and the quotes around `c` are removed.

```m
Splitter.SplitTextByWhitespace(null)("a#(tab)b ""c""")
```

```text
{"a", "b", "c"}
```

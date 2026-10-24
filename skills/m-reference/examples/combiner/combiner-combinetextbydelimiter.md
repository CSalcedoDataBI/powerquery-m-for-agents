<!-- lab: desktop 2.159.883.0 -->

# Combiner.CombineTextByDelimiter

The function returns a combiner, which is applied to a list to show how nulls, delimiters inside values and quoteStyle change the joined text.

```m
Combiner.CombineTextByDelimiter(",")({"a", null, "c"})
```

```text
"a,,c"
```

Without quoteStyle, a value that contains the delimiter or a quote character may be quoted.

```m
Combiner.CombineTextByDelimiter(",")({"a,b", "say ""hi""", "c"})
```

```text
"""a,b"",""say """"hi"""""",c"
```

With QuoteStyle.None, the same values are joined as they are.

```m
Combiner.CombineTextByDelimiter(",", QuoteStyle.None)({"a,b", "say ""hi""", "c"})
```

```text
"a,b,say ""hi"",c"
```

<!-- lab: desktop 2.159.883.0 -->

# Lines.FromText

The examples show how line breaks split, how CSV quoting can keep a break inside one line, and how to keep the separators.

CR, LF and CRLF all split a line. This block also shows how an empty line and a trailing break are handled.

```m
Lines.FromText("a#(cr)#(lf)b#(lf)#(lf)c#(cr)")
```

```text
{"a", "b", "", "c"}
```

With QuoteStyle.Csv, a line break inside double quotes does not start a new line.

```m
Lines.FromText("x,""line#(lf)break""#(lf)y", QuoteStyle.Csv)
```

```text
{"x,""line#(lf)break""", "y"}
```

When includeLineSeparators is true, each line keeps its own break characters. Pass null for quoteStyle to skip it.

```m
Lines.FromText("a#(cr)#(lf)b#(lf)c", null, true)
```

```text
{"a#(cr)#(lf)", "b#(lf)", "c"}
```

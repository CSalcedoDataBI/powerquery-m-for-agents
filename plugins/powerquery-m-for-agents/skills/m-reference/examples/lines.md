<!-- lab: desktop 2.159.883.0 -->

# Executed examples: lines

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Lines.FromBinary

The examples show mixed line breaks, quoted line breaks, trailing separators and the encoding argument.

```m
Lines.FromBinary(Text.ToBinary("a#(cr,lf)b#(lf)c#(cr)d"))
```

```text
{"a", "b", "c", "d"}
```

```m
[
    NoQuoteStyle = Lines.FromBinary(Text.ToBinary("x,""1#(lf)2""#(lf)y")),
    CsvQuoteStyle = Lines.FromBinary(Text.ToBinary("x,""1#(lf)2""#(lf)y"), QuoteStyle.Csv)
]
```

```text
[NoQuoteStyle = {"x,""1", "2""", "y"}, CsvQuoteStyle = {"x,""1#(lf)2""", "y"}]
```

```m
[
    TrailingBreak = Lines.FromBinary(Text.ToBinary("a#(cr,lf)b#(cr,lf)")),
    WithSeparators = Lines.FromBinary(Text.ToBinary("a#(cr,lf)b#(cr,lf)"), null, true),
    Utf16AsDefault = Lines.FromBinary(Text.ToBinary("é#(lf)ü", TextEncoding.Utf16)),
    Utf16Declared = Lines.FromBinary(Text.ToBinary("é#(lf)ü", TextEncoding.Utf16), null, null, TextEncoding.Utf16)
]
```

```text
[TrailingBreak = {"a", "b"}, WithSeparators = {"a#(cr)#(lf)", "b#(cr)#(lf)"}, Utf16AsDefault = {"�#(0000)", "#(0000)�#(0000)"}, Utf16Declared = {"é", "ü"}]
```

## Lines.FromText

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

## Lines.ToBinary

The separator is added after every line, including the last, and the encoding and byte order mark change the bytes.

```m
Binary.ToList(Lines.ToBinary({"a", "b"}))
```

```text
{97, 13, 10, 98, 13, 10}
```

```m
Text.FromBinary(Lines.ToBinary({"a", null, "c"}, "|"))
```

```text
error: Expression.Error: We cannot convert the value null to type Text. | Detail: [Value = null, Type = type text]
```

```m
Binary.ToList(Lines.ToBinary({"é"}, null, TextEncoding.Utf8, true))
```

```text
{239, 187, 191, 195, 169, 13, 10}
```

## Lines.ToText

The separator follows every line, including the last one.

```m
Lines.ToText({"a", "b", "c"})
```

```text
"a#(cr)#(lf)b#(cr)#(lf)c#(cr)#(lf)"
```

A custom separator also trails the last line.

```m
Lines.ToText({"a", "b", "c"}, ", ")
```

```text
"a, b, c, "
```

A null separator, an empty list and a list holding one empty string.

```m
[NullSeparator = Lines.ToText({"a", "b"}, null), EmptyList = Lines.ToText({}), OneEmptyLine = Lines.ToText({""}, "|")]
```

```text
[NullSeparator = "a#(cr)#(lf)b#(cr)#(lf)", EmptyList = "", OneEmptyLine = "|"]
```

<!-- lab: desktop 2.159.883.0 -->

# Lines.FromBinary

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

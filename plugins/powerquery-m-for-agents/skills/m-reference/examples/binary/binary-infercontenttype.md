<!-- lab: desktop 2.157.879.0 -->

# Binary.InferContentType

Even a short phrase with one comma is reported as CSV, and the record lists every delimiter that
was tried with the columns and rows each would give. A null source is an error.

```m
Binary.InferContentType(Text.ToBinary("Hello, world"))
```

```text
[#"Content.Type" = "text/csv", #"Csv.PotentialDelimiters" = #table(type table [PotentialDelimiter = any, QuoteStyle = any, MaxColumns = any, NonEmptyColumns = any, MaxRows = any, NonEmptyRows = any], {{",", 0, 2, 2, 1, 1}, {",", 1, 2, 2, 1, 1}, {"#(tab)", 0, 1, 1, 1, 1}, {"#(tab)", 1, 1, 1, 1, 1}, {";", 0, 1, 1, 1, 1}, {";", 1, 1, 1, 1, 1}, {":", 0, 1, 1, 1, 1}, {":", 1, 1, 1, 1, 1}, {"|", 0, 1, 1, 1, 1}, {"|", 1, 1, 1, 1, 1}, {"#(0001)", 0, 1, 1, 1, 1}, {"#(0001)", 1, 1, 1, 1, 1}, {"W", 0, 2, 2, 1, 1}, {"W", 1, 2, 2, 1, 1}})]
```

```m
Binary.InferContentType(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

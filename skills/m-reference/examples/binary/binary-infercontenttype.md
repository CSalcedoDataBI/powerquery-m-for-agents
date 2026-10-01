<!-- lab: desktop 2.157.879.0 -->

# Binary.InferContentType

The record has two fields: the content type, and a table of every delimiter that was tried with
the columns and rows each would give. Even a short phrase with one comma is reported as CSV. A
null source is an error.

```m
Record.FieldNames(Binary.InferContentType(Text.ToBinary("Name,Age#(lf)Alice,30#(lf)Bob,25")))
```

```text
{"Content.Type", "Csv.PotentialDelimiters"}
```

```m
Record.FieldValues(Binary.InferContentType(Text.ToBinary("Hello, world"))){0}
```

```text
"text/csv"
```

```m
Binary.InferContentType(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

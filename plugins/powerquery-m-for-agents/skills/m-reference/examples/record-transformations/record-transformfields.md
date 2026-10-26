<!-- lab: desktop 2.157.879.0 -->

# Record.TransformFields

The examples show the flat single-field form, the list-of-lists form for several fields, and how null and missing values are handled.

A single field takes a flat two-item list, and the other fields are left alone.

```m
Record.TransformFields([Price = "100", Currency = "usd"], {"Price", Number.FromText})
```

```text
[Price = 100, Currency = "usd"]
```

Several fields take a list of pairs, and a null field stays null under a Text function.

```m
Record.TransformFields(
    [Code = "ab-12", Qty = "3", Note = null],
    {{"Code", Text.Upper}, {"Qty", Number.FromText}, {"Note", Text.Trim}}
)
```

```text
[Code = "AB-12", Qty = 3, Note = null]
```

A field named in the operations but absent from the record is skipped when the optional third argument is MissingField.Ignore.

```m
Record.TransformFields(
    [First = "ada", Last = "lovelace"],
    {{"First", Text.Proper}, {"Last", Text.Proper}, {"Title", Text.Proper}},
    MissingField.Ignore
)
```

```text
[First = "Ada", Last = "Lovelace"]
```

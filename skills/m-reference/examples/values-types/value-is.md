<!-- lab: desktop 2.159.883.0 -->

# Value.Is

Null is only compatible with nullable types, facets such as Int64.Type are not checked, and structured types are matched only on their primitive kind.

```m
[
    NullAsNumber = Value.Is(null, type number),
    NullAsNullableNumber = Value.Is(null, type nullable number),
    NullAsAny = Value.Is(null, type any),
    NullAsNull = Value.Is(null, type null)
]
```

```text
[NullAsNumber = false, NullAsNullableNumber = true, NullAsAny = true, NullAsNull = true]
```

```m
[
    FractionAsInt64 = Value.Is(1.5, Int64.Type),
    TextAsNumber = Value.Is("1", type number),
    DateAsDateTime = Value.Is(#date(1990, 1, 1), type datetime),
    DateTimeAsDate = Value.Is(#datetime(1990, 1, 1, 0, 0, 0), type date)
]
```

```text
[FractionAsInt64 = true, TextAsNumber = false, DateAsDateTime = false, DateTimeAsDate = false]
```

```m
[
    RecordWrongFields = Value.Is([a = 1], type [b = text]),
    TableWrongColumns = Value.Is(#table({"A"}, {{1}}), type table [B = text]),
    ListOfTextAsListOfNumber = Value.Is({"x"}, type {number}),
    FunctionAsFunction = Value.Is(Text.Upper, type function)
]
```

```text
[RecordWrongFields = true, TableWrongColumns = true, ListOfTextAsListOfNumber = true, FunctionAsFunction = true]
```

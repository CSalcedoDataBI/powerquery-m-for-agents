<!-- lab: desktop 2.159.883.0 -->

# Executed examples: values-types

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Value.As

Value.As only checks the type and never converts, so a mismatch is an error.

```m
try Value.As("1", type number)
```

```text
[HasError = true, Error = [Reason = "Expression.Error", Message = "We cannot convert the value ""1"" to type Number.", Detail = [Value = "1", Type = type number], #"Message.Format" = "We cannot convert the value #{0} to type #{1}.", #"Message.Parameters" = {"""1""", "Number"}, ErrorCode = "10277"]]
```

Null fails a plain `number` check but passes `nullable number`.

```m
[Plain = try Value.As(null, type number), Nullable = try Value.As(null, type nullable number)]
```

```text
[Plain = [HasError = true, Error = [Reason = "Expression.Error", Message = "We cannot convert the value null to type Number.", Detail = [Value = null, Type = type number], #"Message.Format" = "We cannot convert the value #{0} to type #{1}.", #"Message.Parameters" = {"null", "Number"}, ErrorCode = "10277"]], Nullable = [HasError = false, Value = null]]
```

Only the outer kind is checked. A list of text passes a list-of-number type.

```m
Value.As({"a", "b"}, type {number})
```

```text
{"a", "b"}
```

## Value.Is

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

## Value.ReplaceType

The new type is attached to the value without converting it. Column names change by position, values keep their own type, and an incompatible type is an error.

```m
Value.ReplaceType(#table({"A", "B"}, {{1, 2}}), type table [X = number, Y = number])
```

```text
#table(type table [X = number, Y = number], {{1, 2}})
```

```m
let
    t = Value.ReplaceType(#table({"A"}, {{"1"}}), type table [A = number])
in
    [IsNumber = Value.Is(t{0}[A], type number), IsText = Value.Is(t{0}[A], type text)]
```

```text
[IsNumber = false, IsText = true]
```

```m
Value.ReplaceType(1, type text)
```

```text
error: Expression.Error: We cannot convert the value 1 to type Text. | Detail: [Value = 1, Type = type text]
```

<!-- lab: desktop 2.159.883.0 -->

# Value.RemoveMetadata

These examples show what metadata survives removal, how the optional second argument behaves, and what happens with null.

```m
let
    Tagged = 5 meta [Unit = "kg", Source = "scale"],
    Stripped = Value.RemoveMetadata(Tagged)
in
    [Value = Stripped, Before = Value.Metadata(Tagged), After = Value.Metadata(Stripped)]
```

```text
[Value = 5, Before = [Unit = "kg", Source = "scale"], After = []]
```

Passing a record as the optional metaValue argument:

```m
let
    Tagged = "x" meta [A = 1, B = 2],
    Stripped = Value.RemoveMetadata(Tagged, [A = 1])
in
    [Value = Stripped, After = Value.Metadata(Stripped)]
```

```text
[Value = error: Expression.Error: We cannot convert a value of type Record to type List. | Detail: [Value = [A = 1], Type = type {any}], After = error: Expression.Error: We cannot convert a value of type Record to type List. | Detail: [Value = [A = 1], Type = type {any}]]
```

Metadata on null, and on a value that has no metadata:

```m
[
    NullValue = Value.RemoveMetadata(null meta [A = 1]),
    NullMeta = Value.Metadata(Value.RemoveMetadata(null meta [A = 1])),
    Plain = Value.Metadata(Value.RemoveMetadata(42))
]
```

```text
[NullValue = null, NullMeta = [], Plain = []]
```

<!-- lab: desktop 2.159.883.0 -->

# Executed examples: metadata

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Value.Metadata

These examples show what metadata is kept, merged or lost.

```m
Value.Metadata(42)
```

```text
[]
```

Stacked `meta` merges the records, and the later field wins on a name clash.

```m
Value.Metadata(((1 meta [A = 1, B = 1]) meta [B = 2, C = 3]))
```

```text
[A = 1, B = 2, C = 3]
```

Arithmetic returns a new value, so the result has no metadata.

```m
Value.Metadata((1 meta [A = 1]) + 1)
```

```text
[]
```

## Value.RemoveMetadata

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

## Value.ReplaceMetadata

The new record replaces the existing metadata rather than merging with it, as the `meta` operator does.

```m
[
    Replaced = Value.Metadata(Value.ReplaceMetadata(1 meta [A = 1], [B = 2])),
    Merged = Value.Metadata((1 meta [A = 1]) meta [B = 2])
]
```

```text
[Replaced = [B = 2], Merged = [A = 1, B = 2]]
```

An empty record clears all metadata. The value itself is unchanged.

```m
[
    Cleared = Value.Metadata(Value.ReplaceMetadata("x" meta [A = 1], [])),
    SameValue = Value.ReplaceMetadata("x" meta [A = 1], [B = 2]) = "x"
]
```

```text
[Cleared = [], SameValue = true]
```

A null metaValue also clears the metadata, giving the same empty record `[]` as passing an empty record.

```m
Value.Metadata(Value.ReplaceMetadata(1 meta [A = 1], null))
```

```text
[]
```

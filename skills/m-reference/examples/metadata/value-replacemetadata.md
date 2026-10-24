<!-- lab: desktop 2.159.883.0 -->

# Value.ReplaceMetadata

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

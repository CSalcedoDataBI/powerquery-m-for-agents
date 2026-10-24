<!-- lab: desktop 2.159.883.0 -->

# Value.Metadata

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

<!-- lab: desktop 2.159.883.0 -->

# Value.Type

A literal's type is the base kind only. Ascribed types come back unchanged, and the field types of a record literal are not inferred from their values.

```m
{Value.Type(1), Value.Type(1.5), Value.Type(null), Value.Type(#date(1990, 1, 1)), Value.Type("1")}
```

```text
{type number, type number, type null, type date, type text}
```

```m
Type.ListItem(Value.Type(Value.ReplaceType({1, 2}, type {number})))
```

```text
type number
```

```m
Type.RecordFields(Value.Type([A = 1, B = "x"]))
```

```text
[A = [Type = type any, Optional = false], B = [Type = type any, Optional = false]]
```

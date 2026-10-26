<!-- lab: desktop 2.157.879.0 -->

# Type.RecordFields

Optional fields are flagged separately from `nullable`, which stays inside each field's `Type`.

```m
Type.RecordFields(type [A = number, optional B = any])
```

```text
[A = [Type = type number, Optional = false], B = [Type = type any, Optional = true]]
```

```m
Type.RecordFields(type [A = nullable text, optional B = nullable text])
```

```text
[A = [Type = type nullable text, Optional = false], B = [Type = type nullable text, Optional = true]]
```

```m
Type.RecordFields(type [])
```

```text
[]
```

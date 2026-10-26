<!-- lab: desktop 2.157.879.0 -->

# Type.ForRecord

`Value.Is` against a record type built here checks only that the value is a record: field types,
nullability and openness are not checked. All four are `true`, the last one with a number in a
text field.

```m
Value.Is([Name = null], Type.ForRecord([Name = [Type = type text, Optional = true]], false))
```

```text
true
```

```m
Value.Is([Name = null], Type.ForRecord([Name = [Type = type nullable text, Optional = false]], false))
```

```text
true
```

```m
Value.Is([Name = "x", Age = 1], Type.ForRecord([Name = [Type = type text, Optional = false]], true))
```

```text
true
```

```m
Value.Is([Name = 1], Type.ForRecord([Name = [Type = type text, Optional = false]], false))
```

```text
true
```

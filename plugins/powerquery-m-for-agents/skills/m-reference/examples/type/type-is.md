<!-- lab: desktop 2.157.879.0 -->

# Type.Is

Nullability is part of the check, and `null` has its own type.

```m
Type.Is(type number, type nullable number)
```

```text
true
```

```m
Type.Is(type nullable number, type number)
```

```text
false
```

```m
Type.Is(type null, type nullable number)
```

```text
true
```

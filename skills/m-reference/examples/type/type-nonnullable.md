<!-- lab: desktop 2.157.879.0 -->

# Type.NonNullable

The examples show that `Type.NonNullable` removes only the outer `nullable` marker, leaving an already non-nullable type and any element nullability untouched.

```m
Type.NonNullable(type nullable number)
```

```text
type number
```

```m
Type.NonNullable(type number)
```

```text
type number
```

```m
Type.NonNullable(type nullable {nullable number})
```

```text
type {nullable number}
```

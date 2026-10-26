<!-- lab: desktop 2.157.879.0 -->

# Type.IsNullable

Nullability is a flag on the type itself, which is not the same as whether the type admits null values.

```m
Type.IsNullable(type number)
```

```text
false
```

```m
Type.IsNullable(type nullable number)
```

```text
true
```

```m
Type.IsNullable(type any)
```

```text
true
```

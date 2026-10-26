<!-- lab: desktop 2.157.879.0 -->

# Type.Union

These examples show how Type.Union treats nullability, incompatible primitives, and an empty list.

```m
Type.Union({type text, type nullable text})
```

```text
type nullable text
```

```m
Type.Union({type text, type number})
```

```text
type any
```

```m
Type.Union({})
```

```text
type none
```

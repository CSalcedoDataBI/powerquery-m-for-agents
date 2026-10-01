<!-- lab: desktop 2.157.879.0 -->

# Type.ListItem

The item type retains nullability.

```m
Type.ListItem(type {nullable number})
```

```text
type nullable number
```

A plain `type list` has items of type `any`.

```m
Type.ListItem(type list)
```

```text
type any
```

Nested list types return the inner list type.

```m
Type.ListItem(type {{number}})
```

```text
type {number}
```

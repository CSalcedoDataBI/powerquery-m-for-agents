<!-- lab: desktop 2.157.879.0 -->

# Logical.From

The examples show null and logical passthrough, zero-versus-nonzero numbers, and uppercase text.

```m
List.Transform({null, true}, Logical.From)
```

```text
{null, true}
```

```m
List.Transform({0, -1, 0.5}, Logical.From)
```

```text
{false, true, true}
```

```m
Logical.From("TRUE")
```

```text
true
```

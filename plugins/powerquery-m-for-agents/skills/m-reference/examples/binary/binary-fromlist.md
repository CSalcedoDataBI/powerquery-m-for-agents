<!-- lab: desktop 2.157.879.0 -->

# Binary.FromList

The examples cover an empty list, the 0 and 255 byte boundaries, and a null entry.

```m
Binary.FromList({})
```

```text
#binary({})
```

```m
Binary.FromList({0, 255})
```

```text
#binary({0, 255})
```

```m
Binary.FromList({0, null, 255})
```

```text
error: Expression.Error: We cannot convert the value null to type Number. | Detail: [Value = null, Type = type number]
```

<!-- lab: desktop 2.157.879.0 -->

# Binary.ToList

The examples show byte-to-number conversion, the empty binary, and null handling.

```m
Binary.ToList(#binary({0x00, 0x7F, 0xFF}))
```

```text
{0, 127, 255}
```

```m
Binary.ToList(#binary({}))
```

```text
{}
```

```m
Binary.ToList(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

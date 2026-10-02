<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.Single

BinaryFormat.Single reads big-endian by default: the little-endian bytes of 1.0 give a tiny subnormal, and the same bytes reversed give 1. A null binary is an error.

```m
BinaryFormat.Single(#binary({0x00, 0x00, 0x80, 0x3F}))
```

```text
4.6006029882248069E-41
```

```m
BinaryFormat.Single(#binary({0x3F, 0x80, 0x00, 0x00}))
```

```text
1
```

```m
BinaryFormat.Single(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

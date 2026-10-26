<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.7BitEncodedSignedInteger

The 7-bit value is zigzag-encoded: even raw values are positive, odd ones negative. The raw
value 64 reads as 32; a redundant continuation byte (0xC0, 0x00) carries the same raw 64, so
it reads as 32 too; and the raw value 1 is -1. A null binary is an error.

```m
BinaryFormat.7BitEncodedSignedInteger(#binary({0x40}))
```

```text
32
```

```m
BinaryFormat.7BitEncodedSignedInteger(#binary({0xC0, 0x00}))
```

```text
32
```

```m
BinaryFormat.7BitEncodedSignedInteger(#binary({0x01}))
```

```text
-1
```

```m
BinaryFormat.7BitEncodedSignedInteger(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.7BitEncodedUnsignedInteger

The examples show null input and multi-byte 7-bit decoding.

```m
BinaryFormat.7BitEncodedUnsignedInteger(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

The high bit is a continuation flag, so the first byte's 172 is not the value; the pair decodes to 300.

```m
BinaryFormat.7BitEncodedUnsignedInteger(#binary({0xAC, 0x02}))
```

```text
300
```

The largest unsigned 64-bit value needs ten bytes, the last one holding a single payload bit.

```m
BinaryFormat.7BitEncodedUnsignedInteger(#binary({0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x01}))
```

```text
18446744073709551615
```

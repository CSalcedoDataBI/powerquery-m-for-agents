<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.UnsignedInteger32

The examples show the all-ones unsigned value, big-endian versus little-endian reads, and null input.

```m
BinaryFormat.UnsignedInteger32(#binary({0xFF, 0xFF, 0xFF, 0xFF}))
```

```text
4294967295
```

```m
[
    defaultByteOrder = BinaryFormat.UnsignedInteger32(#binary({0x01, 0x00, 0x00, 0x00})),
    littleEndian = BinaryFormat.ByteOrder(BinaryFormat.UnsignedInteger32, ByteOrder.LittleEndian)(#binary({0x01, 0x00, 0x00, 0x00}))
]
```

```text
[defaultByteOrder = 16777216, littleEndian = 1]
```

```m
BinaryFormat.UnsignedInteger32(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

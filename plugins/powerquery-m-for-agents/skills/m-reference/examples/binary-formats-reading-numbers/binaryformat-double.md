<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.Double

An 8-byte IEEE double, read big-endian unless BinaryFormat.ByteOrder says otherwise. The
input is a binary value, not a hex number literal. Negative zero reads back as 0.

```m
BinaryFormat.Double(#binary({0x3F, 0xF0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00}))
```

```text
1
```

```m
BinaryFormat.ByteOrder(BinaryFormat.Double, ByteOrder.LittleEndian)(#binary({0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF0, 0x3F}))
```

```text
1
```

```m
let
    LE = (bytes) => BinaryFormat.ByteOrder(BinaryFormat.Double, ByteOrder.LittleEndian)(Binary.FromList(bytes))
in
    [
        SmallestPositive = LE({1, 0, 0, 0, 0, 0, 0, 0}),
        NegativeZero = LE({0, 0, 0, 0, 0, 0, 0, 0x80}),
        PositiveInfinity = LE({0, 0, 0, 0, 0, 0, 0xF0, 0x7F}),
        NaN = LE({0, 0, 0, 0, 0, 0, 0xF8, 0x7F})
    ]
```

```text
[SmallestPositive = 4.94065645841247E-324, NegativeZero = 0, PositiveInfinity = #infinity, NaN = #nan]
```

```m
BinaryFormat.Double(0x3FF0000000000000)
```

```text
error: Expression.Error: We cannot convert the value 4607182418800017408 to type Binary. | Detail: [Value = 4607182418800017408, Type = type binary]
```

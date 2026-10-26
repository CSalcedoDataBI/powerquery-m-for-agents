<!-- lab: desktop 2.157.879.0 -->

# Executed examples: binary-formats-reading-numbers

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## BinaryFormat.7BitEncodedSignedInteger

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

## BinaryFormat.7BitEncodedUnsignedInteger

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

## BinaryFormat.Byte

Reads one byte from a binary, and rejects empty or null input.

```m
BinaryFormat.Byte(#binary({0xFF, 0x00}))
```

```text
255
```

```m
BinaryFormat.Byte(#binary({}))
```

```text
error: DataFormat.Error: There was a problem reading the binary format at position 0.  The end of the input was reached before the value could be read.
```

```m
BinaryFormat.Byte(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

## BinaryFormat.Decimal

These examples show how the .NET decimal's scale byte and null input affect the value returned.

```m
BinaryFormat.Decimal(#binary({1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}))
```

```text
1
```

```m
BinaryFormat.Decimal(#binary({1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0}))
```

```text
0.1
```

```m
BinaryFormat.Decimal(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

## BinaryFormat.Double

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

## BinaryFormat.SignedInteger16

Two bytes are read as a signed 16-bit integer, so byte order and the sign bit both change the value.

```m
BinaryFormat.SignedInteger16(#binary({0xFF, 0xFF}))
```

```text
-1
```

```m
BinaryFormat.List(BinaryFormat.SignedInteger16)(#binary({0x01, 0x00, 0x00, 0x01}))
```

```text
{256, 1}
```

```m
BinaryFormat.SignedInteger16(#binary({0x7F}))
```

```text
error: DataFormat.Error: There was a problem reading the binary format at position 1.  The end of the input was reached before the value could be read.
```

## BinaryFormat.SignedInteger32

A signed read uses the high bit as a sign, needs all four bytes, and does not treat null as zero.

```m
BinaryFormat.SignedInteger32(Binary.FromList({255, 255, 255, 255}))
```

```text
-1
```

```m
BinaryFormat.SignedInteger32(Binary.FromList({0, 0, 0}))
```

```text
error: DataFormat.Error: There was a problem reading the binary format at position 3.  The end of the input was reached before the value could be read.
```

```m
BinaryFormat.SignedInteger32(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

## BinaryFormat.SignedInteger64

Eight bytes are read in big-endian order, with the first byte holding the highest-order bits.

```m
BinaryFormat.SignedInteger64(#binary({0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2A}))
```

```text
42
```

Negative values use two's complement, so all eight bytes set to `0xFF` decode to -1 rather than a large positive integer.

```m
BinaryFormat.SignedInteger64(#binary({0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF}))
```

```text
-1
```

Setting only the high bit gives the minimum 64-bit value, not zero.

```m
BinaryFormat.SignedInteger64(#binary({0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00}))
```

```text
-9223372036854775808
```

## BinaryFormat.Single

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

## BinaryFormat.UnsignedInteger16

These examples show how the format reads a 16-bit unsigned integer, what a short binary does, and how null is treated.

```m
BinaryFormat.UnsignedInteger16(#binary({0x01, 0x00}))
```

```text
256
```

A binary with fewer than two bytes is too short.

```m
BinaryFormat.UnsignedInteger16(#binary({0x01}))
```

```text
error: DataFormat.Error: There was a problem reading the binary format at position 1.  The end of the input was reached before the value could be read.
```

A null binary is not a zero value.

```m
BinaryFormat.UnsignedInteger16(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

## BinaryFormat.UnsignedInteger32

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

## BinaryFormat.UnsignedInteger64

These examples show byte order, the maximum unsigned value, and null or short binary inputs.

```m
BinaryFormat.UnsignedInteger64(#binary({0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08}))
```

```text
72623859790382856
```

```m
BinaryFormat.UnsignedInteger64(#binary({0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF}))
```

```text
18446744073709551615
```

```m
List.Transform({null, #binary({0x01, 0x02, 0x03})}, (b) => (try BinaryFormat.UnsignedInteger64(b) otherwise "invalid binary"))
```

```text
{"invalid binary", "invalid binary"}
```

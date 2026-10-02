<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.ByteOrder

The examples show how the byte order changes the value read from identical bytes.

Little endian treats the first byte as the least significant.

```m
BinaryFormat.ByteOrder(BinaryFormat.UnsignedInteger16, ByteOrder.LittleEndian)(#binary({0x01, 0x02}))
```

```text
513
```

Big endian treats the first byte as the most significant, matching the default used when no order is specified.

```m
BinaryFormat.ByteOrder(BinaryFormat.UnsignedInteger16, ByteOrder.BigEndian)(#binary({0x01, 0x02}))
```

```text
258
```

A single-byte format accepts a byte order argument but the choice cannot change the value.

```m
BinaryFormat.ByteOrder(BinaryFormat.Byte, ByteOrder.LittleEndian)(#binary({0x2A}))
```

```text
42
```

<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.SignedInteger64

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

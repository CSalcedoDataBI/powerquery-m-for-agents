<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.Binary

BinaryFormat.Binary returns a format, a function of one binary. Its optional length decides
how many bytes the format reads: omitted or null reads to the end, a number reads that many,
and a binary format reads the length first from the data.

```m
[
    Omitted = BinaryFormat.Binary()(#binary({0x01, 0x02, 0x03})),
    NullLength = BinaryFormat.Binary(null)(#binary({0x01, 0x02, 0x03})),
    ZeroLength = BinaryFormat.Binary(0)(#binary({0x01, 0x02, 0x03}))
]
```

```text
[Omitted = #binary({1, 2, 3}), NullLength = #binary({1, 2, 3}), ZeroLength = #binary({})]
```

```m
BinaryFormat.Binary(2)(#binary({0x01, 0x02, 0x03, 0x04}))
```

```text
#binary({1, 2})
```

```m
[
    TwoBytes = BinaryFormat.Binary(BinaryFormat.Byte)(#binary({0x02, 0x0A, 0x0B, 0x0C})),
    ZeroBytes = BinaryFormat.Binary(BinaryFormat.Byte)(#binary({0x00, 0x0A}))
]
```

```text
[TwoBytes = #binary({10, 11}), ZeroBytes = #binary({})]
```

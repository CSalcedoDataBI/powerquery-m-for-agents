<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.UnsignedInteger64

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

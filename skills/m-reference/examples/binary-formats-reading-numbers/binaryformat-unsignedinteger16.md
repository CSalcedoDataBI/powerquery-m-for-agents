<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.UnsignedInteger16

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

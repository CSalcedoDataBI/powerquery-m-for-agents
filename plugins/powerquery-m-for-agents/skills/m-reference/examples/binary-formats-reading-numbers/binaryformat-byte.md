<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.Byte

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

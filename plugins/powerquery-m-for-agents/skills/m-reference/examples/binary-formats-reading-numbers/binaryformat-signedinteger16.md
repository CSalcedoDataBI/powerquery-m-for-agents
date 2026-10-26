<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.SignedInteger16

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

<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.SignedInteger32

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

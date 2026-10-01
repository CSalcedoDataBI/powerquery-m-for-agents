<!-- lab: desktop 2.157.879.0 -->

# Binary.Decompress

A null binary stays null, and the compression type must match the one used to compress the data. A mismatch fails only when the bytes are read, so `try ... otherwise` around the call does not catch it.

```m
Binary.Decompress(null, Compression.Deflate)
```

```text
null
```

```m
Binary.Decompress(Binary.Compress(#binary({1, 2, 3}), Compression.GZip), Compression.GZip)
```

```text
#binary({1, 2, 3})
```

```m
try Binary.Decompress(Binary.Compress(#binary({1, 2, 3}), Compression.GZip), Compression.Deflate) otherwise "wrong compression type"
```

```text
error: DataFormat.Error: Found invalid data while decoding.
```

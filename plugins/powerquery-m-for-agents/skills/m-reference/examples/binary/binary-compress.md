<!-- lab: desktop 2.157.879.0 -->

# Binary.Compress

Null input comes back as null, and the compression type selects the output container.

```m
Binary.Compress(null, Compression.Deflate)
```

```text
null
```

An empty binary compresses to an empty binary: no header or framing bytes are added.

```m
Binary.Compress(#binary({}), Compression.GZip)
```

```text
#binary({})
```

GZip output starts with the GZip header bytes 31 and 139; a raw deflate stream has no header.

```m
Binary.ToList(Binary.Range(Binary.Compress(Text.ToBinary("Power Query"), Compression.GZip), 0, 2))
```

```text
{31, 139}
```

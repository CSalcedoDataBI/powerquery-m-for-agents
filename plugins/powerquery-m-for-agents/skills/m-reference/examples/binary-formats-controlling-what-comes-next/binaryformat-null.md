<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.Null

These examples show that BinaryFormat.Null returns null and consumes no bytes, even for an empty binary or before another format.

```m
{BinaryFormat.Null(Binary.FromList({})), BinaryFormat.Null(Binary.FromList({1, 2, 3}))}
```

```text
{null, null}
```

```m
BinaryFormat.Record([ignored = BinaryFormat.Null, number = BinaryFormat.UnsignedInteger16])(Binary.FromList({0, 65}))
```

```text
[ignored = null, number = 65]
```

<!-- lab: desktop 2.157.879.0 -->

# Binary.ApproximateLength

A null input returns null rather than 0, and lengths count bytes, not characters.

```m
Binary.ApproximateLength(null)
```

```text
null
```

```m
Binary.ApproximateLength(Binary.FromText("", BinaryEncoding.Base64))
```

```text
0
```

```m
Binary.ApproximateLength(Binary.FromText("aGVsbG8=", BinaryEncoding.Base64))
```

```text
5
```

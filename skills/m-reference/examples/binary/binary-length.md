<!-- lab: desktop 2.157.879.0 -->

# Binary.Length

Null input returns null, while an empty binary has length zero.

```m
Binary.Length(null)
```

```text
null
```

```m
Binary.Length(Text.ToBinary("Seattle"))
```

```text
7
```

```m
Binary.Length(Text.ToBinary(""))
```

```text
0
```

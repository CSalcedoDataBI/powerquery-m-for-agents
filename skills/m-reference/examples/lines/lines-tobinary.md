<!-- lab: desktop 2.159.883.0 -->

# Lines.ToBinary

The separator is added after every line, including the last, and the encoding and byte order mark change the bytes.

```m
Binary.ToList(Lines.ToBinary({"a", "b"}))
```

```text
{97, 13, 10, 98, 13, 10}
```

```m
Text.FromBinary(Lines.ToBinary({"a", null, "c"}, "|"))
```

```text
error: Expression.Error: We cannot convert the value null to type Text. | Detail: [Value = null, Type = type text]
```

```m
Binary.ToList(Lines.ToBinary({"é"}, null, TextEncoding.Utf8, true))
```

```text
{239, 187, 191, 195, 169, 13, 10}
```

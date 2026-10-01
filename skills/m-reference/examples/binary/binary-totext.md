<!-- lab: desktop 2.157.879.0 -->

# Binary.ToText

The examples show null input, what omitting `encoding` produces, and the Hex alternative.

```m
Binary.ToText(null)
```

```text
null
```

```m
Binary.ToText(Binary.FromList({72, 105}))
```

```text
"SGk="
```

```m
Binary.ToText(Binary.FromList({72, 105}), BinaryEncoding.Hex)
```

```text
"4869"
```

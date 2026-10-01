<!-- lab: desktop 2.157.879.0 -->

# Binary.FromText

These examples show null propagation and how the same text is decoded differently when the optional encoding argument is omitted versus set to Hex.

```m
Binary.FromText(null)
```

```text
null
```

```m
Binary.FromText("1011")
```

```text
#binary({215, 77, 117})
```

```m
Binary.FromText("1011", BinaryEncoding.Hex)
```

```text
#binary({16, 17})
```

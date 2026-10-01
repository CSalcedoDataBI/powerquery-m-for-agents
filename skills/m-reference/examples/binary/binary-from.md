<!-- lab: desktop 2.157.879.0 -->

# Binary.From

These examples show how `Binary.From` treats null, text with an explicit encoding, and an existing binary value.

```m
Binary.From(null)
```

```text
null
```

The optional second argument decodes text using the given encoding instead of the default.

```m
Binary.From("1011", BinaryEncoding.Hex)
```

```text
#binary({16, 17})
```

A binary value is returned unchanged rather than decoded again.

```m
Binary.From(Binary.FromText("1011", BinaryEncoding.Hex))
```

```text
#binary({16, 17})
```

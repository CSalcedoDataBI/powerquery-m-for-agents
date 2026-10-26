<!-- lab: desktop 2.157.879.0 -->

# Binary.Buffer

Null passes through, empty inputs stay empty, and a buffered value keeps every byte in order.

```m
Binary.Buffer(null)
```

```text
null
```

Buffering an empty binary gives an empty binary, not null.

```m
Binary.Buffer(Binary.FromList({}))
```

```text
#binary({})
```

Zero is a real byte value, so zero bytes survive buffering.

```m
Binary.Buffer(Binary.FromList({0, 0, 255}))
```

```text
#binary({0, 0, 255})
```

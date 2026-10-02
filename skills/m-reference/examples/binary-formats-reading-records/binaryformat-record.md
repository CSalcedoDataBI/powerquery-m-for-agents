<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.Record

The examples show that non-binary-format field values are echoed without consuming bytes, that `null` survives the same way, and that nested record formats read their fields in order.

```m
let
    binaryData = #binary({0x05, 0x06}),
    recordFormat = BinaryFormat.Record([
        A = BinaryFormat.Byte,
        Label = "constant",
        B = BinaryFormat.Byte
    ])
in
    recordFormat(binaryData)
```

```text
[A = 5, Label = "constant", B = 6]
```

```m
let
    binaryData = #binary({0x01, 0x02}),
    recordFormat = BinaryFormat.Record([
        A = BinaryFormat.Byte,
        Nothing = null,
        B = BinaryFormat.Byte
    ])
in
    recordFormat(binaryData)
```

```text
[A = 1, Nothing = null, B = 2]
```

```m
let
    binaryData = #binary({0x0A, 0x0B}),
    innerFormat = BinaryFormat.Record([
        X = BinaryFormat.Byte,
        Y = BinaryFormat.Byte
    ]),
    outerFormat = BinaryFormat.Record([
        Pair = innerFormat
    ])
in
    outerFormat(binaryData)
```

```text
[Pair = [X = 10, Y = 11]]
```

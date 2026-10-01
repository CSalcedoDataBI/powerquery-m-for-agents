<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.Text

These examples show how BinaryFormat.Text uses byte counts, a length prefix, and an omitted or null encoding.

```m
let
    binaryData = #binary({195, 169, 65}),
    textFormat = BinaryFormat.Text(2)
in
    textFormat(binaryData)
```

```text
"é"
```

```m
let
    binaryData = #binary({2, 65, 66}),
    textFormat = BinaryFormat.Text(BinaryFormat.Byte, null)
in
    textFormat(binaryData)
```

```text
"AB"
```

```m
let
    binaryData = #binary({65, 66}),
    textFormat = BinaryFormat.Text(0, TextEncoding.Ascii)
in
    textFormat(binaryData)
```

```text
""
```

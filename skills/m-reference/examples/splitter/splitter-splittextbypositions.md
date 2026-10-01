<!-- lab: desktop 2.157.879.0 -->

# Splitter.SplitTextByPositions

A position can repeat, which gives an empty item.

```m
Splitter.SplitTextByPositions({0, 3, 3, 4})("ABC|12345")
```

```text
{"ABC", "", "|", "12345"}
```

With `startAtEnd` set to true, positions count from the end of the text.

```m
let
    startAtEnd = true
in
    Splitter.SplitTextByPositions({0, 5}, startAtEnd)("Redmond98052")
```

```text
{"Redmond", "98052"}
```

The optional argument also accepts null.

```m
let
    startAtEnd = null
in
    Splitter.SplitTextByPositions({0, 3, 4}, startAtEnd)("ABC|12345")
```

```text
{"ABC", "|", "12345"}
```

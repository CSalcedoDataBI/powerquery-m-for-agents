<!-- lab: desktop 2.157.879.0 -->

# Binary.View

Handlers are optional, handler errors fall back, and a null binary view needs GetStream.

```m
Binary.Length(Binary.View(Text.ToBinary("hello"), []))
```

```text
5
```

```m
Binary.Length(Binary.View(Text.ToBinary("hello"), [GetLength = () => Number.FromText("not a number")]))
```

```text
5
```

```m
Text.FromBinary(Binary.View(null, [GetLength = () => 12, GetStream = () => Text.ToBinary("hello world!")]))
```

```text
"hello world!"
```

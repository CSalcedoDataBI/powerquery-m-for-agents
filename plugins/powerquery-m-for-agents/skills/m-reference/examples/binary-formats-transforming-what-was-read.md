<!-- lab: desktop 2.157.879.0 -->

# Executed examples: binary-formats-transforming-what-was-read

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## BinaryFormat.Transform

These examples show the transform receiving the whole value read, honoring the wrapped format's optional count, and returning null.

```m
BinaryFormat.Transform(BinaryFormat.Byte, (x) => x + 1)(#binary({1}))
```

```text
2
```

```m
BinaryFormat.Transform(BinaryFormat.List(BinaryFormat.Byte, 2), List.Sum)(#binary({1, 2, 3}))
```

```text
3
```

```m
BinaryFormat.Transform(BinaryFormat.Byte, (x) => null)(#binary({1}))
```

```text
null
```

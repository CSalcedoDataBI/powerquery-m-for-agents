<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.List

These examples show when BinaryFormat.List stops reading: at the end of the data, on a condition, or after a count read from the data.

```m
BinaryFormat.List(BinaryFormat.Byte)(#binary({1, 2, 3}))
```

```text
{1, 2, 3}
```

```m
BinaryFormat.List(BinaryFormat.Byte, (x) => x < 2)(#binary({1, 2, 3}))
```

```text
{1, 2}
```

```m
BinaryFormat.List(BinaryFormat.Byte, BinaryFormat.Byte)(#binary({2, 10, 20, 30}))
```

```text
{10, 20}
```

<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.Length

These examples show a read capped to a fixed byte count, to a count taken from a preceding
length value, and to zero bytes. The format passed in must be a format value:
BinaryFormat.Binary on its own is the function that builds one, so it is refused.

```m
BinaryFormat.Length(BinaryFormat.List(BinaryFormat.Byte), 3)(#binary({1, 2, 3, 4, 5}))
```

```text
{1, 2, 3}
```

```m
BinaryFormat.Length(BinaryFormat.List(BinaryFormat.Byte), BinaryFormat.Byte)(#binary({2, 10, 20, 30}))
```

```text
{10, 20}
```

```m
BinaryFormat.Length(BinaryFormat.List(BinaryFormat.Byte), 0)(#binary({1, 2, 3}))
```

```text
{}
```

```m
BinaryFormat.Length(BinaryFormat.Binary, 3)(#binary({1, 2, 3, 4, 5}))
```

```text
error: Expression.Error: The value isn't a binary format value. | Detail: error: Expression.Error: Function.Type is abstract and has no defined parameters.
```

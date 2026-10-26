<!-- lab: desktop 2.157.879.0 -->

# Executed examples: binary-formats-controlling-what-comes-next

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## BinaryFormat.Choice

Without a combine function only the value of the chosen format comes back; the first value is read and discarded. With one, both reach it - but then the type argument must be null: `type list` is an error. The last block also shows a zero count choosing BinaryFormat.Null.

```m
let
    data = #binary({3, 10, 20, 30}),
    reader = BinaryFormat.Choice(
        BinaryFormat.Byte,
        (count) => BinaryFormat.List(BinaryFormat.Byte, count)
    )
in
    reader(data)
```

```text
{10, 20, 30}
```

```m
let
    data = #binary({3, 10, 20, 30}),
    reader = BinaryFormat.Choice(
        BinaryFormat.Byte,
        (count) => BinaryFormat.List(BinaryFormat.Byte, count),
        type list,
        (count, values) => [count = count, values = values]
    )
in
    reader(data)
```

```text
error: Expression.Error: A type of 'list' or 'binary' cannot be specified when using a combine function. | Detail: type {any}
```

```m
let
    data = #binary({0}),
    reader = BinaryFormat.Choice(
        BinaryFormat.Byte,
        (count) => if count = 0 then BinaryFormat.Null else BinaryFormat.List(BinaryFormat.Byte, count),
        null,
        (count, value) => [count = count, value = value]
    )
in
    reader(data)
```

```text
[count = 0, value = null]
```

## BinaryFormat.Null

These examples show that BinaryFormat.Null returns null and consumes no bytes, even for an empty binary or before another format.

```m
{BinaryFormat.Null(Binary.FromList({})), BinaryFormat.Null(Binary.FromList({1, 2, 3}))}
```

```text
{null, null}
```

```m
BinaryFormat.Record([ignored = BinaryFormat.Null, number = BinaryFormat.UnsignedInteger16])(Binary.FromList({0, 65}))
```

```text
[ignored = null, number = 65]
```

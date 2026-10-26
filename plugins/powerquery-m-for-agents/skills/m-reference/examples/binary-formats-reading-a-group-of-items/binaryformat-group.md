<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.Group

These examples show how item order, missing optional and repeating items, and unexpected keys are handled.

```m
let
    b = #binary({2, 22, 1, 11, 2, 33}),
    f = BinaryFormat.Group(
        BinaryFormat.Byte,
        {
            {1, BinaryFormat.Byte, BinaryOccurrence.Required},
            {2, BinaryFormat.Byte, BinaryOccurrence.Repeating, null, (list) => List.Sum(list)}
        }
    )
in
    f(b)
```

```text
{11, 55}
```

An absent optional item becomes null, an absent repeating item becomes `{ }`, and a supplied default is returned without the transform being called.

```m
let
    b = #binary({1, 11}),
    f = BinaryFormat.Group(
        BinaryFormat.Byte,
        {
            {1, BinaryFormat.Byte, BinaryOccurrence.Required},
            {2, BinaryFormat.Byte, BinaryOccurrence.Optional},
            {3, BinaryFormat.Byte, BinaryOccurrence.Repeating},
            {4, BinaryFormat.Byte, BinaryOccurrence.Optional, 123, (v) => v + 1000}
        }
    )
in
    f(b)
```

```text
{11, null, {}, 123}
```

An unexpected key is read with the format returned by `extra` and discarded, so parsing resumes at the next key.

```m
let
    b = #binary({1, 11, 9, 99, 2, 22}),
    f = BinaryFormat.Group(
        BinaryFormat.Byte,
        {
            {1, BinaryFormat.Byte, BinaryOccurrence.Optional},
            {2, BinaryFormat.Byte, BinaryOccurrence.Optional}
        },
        (key) => if key < 10 then BinaryFormat.Byte else BinaryFormat.UnsignedInteger16
    )
in
    f(b)
```

```text
{11, 22}
```

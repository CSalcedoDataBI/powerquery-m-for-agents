<!-- lab: desktop 2.157.879.0 -->

# Binary.ViewFunction

The examples show a view function running its wrapped function and a Binary.View intercepting or falling back to it.

```m
let
    Size = Binary.ViewFunction((binary as nullable binary) => if binary = null then 0 else Binary.Length(binary))
in
    {Size(null), Size(Text.ToBinary("abcdef"))}
```

```text
{0, 6}
```

When the view supplies an OnInvoke handler, that handler's result is used instead of running the wrapped function.

```m
let
    Size = Binary.ViewFunction((binary as nullable binary) => if binary = null then 0 else Binary.Length(binary)),
    Viewed = Binary.View(
        null,
        [
            GetStream = () => Text.ToBinary("abcdef"),
            OnInvoke = (func, args, index) => 99
        ]
    )
in
    Size(Viewed)
```

```text
99
```

An error raised by OnInvoke is swallowed, and the wrapped function is applied to the view instead.

```m
let
    Size = Binary.ViewFunction((binary as nullable binary) => if binary = null then 0 else Binary.Length(binary)),
    Viewed = Binary.View(
        null,
        [
            GetStream = () => Text.ToBinary("abcdef"),
            GetLength = () => 6,
            OnInvoke = (func, args, index) => error "not handled"
        ]
    )
in
    Size(Viewed)
```

```text
6
```

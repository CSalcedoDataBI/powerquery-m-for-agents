<!-- lab: desktop 2.159.883.0 -->

# Number.RoundUp

Rounds toward positive infinity, so negative numbers move toward zero and whole numbers stay as they are.

```m
{Number.RoundUp(1.2), Number.RoundUp(-1.2), Number.RoundUp(-1.8), Number.RoundUp(5), Number.RoundUp(null)}
```

```text
{2, -1, -1, 5, null}
```

`digits` sets the number of decimal places. A negative value rounds to tens, hundreds and so on.

```m
{Number.RoundUp(1.231, 2), Number.RoundUp(-1.239, 2), Number.RoundUp(1201, -2), Number.RoundUp(-1299, -2)}
```

```text
{1.24, -1.23, 1300, -1200}
```

A `null` for `digits` behaves like leaving it out.

```m
{Number.RoundUp(2.01, null), Number.RoundUp(2.01, 0), Number.RoundUp(2.01)}
```

```text
{3, 3, 3}
```

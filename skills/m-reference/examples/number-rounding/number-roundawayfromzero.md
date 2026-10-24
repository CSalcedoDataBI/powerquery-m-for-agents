<!-- lab: desktop 2.159.883.0 -->

# Number.RoundAwayFromZero

Any fraction pushes the value away from zero, so negatives get more negative; `digits` sets the decimal place, and nulls pass through.

```m
{Number.RoundAwayFromZero(1.2), Number.RoundAwayFromZero(-1.2), Number.RoundAwayFromZero(2.5), Number.RoundAwayFromZero(-2.5), Number.RoundAwayFromZero(3)}
```

```text
{2, -2, 3, -3, 3}
```

```m
{Number.RoundAwayFromZero(1.2341, 2), Number.RoundAwayFromZero(-1.2341, 2), Number.RoundAwayFromZero(1201, -2), Number.RoundAwayFromZero(-1201, -2)}
```

```text
{1.24, -1.24, 1300, -1300}
```

```m
{Number.RoundAwayFromZero(null), Number.RoundAwayFromZero(null, 2), Number.RoundAwayFromZero(1.2, null)}
```

```text
{null, null, 2}
```

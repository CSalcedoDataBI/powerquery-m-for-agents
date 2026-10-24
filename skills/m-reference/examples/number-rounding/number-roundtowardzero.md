<!-- lab: desktop 2.159.883.0 -->

# Number.RoundTowardZero

Negative numbers round up toward zero, `digits` can be negative or null, and a null number returns null.

```m
{Number.RoundTowardZero(1.7), Number.RoundTowardZero(-1.7), Number.RoundTowardZero(-0.5), Number.RoundTowardZero(-2)}
```

```text
{1, -1, 0, -2}
```

With `digits`, the cut happens at that decimal place. Negative `digits` cut to the left of the point. A null `digits` acts as if it were omitted.

```m
{Number.RoundTowardZero(-1.239, 2), Number.RoundTowardZero(1.239, 2), Number.RoundTowardZero(-1789.5, -2), Number.RoundTowardZero(1.239, null)}
```

```text
{-1.23, 1.23, -1700, 1}
```

A null number gives null rather than an error.

```m
Number.RoundTowardZero(null, 2)
```

```text
null
```

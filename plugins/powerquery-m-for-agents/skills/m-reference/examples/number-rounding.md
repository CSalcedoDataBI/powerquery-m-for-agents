<!-- lab: desktop 2.159.883.0 -->

# Executed examples: number-rounding

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Number.Round

By default halves round to the nearest even number, and the optional arguments change the precision and the rounding mode.

```m
{Number.Round(2.5), Number.Round(3.5), Number.Round(-2.5), Number.Round(0.5)}
```

```text
{2.0, 4.0, -2.0, 0.0}
```

Negative digits round to tens or hundreds. A null number returns null, and null digits act like the default.

```m
{Number.Round(1.2345, 2), Number.Round(1250, -2), Number.Round(1350, -2), Number.Round(null), Number.Round(2.5, null)}
```

```text
{1.23, 1200, 1400, null, 2.0}
```

The mode only changes how an exact half rounds. Up and Down round toward positive or negative infinity, not away from or toward zero.

```m
{Number.Round(2.5, 0, RoundingMode.AwayFromZero), Number.Round(-2.5, 0, RoundingMode.Up), Number.Round(-2.5, 0, RoundingMode.Down), Number.Round(-2.5, 0, RoundingMode.TowardZero), Number.Round(2.6, 0, RoundingMode.Down)}
```

```text
{3.0, -2.0, -3.0, -2, 3}
```

## Number.RoundAwayFromZero

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

## Number.RoundDown

These examples show how negative numbers, the optional digits argument and nulls behave.

Negative numbers round toward negative infinity, not toward zero.

```m
{Number.RoundDown(1.7), Number.RoundDown(-1.2), Number.RoundDown(-1.7)}
```

```text
{1, -2, -2}
```

The digits argument sets decimal places. A negative value applies to the left of the decimal point.

```m
{Number.RoundDown(1.2345, 2), Number.RoundDown(-1.2345, 2), Number.RoundDown(1234.5, -2), Number.RoundDown(1.2345, 0)}
```

```text
{1.23, -1.24, 1200, 1}
```

A null number and a null digits argument behave differently.

```m
{Number.RoundDown(null), Number.RoundDown(null, 2), Number.RoundDown(1.789, null)}
```

```text
{null, null, 1}
```

## Number.RoundTowardZero

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

## Number.RoundUp

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

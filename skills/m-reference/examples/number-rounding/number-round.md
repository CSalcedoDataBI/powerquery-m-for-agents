<!-- lab: desktop 2.159.883.0 -->

# Number.Round

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

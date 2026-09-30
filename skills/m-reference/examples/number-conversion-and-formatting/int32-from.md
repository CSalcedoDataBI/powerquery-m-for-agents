<!-- lab: desktop 2.157.879.0 -->

# Int32.From

The examples show that `null` passes straight through, that fractional numbers are rounded to even by default, and that an explicit rounding mode overrides it.

```m
Int32.From(null)
```

```text
null
```

```m
Int32.From(2.5)
```

```text
2
```

```m
Int32.From("4.5", null, RoundingMode.AwayFromZero)
```

```text
5
```

The rounding mode only breaks ties: 7.9 still becomes 8 with `RoundingMode.Down`.

```m
{Int32.From(7.9, null, RoundingMode.Down), Int32.From(-7.9, null, RoundingMode.TowardZero)}
```

```text
{8, -8}
```

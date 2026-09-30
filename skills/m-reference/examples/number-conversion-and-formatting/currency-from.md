<!-- lab: desktop 2.157.879.0 -->

# Currency.From

These examples show null handling, default rounding, and an explicit rounding mode.

```m
Currency.From(null)
```

```text
null
```

```m
Currency.From("1.23445")
```

```text
1.23440
```

```m
Currency.From("1.23445", "en-US", RoundingMode.Up)
```

```text
1.23450
```

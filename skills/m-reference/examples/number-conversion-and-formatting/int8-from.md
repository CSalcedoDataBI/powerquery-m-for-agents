<!-- lab: desktop 2.157.879.0 -->

# Int8.From

These examples show null input, the default banker's rounding, and an explicit rounding mode with a culture.

```m
Int8.From(null)
```

```text
null
```

```m
Int8.From("4.5")
```

```text
4
```

```m
Int8.From("1,5", "de-DE", RoundingMode.AwayFromZero)
```

```text
2
```

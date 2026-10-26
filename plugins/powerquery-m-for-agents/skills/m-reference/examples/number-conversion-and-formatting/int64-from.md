<!-- lab: desktop 2.157.879.0 -->

# Int64.From

These examples show how `Int64.From` handles nulls, default banker's rounding, and culture-aware text conversion with an explicit rounding mode.

```m
Int64.From(null)
```

```text
null
```

```m
Int64.From(2.5)
```

```text
2
```

```m
Int64.From("4,5", "fr-FR", RoundingMode.AwayFromZero)
```

```text
5
```

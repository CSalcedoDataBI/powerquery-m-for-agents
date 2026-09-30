<!-- lab: desktop 2.157.879.0 -->

# Decimal.From

Null passes through, an explicit culture changes how text is parsed, and a value that is already a number is returned as-is.

```m
Decimal.From(null)
```

```text
null
```

```m
Decimal.From("1.234,5", "de-DE")
```

```text
1234.5
```

```m
Decimal.From(123)
```

```text
123
```

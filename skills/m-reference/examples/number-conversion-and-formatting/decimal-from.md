<!-- lab: desktop 2.157.879.0 -->

# Decimal.From

Text, logical and null.

```m
{Decimal.From("4.5"), Decimal.From(true), Decimal.From(null)}
```

```text
{4.5, 1, null}
```

The culture decides the decimal separator.

```m
{Decimal.From("4,5", "es-ES"), Decimal.From("4,5", "en-US")}
```

```text
{4.5, 45}
```

<!-- lab: desktop 2.157.879.0 -->

# Currency.From

Currency keeps four decimals; the rest is rounded.

```m
{Currency.From(1.23456), Currency.From(1.23455), Currency.From(1.23455, null, RoundingMode.AwayFromZero)}
```

```text
{1.2346, 1.23460, 1.23460}
```

Text is read with the culture.

```m
{Currency.From("1.234,5", "es-ES"), Currency.From("1,234.5", "en-US")}
```

```text
{1234.5, 1234.5}
```

<!-- lab: desktop 2.157.879.0 -->

# Percentage.From

Text with a percent sign, and a plain number.

```m
{Percentage.From("12.5%"), Percentage.From(0.125), Percentage.From("12.5")}
```

```text
{0.125, 0.125, 12.5}
```

The value's type after the call.

```m
Value.Type(Percentage.From(0.5))
```

```text
type number
```

<!-- lab: desktop 2.157.879.0 -->

# Int16.From

Nulls pass through, fractional values round to even by default, and values outside the 16-bit range are rejected.

```m
Int16.From(null)
```

```text
null
```

```m
{Int16.From(2.5), Int16.From(3.5), Int16.From(2.5, null, RoundingMode.AwayFromZero)}
```

```text
{2, 4, 3}
```

```m
Int16.From(32768)
```

```text
error: Expression.Error: The number is out of range of a 16 bit integer value. | Detail: 32768
```

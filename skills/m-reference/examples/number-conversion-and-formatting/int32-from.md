<!-- lab: desktop 2.157.879.0 -->

# Int32.From

The rounding mode only breaks ties: 7.9 still becomes 8 with `RoundingMode.Down`.

```m
{Int32.From("7.5"), Int32.From(7.9, null, RoundingMode.Down), Int32.From(-7.9, null, RoundingMode.TowardZero)}
```

```text
{8, 8, -8}
```

Just past the 32-bit range.

```m
try Int32.From(2147483648)
```

```text
[HasError = true, Error = [Reason = "Expression.Error", Message = "The number is out of range of a 32 bit integer value.", Detail = 2147483648, #"Message.Format" = "The number is out of range of a 32 bit integer value.", #"Message.Parameters" = null, ErrorCode = "10108"]]
```

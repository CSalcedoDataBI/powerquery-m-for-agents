<!-- lab: desktop 2.157.879.0 -->

# Int16.From

Rounding of halves, default and away from zero.

```m
{Int16.From(2.5), Int16.From(-2.5), Int16.From(2.5, null, RoundingMode.AwayFromZero)}
```

```text
{2, -2, 3}
```

Just past the 16-bit range.

```m
{Int16.From(32767), try Int16.From(32768)}
```

```text
{32767, [HasError = true, Error = [Reason = "Expression.Error", Message = "The number is out of range of a 16 bit integer value.", Detail = 32768, #"Message.Format" = "The number is out of range of a 16 bit integer value.", #"Message.Parameters" = null, ErrorCode = "10482"]]}
```

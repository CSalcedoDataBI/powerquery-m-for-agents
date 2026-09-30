<!-- lab: desktop 2.157.879.0 -->

# Byte.From

A fraction is rounded; the default mode is to even.

```m
{Byte.From(2.5), Byte.From(3.5), Byte.From(2.5, null, RoundingMode.AwayFromZero)}
```

```text
{2, 4, 3}
```

Out of range for a byte (0 to 255).

```m
{try Byte.From(256), try Byte.From(-1)}
```

```text
{[HasError = true, Error = [Reason = "Expression.Error", Message = "The number is out of range of a byte value.", Detail = 256, #"Message.Format" = "The number is out of range of a byte value.", #"Message.Parameters" = null, ErrorCode = "10106"]], [HasError = true, Error = [Reason = "Expression.Error", Message = "The number is out of range of a byte value.", Detail = -1, #"Message.Format" = "The number is out of range of a byte value.", #"Message.Parameters" = null, ErrorCode = "10106"]]}
```

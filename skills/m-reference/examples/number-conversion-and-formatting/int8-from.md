<!-- lab: desktop 2.157.879.0 -->

# Int8.From

Int8 is signed: -128 to 127.

```m
{Int8.From(-128), try Int8.From(128)}
```

```text
{-128, [HasError = true, Error = [Reason = "Expression.Error", Message = "The number is out of range of an 8 bit integer value.", Detail = 128, #"Message.Format" = "The number is out of range of an 8 bit integer value.", #"Message.Parameters" = null, ErrorCode = "10483"]]}
```

A tie goes to even by default; the mode decides it otherwise.

```m
{Int8.From(-1.5), Int8.From(-1.5, null, RoundingMode.TowardZero)}
```

```text
{-2, -1}
```

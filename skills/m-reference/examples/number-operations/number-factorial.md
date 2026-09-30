<!-- lab: desktop 2.157.879.0 -->

# Number.Factorial

Small values, and zero.

```m
{Number.Factorial(0), Number.Factorial(5), Number.Factorial(null)}
```

```text
{1, 120, null}
```

Negative and fractional input are errors.

```m
{try Number.Factorial(-1), try Number.Factorial(2.5)}
```

```text
{[HasError = true, Error = [Reason = "Expression.Error", Message = "This function operates only on Unsigned values, but value -1 doesn't match the Unsigned pattern.", Detail = -1, #"Message.Format" = "This function operates only on Unsigned values, but value #{0} doesn't match the Unsigned pattern.", #"Message.Parameters" = {"-1"}, ErrorCode = "10015"]], [HasError = true, Error = [Reason = "Expression.Error", Message = "The number is out of range of a 64 bit integer value.", Detail = 2.5, #"Message.Format" = "The number is out of range of a 64 bit integer value.", #"Message.Parameters" = null, ErrorCode = "10109"]]}
```

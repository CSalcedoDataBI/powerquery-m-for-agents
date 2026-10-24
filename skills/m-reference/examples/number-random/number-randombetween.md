<!-- lab: desktop 2.159.883.0 -->

# Number.RandomBetween

The result is a random fraction, not a whole number, so these blocks check its properties rather than its value.

```m
let r = Number.RandomBetween(1, 10) in [InRange = r >= 1 and r <= 10, IsWhole = r = Number.RoundDown(r)]
```

```text
[InRange = true, IsWhole = false]
```

Swapped bounds: the bottom is larger than the top.

```m
let r = Number.RandomBetween(10, 1) in [InRange = r >= 1 and r <= 10, Error = try r otherwise "error"]
```

```text
[InRange = error: Expression.Error: The 'top' argument cannot be less than 'bottom'. | Detail: 1, Error = "error"]
```

A null bound.

```m
try Number.RandomBetween(null, 10)
```

```text
[HasError = true, Error = [Reason = "Expression.Error", Message = "We cannot convert the value null to type Number.", Detail = [Value = null, Type = type number], #"Message.Format" = "We cannot convert the value #{0} to type #{1}.", #"Message.Parameters" = {"null", "Number"}, ErrorCode = "10277"]]
```

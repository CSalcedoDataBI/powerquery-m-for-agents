<!-- lab: desktop 2.159.883.0 -->

# Executed examples: number-random

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Number.Random

These examples show that the result is a number from 0 up to but not including 1, and that the function takes no arguments.

```m
let r = Number.Random() in [IsNumber = Value.Is(r, Number.Type), InRange = r >= 0 and r < 1]
```

```text
[IsNumber = true, InRange = true]
```

To get a number in another range, scale the result yourself. Number.Random accepts no bounds.

```m
let r = Number.Random() * 10 + 5 in r >= 5 and r < 15
```

```text
true
```

Passing an argument, such as a seed, raises an error.

```m
try Number.Random(42)
```

```text
[HasError = true, Error = [Reason = "Expression.Error", Message = "1 arguments were passed to a function which expects 0.", Detail = [Pattern = null, Arguments = {42}], #"Message.Format" = "#{0} arguments were passed to a function which expects #{1}.", #"Message.Parameters" = {1, 0}, ErrorCode = "10065"]]
```

## Number.RandomBetween

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

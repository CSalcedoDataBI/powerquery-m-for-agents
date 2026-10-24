<!-- lab: desktop 2.159.883.0 -->

# Number.Random

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

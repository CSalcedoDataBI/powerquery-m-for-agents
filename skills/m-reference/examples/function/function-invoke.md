<!-- lab: desktop 2.159.883.0 -->

# Function.Invoke

The list is spread into separate arguments, and optional parameters can be omitted or passed as null.

```m
Function.Invoke(List.Sum, {{1, 2, 3}})
```

```text
6
```

Without the outer list, each number becomes its own argument, so List.Sum gets too many arguments.

```m
Function.Invoke(List.Sum, {1, 2, 3})
```

```text
error: Expression.Error: 3 arguments were passed to a function which expects between 1 and 2. | Detail: [Pattern = null, Arguments = {1, 2, 3}]
```

Omitting an optional argument and passing null for one both use the default.

```m
{Function.Invoke(Text.PadStart, {"7", 3}), Function.Invoke(Text.PadStart, {"7", 3, null}), Function.Invoke(Text.PadStart, {"7", 3, "0"})}
```

```text
{"  7", "  7", "007"}
```

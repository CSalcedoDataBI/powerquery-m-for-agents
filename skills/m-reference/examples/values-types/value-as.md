<!-- lab: desktop 2.159.883.0 -->

# Value.As

Value.As only checks the type and never converts, so a mismatch is an error.

```m
try Value.As("1", type number)
```

```text
[HasError = true, Error = [Reason = "Expression.Error", Message = "We cannot convert the value ""1"" to type Number.", Detail = [Value = "1", Type = type number], #"Message.Format" = "We cannot convert the value #{0} to type #{1}.", #"Message.Parameters" = {"""1""", "Number"}, ErrorCode = "10277"]]
```

Null fails a plain `number` check but passes `nullable number`.

```m
[Plain = try Value.As(null, type number), Nullable = try Value.As(null, type nullable number)]
```

```text
[Plain = [HasError = true, Error = [Reason = "Expression.Error", Message = "We cannot convert the value null to type Number.", Detail = [Value = null, Type = type number], #"Message.Format" = "We cannot convert the value #{0} to type #{1}.", #"Message.Parameters" = {"null", "Number"}, ErrorCode = "10277"]], Nullable = [HasError = false, Value = null]]
```

Only the outer kind is checked. A list of text passes a list-of-number type.

```m
Value.As({"a", "b"}, type {number})
```

```text
{"a", "b"}
```

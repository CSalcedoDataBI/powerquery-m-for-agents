<!-- lab: desktop 2.157.879.0 -->

# Duration.ToRecord

These examples show how a duration splits into day, hour, minute and second parts, including carry-over, fractional seconds, and null, which is an error.

```m
Duration.ToRecord(#duration(0, 25, 0, 0))
```

```text
[Days = 1, Hours = 1, Minutes = 0, Seconds = 0]
```

```m
Duration.ToRecord(#duration(0, 0, 0, 1.5))
```

```text
[Days = 0, Hours = 0, Minutes = 0, Seconds = 1.5]
```

```m
Duration.ToRecord(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Duration. | Detail: [Value = null, Type = type duration]
```

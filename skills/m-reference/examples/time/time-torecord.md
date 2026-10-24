<!-- lab: desktop 2.159.883.0 -->

# Time.ToRecord

The examples show fractional seconds, the 24:00 edge case, and a null input.

```m
Time.ToRecord(#time(14, 5, 30.25))
```

```text
[Hour = 14, Minute = 5, Second = 30.25]
```

```m
Time.ToRecord(#time(24, 0, 0))
```

```text
[Hour = 0, Minute = 0, Second = 0]
```

```m
Time.ToRecord(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Time. | Detail: [Value = null, Type = type time]
```

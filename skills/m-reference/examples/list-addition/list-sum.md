<!-- lab: desktop 2.157.879.0 -->

# List.Sum

Nulls ignored, empty gives null, and decimal precision.

```m
{List.Sum({1, null, 2}), List.Sum({}), List.Sum({0.1, 0.2}), List.Sum({0.1, 0.2}, Precision.Decimal)}
```

```text
{3, null, 0.30000000000000004, 0.3}
```

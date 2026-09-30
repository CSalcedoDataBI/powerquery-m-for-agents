<!-- lab: desktop 2.157.879.0 -->

# List.Distinct

Plain and case-insensitive.

```m
{List.Distinct({1, 1, 2}), List.Distinct({"a", "A", "b"}, Comparer.OrdinalIgnoreCase)}
```

```text
{{1, 2}, {"a", "b"}}
```

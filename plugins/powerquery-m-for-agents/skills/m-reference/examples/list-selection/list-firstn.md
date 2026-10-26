<!-- lab: desktop 2.157.879.0 -->

# List.FirstN

A count, or a condition that stops at the first item failing it.

```m
{List.FirstN({1, 2, 3, 4}, 2), List.FirstN({1, 2, 5, 1}, each _ < 3)}
```

```text
{{1, 2}, {1, 2}}
```

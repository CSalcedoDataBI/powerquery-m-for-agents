<!-- lab: desktop 2.157.879.0 -->

# Duration.TotalHours

These examples show null handling and totals built from whole days or minutes rather than the hours component alone.

```m
Duration.TotalHours(null)
```

```text
null
```

```m
Duration.TotalHours(#duration(2, 3, 0, 0))
```

```text
51
```

```m
Duration.TotalHours(#duration(0, 0, 90, 0))
```

```text
1.5
```

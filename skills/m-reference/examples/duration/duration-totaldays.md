<!-- lab: desktop 2.157.879.0 -->

# Duration.TotalDays

These examples show that a null propagates, that part of a day counts as a fraction, and that a negative duration yields a negative total.

```m
Duration.TotalDays(null)
```

```text
null
```

```m
Duration.TotalDays(#duration(0, 23, 59, 59))
```

```text
0.99998842592592585
```

```m
Duration.TotalDays(#duration(-2, -12, 0, 0))
```

```text
-2.5
```

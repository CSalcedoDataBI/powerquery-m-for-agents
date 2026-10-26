<!-- lab: desktop 2.157.879.0 -->

# Duration.Hours

These examples show the hour component of a duration, including null input and an hour value that carries into days.

A null duration stays null.

```m
Duration.Hours(null)
```

```text
null
```

Only the hours field is returned, not the hours contained in the days.

```m
Duration.Hours(#duration(5, 4, 3, 2))
```

```text
4
```

Hours beyond a full day are carried into the days, so the hours field wraps.

```m
Duration.Hours(#duration(0, 25, 0, 0))
```

```text
1
```

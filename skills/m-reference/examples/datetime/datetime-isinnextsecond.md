<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInNextSecond

Only the one-second window after the current instant counts, while null and far-off values fall outside it.

A null input yields null rather than false.

```m
DateTime.IsInNextSecond(null)
```

```text
null
```

A datetime far in the past is never in the next second, regardless of the current system time.

```m
DateTime.IsInNextSecond(#datetime(1990, 12, 31, 23, 59, 59))
```

```text
false
```

A datetimezone in the far future is likewise false, since neither the date nor its offset can pull it into the next second.

```m
DateTime.IsInNextSecond(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

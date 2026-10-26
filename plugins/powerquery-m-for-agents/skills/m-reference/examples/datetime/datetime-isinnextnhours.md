<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInNextNHours

A null value gives a null result.

```m
DateTime.IsInNextNHours(null, 3)
```

```text
null
```

A datetime far in the past is never in the next few hours.

```m
DateTime.IsInNextNHours(#datetime(1990, 1, 1, 0, 0, 0), 3)
```

```text
false
```

A far-future datetime qualifies only when the hour window reaches it.

```m
DateTime.IsInNextNHours(#datetime(2200, 1, 1, 0, 0, 0), 2000000)
```

```text
true
```

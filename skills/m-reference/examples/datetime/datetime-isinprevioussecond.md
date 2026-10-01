<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInPreviousSecond

These examples show a value far from the current second, a null argument, and a `datetimezone` value.

```m
DateTime.IsInPreviousSecond(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInPreviousSecond(null)
```

```text
null
```

```m
DateTime.IsInPreviousSecond(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

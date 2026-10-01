<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInPreviousNMinutes

The window is anchored to the current clock, so timestamps far in the past or future fall outside it even for a large `minutes` value.

```m
DateTime.IsInPreviousNMinutes(#datetime(1990, 1, 1, 0, 0, 0), 5)
```

```text
false
```

A `datetimezone` value is accepted in place of a `datetime`.

```m
DateTime.IsInPreviousNMinutes(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0), 5)
```

```text
false
```

A null `dateTime` returns null rather than false.

```m
DateTime.IsInPreviousNMinutes(null, 5)
```

```text
null
```

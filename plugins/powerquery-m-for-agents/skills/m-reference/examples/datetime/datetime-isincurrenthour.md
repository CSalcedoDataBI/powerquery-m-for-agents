<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInCurrentHour

Distant instants are never in the current hour, a time-zone value behaves the same way, and null stays null.

```m
DateTime.IsInCurrentHour(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

A `datetimezone` value from the far future is likewise outside the current hour.

```m
DateTime.IsInCurrentHour(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

A null input is not treated as false.

```m
DateTime.IsInCurrentHour(null)
```

```text
null
```

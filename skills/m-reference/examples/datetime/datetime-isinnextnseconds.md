<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInNextNSeconds

Null propagates, a fixed far-past value stays outside the window, and a far-future value can fall inside a very long window.

```m
DateTime.IsInNextNSeconds(null, 10)
```

```text
null
```

```m
DateTime.IsInNextNSeconds(#datetime(1990, 1, 1, 0, 0, 0), 60)
```

```text
false
```

```m
DateTime.IsInNextNSeconds(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0), 10000000000)
```

```text
true
```

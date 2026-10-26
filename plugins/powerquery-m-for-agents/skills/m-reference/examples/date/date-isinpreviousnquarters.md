<!-- lab: desktop 2.157.879.0 -->

# Date.IsInPreviousNQuarters

The examples show null input, a far-past datetime, and a zero-quarter count.

```m
Date.IsInPreviousNQuarters(null, 4)
```

```text
null
```

```m
Date.IsInPreviousNQuarters(#datetime(1990, 1, 1, 0, 0, 0), 4)
```

```text
false
```

```m
Date.IsInPreviousNQuarters(#date(2200, 1, 1), 0)
```

```text
false
```

<!-- lab: desktop 2.157.879.0 -->

# Date.IsInNextNQuarters

The examples show null handling, a past date, and a count large enough to reach a far-future date.

```m
Date.IsInNextNQuarters(null, 1)
```

```text
null
```

```m
Date.IsInNextNQuarters(#date(1990, 1, 1), 1000)
```

```text
false
```

```m
Date.IsInNextNQuarters(#date(2200, 6, 15), 1000)
```

```text
true
```

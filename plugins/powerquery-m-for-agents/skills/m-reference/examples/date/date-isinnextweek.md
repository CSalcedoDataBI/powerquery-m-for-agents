<!-- lab: desktop 2.157.879.0 -->

# Date.IsInNextWeek

Distant dates fall outside the next week, and null input is passed through.

```m
Date.IsInNextWeek(#date(1990, 1, 1))
```

```text
false
```

A far-future datetime is outside the next week as well.

```m
Date.IsInNextWeek(#datetime(2200, 1, 1, 12, 0, 0))
```

```text
false
```

A null date shows how a missing value is handled.

```m
Date.IsInNextWeek(null)
```

```text
null
```

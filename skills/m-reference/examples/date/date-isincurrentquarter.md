<!-- lab: desktop 2.157.879.0 -->

# Date.IsInCurrentQuarter

Fixed dates far from the current quarter show which values qualify and how null is handled.

A date from 1990 never belongs to the current quarter.

```m
Date.IsInCurrentQuarter(#date(1990, 3, 15))
```

```text
false
```

A future value is not in the current quarter even when its quarter number lines up, because the year is not current.

```m
Date.IsInCurrentQuarter(#datetimezone(2200, 3, 15, 0, 0, 0, 0, 0))
```

```text
false
```

Null flows through instead of being treated as a date.

```m
Date.IsInCurrentQuarter(null)
```

```text
null
```

<!-- lab: desktop 2.157.879.0 -->

# Date.IsInPreviousQuarter

The previous quarter is measured from the current system date, so fixed literal dates are never in it.

```m
Date.IsInPreviousQuarter(#date(1990, 3, 14))
```

```text
false
```

A future `datetimezone` is accepted but is not the previous quarter.

```m
Date.IsInPreviousQuarter(#datetimezone(2200, 9, 1, 0, 0, 0, 0, 0))
```

```text
false
```

A `null` value gives `null`, not `false`.

```m
Date.IsInPreviousQuarter(null)
```

```text
null
```

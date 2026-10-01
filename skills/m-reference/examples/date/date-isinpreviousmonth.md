<!-- lab: desktop 2.157.879.0 -->

# Date.IsInPreviousMonth

These examples show null handling and how dates fixed far from the system's clock behave.

A null input produces a null result rather than an error.

```m
Date.IsInPreviousMonth(null)
```

```text
null
```

A fixed 1990 date can never be the month before the current system month, whatever day the block runs.

```m
Date.IsInPreviousMonth(#date(1990, 1, 15))
```

```text
false
```

A `datetimezone` far in the future is likewise outside the previous month.

```m
Date.IsInPreviousMonth(#datetimezone(2200, 6, 1, 0, 0, 0, 0, 0))
```

```text
false
```

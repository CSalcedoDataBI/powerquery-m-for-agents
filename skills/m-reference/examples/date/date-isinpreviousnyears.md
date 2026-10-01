<!-- lab: desktop 2.157.879.0 -->

# Date.IsInPreviousNYears

Nulls stay null, and the window looks only backward, so future dates never qualify.

```m
Date.IsInPreviousNYears(null, 2)
```

```text
null
```

A far-future date is never part of the previous years, however wide the count.

```m
Date.IsInPreviousNYears(#date(2200, 12, 31), 1000)
```

```text
false
```

A far-past date falls inside a large enough count.

```m
Date.IsInPreviousNYears(#date(1990, 1, 1), 1000)
```

```text
true
```

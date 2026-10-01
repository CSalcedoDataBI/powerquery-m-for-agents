<!-- lab: desktop 2.157.879.0 -->

# Date.IsInNextQuarter

Far-off dates and nulls show what "next quarter" does and does not include.

A null input yields null rather than false.

```m
Date.IsInNextQuarter(null)
```

```text
null
```

A date decades in the past is not in the next quarter.

```m
Date.IsInNextQuarter(#date(1990, 3, 15))
```

```text
false
```

A date far in the future is still not the *next* quarter, because "next" means the quarter immediately after the current one.

```m
Date.IsInNextQuarter(#datetime(2200, 6, 1, 0, 0, 0))
```

```text
false
```

<!-- lab: desktop 2.157.879.0 -->

# Date.IsInNextNMonths

The examples cover null input, zero months, and fixed dates far from the current month.

A null date is accepted as input.

```m
Date.IsInNextNMonths(null, 1)
```

```text
null
```

A zero-month window does not match any month, even one far in the past.

```m
Date.IsInNextNMonths(#date(1990, 1, 1), 0)
```

```text
false
```

A fixed date far in the future stays outside the next month.

```m
Date.IsInNextNMonths(#date(2200, 1, 1), 1)
```

```text
false
```

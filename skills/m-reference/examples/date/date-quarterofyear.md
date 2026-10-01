<!-- lab: desktop 2.157.879.0 -->

# Date.QuarterOfYear

These examples show which quarter a date falls into at the March/April boundary, plus how null and datetime inputs behave.

Null input returns null.

```m
Date.QuarterOfYear(null)
```

```text
null
```

The last day of March is still quarter 1, while the first day of April is quarter 2.

```m
Date.QuarterOfYear(#date(2011, 3, 31))
```

```text
1
```

```m
Date.QuarterOfYear(#date(2011, 4, 1))
```

```text
2
```

A datetime value is judged by its date part, so the end of December is quarter 4.

```m
Date.QuarterOfYear(#datetime(1990, 12, 31, 23, 59, 59))
```

```text
4
```

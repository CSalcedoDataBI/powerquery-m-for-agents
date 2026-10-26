<!-- lab: desktop 2.157.879.0 -->

# Date.IsInNextYear

Fixed dates from opposite ends of the calendar show that the function compares against the current year, and null shows its null handling.

```m
Date.IsInNextYear(#date(1990, 12, 31))
```

```text
false
```

```m
Date.IsInNextYear(#date(2200, 1, 1))
```

```text
false
```

```m
Date.IsInNextYear(null)
```

```text
null
```

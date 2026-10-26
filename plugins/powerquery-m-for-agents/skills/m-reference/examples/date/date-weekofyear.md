<!-- lab: desktop 2.157.879.0 -->

# Date.WeekOfYear

Null input returns null, and the start-of-week argument is accepted; for 1 January 2006 both starts give week 1.

```m
Date.WeekOfYear(null)
```

```text
null
```

```m
Date.WeekOfYear(#date(2006, 1, 1), Day.Sunday)
```

```text
1
```

```m
Date.WeekOfYear(#date(2006, 1, 1), Day.Monday)
```

```text
1
```

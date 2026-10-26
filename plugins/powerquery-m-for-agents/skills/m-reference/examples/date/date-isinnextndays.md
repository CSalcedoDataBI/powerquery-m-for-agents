<!-- lab: desktop 2.157.879.0 -->

# Date.IsInNextNDays

Null input returns null, past dates fall outside the window, and a large day count can still reach a far-future date.

```m
Date.IsInNextNDays(null, 2)
```

```text
null
```

```m
Date.IsInNextNDays(#date(1990, 1, 1), 2)
```

```text
false
```

```m
Date.IsInNextNDays(#date(2200, 1, 1), 100000)
```

```text
true
```

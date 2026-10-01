<!-- lab: desktop 2.157.879.0 -->

# Date.IsInNextNYears

The examples show null handling and how fixed dates far from today are judged against a wide year window.

```m
Date.IsInNextNYears(null, 2)
```

```text
null
```

A far-future date lies inside a wide enough window no matter when the block runs.

```m
Date.IsInNextNYears(#date(2200, 6, 1), 1000)
```

```text
true
```

A past date is never in a future window, however many years it spans.

```m
Date.IsInNextNYears(#date(1990, 6, 1), 1000)
```

```text
false
```

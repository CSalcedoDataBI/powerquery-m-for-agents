<!-- lab: desktop 2.157.879.0 -->

# Date.MonthName

Null dates return null, the culture argument is optional, and datetime values are accepted. Without the argument the result follows the query's culture: these results are for en-US, the culture the lab model sets.

```m
Date.MonthName(null)
```

```text
null
```

```m
Date.MonthName(#date(2200, 2, 1))
```

```text
"February"
```

```m
Date.MonthName(#datetime(1990, 12, 31, 23, 59, 59), "fr-FR")
```

```text
"décembre"
```

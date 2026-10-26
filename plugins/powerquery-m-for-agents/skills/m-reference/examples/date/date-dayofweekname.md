<!-- lab: desktop 2.157.879.0 -->

# Date.DayOfWeekName

These examples show null propagation, the optional culture argument, and dates far from today.

```m
Date.DayOfWeekName(null)
```

```text
null
```

With no culture, the name comes from the query's culture: en-US in the lab model.

```m
Date.DayOfWeekName(#date(2200, 1, 1))
```

```text
"Wednesday"
```

A supplied culture changes the language of the name.

```m
Date.DayOfWeekName(#date(1990, 1, 1), "fr-FR")
```

```text
"lundi"
```

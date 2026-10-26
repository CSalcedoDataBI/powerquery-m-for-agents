<!-- lab: desktop 2.157.879.0 -->

# Date.ToText

These examples show how `Date.ToText` handles a null date, custom format and culture options, and the legacy text form of the options argument.

```m
Date.ToText(null)
```

```text
null
```

```m
Date.ToText(#date(2200, 1, 5), [Format = "dddd, dd MMMM yyyy", Culture = "fr-FR"])
```

```text
"dimanche, 05 janvier 2200"
```

```m
Date.ToText(#date(1990, 3, 1), "yyyy-MM-dd")
```

```text
"1990-03-01"
```

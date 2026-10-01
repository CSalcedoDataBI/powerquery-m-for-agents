<!-- lab: desktop 2.157.879.0 -->

# Date.FromText

The examples show a null input, the legacy culture-as-text option, and a format record for a non-Gregorian calendar.

```m
Date.FromText(null)
```

```text
null
```

```m
Date.FromText("01/02/2010", "en-GB")
```

```text
#date(2010, 2, 1)
```

```m
Date.FromText("1400", [Format = "yyyy", Culture = "ar-SA"])
```

```text
#date(1979, 11, 20)
```

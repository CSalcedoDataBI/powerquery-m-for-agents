<!-- lab: desktop 2.157.879.0 -->

# Date.From

Nulls pass through, numeric serials use the 1899-12-30 base rather than Unix time, and the optional culture argument changes text parsing.

```m
Date.From(null)
```

```text
null
```

```m
Date.From(1.25)
```

```text
#date(1899, 12, 31)
```

```m
Date.From("20 Januar 2023", "de-DE")
```

```text
#date(2023, 1, 20)
```

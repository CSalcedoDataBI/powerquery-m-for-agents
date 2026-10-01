<!-- lab: desktop 2.157.879.0 -->

# DateTime.From

These examples show the null result, the optional culture argument, and the date chosen when converting a time.

```m
DateTime.From(null)
```

```text
null
```

```m
DateTime.From("12/31/1990 11:59:59 PM", "en-US")
```

```text
#datetime(1990, 12, 31, 23, 59, 59)
```

```m
DateTime.From(#time(6, 45, 12))
```

```text
#datetime(1899, 12, 30, 6, 45, 12)
```

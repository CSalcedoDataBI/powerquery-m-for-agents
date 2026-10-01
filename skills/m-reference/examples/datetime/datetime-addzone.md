<!-- lab: desktop 2.157.879.0 -->

# DateTime.AddZone

These examples show how a null datetime, the optional minutes argument, and a negative offset behave.

Attaching a zone to a null datetime returns null.

```m
DateTime.AddZone(null, 7, 30)
```

```text
null
```

When the optional minutes argument is omitted, it defaults to zero.

```m
DateTime.AddZone(#datetime(2010, 12, 31, 11, 56, 2), -5)
```

```text
#datetimezone(2010, 12, 31, 11, 56, 2, -5, 0)
```

The offset never shifts the clock digits, even at the end of a day.

```m
DateTime.AddZone(#datetime(2200, 6, 15, 23, 59, 59), -3, -30)
```

```text
#datetimezone(2200, 6, 15, 23, 59, 59, -3, -30)
```

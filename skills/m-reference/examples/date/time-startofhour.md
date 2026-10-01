<!-- lab: desktop 2.157.879.0 -->

# Time.StartOfHour

The reset keeps the input's type (and a datetimezone's offset) and passes null through.

```m
Time.StartOfHour(#time(8, 10, 32))
```

```text
#time(8, 0, 0)
```

```m
Time.StartOfHour(#datetimezone(2200, 6, 15, 14, 45, 30, 5, 30))
```

```text
#datetimezone(2200, 6, 15, 14, 0, 0, 5, 30)
```

```m
Time.StartOfHour(null)
```

```text
null
```

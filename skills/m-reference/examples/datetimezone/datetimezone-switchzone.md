<!-- lab: desktop 2.159.883.0 -->

# DateTimeZone.SwitchZone

The instant stays the same, so the clock time and even the date shift, and a null input returns null.

```m
DateTimeZone.SwitchZone(#datetimezone(2010, 12, 31, 23, 0, 0, 0, 0), 5, 30)
```

```text
#datetimezone(2011, 1, 1, 4, 30, 0, 5, 30)
```

For a negative offset with minutes, give the minutes the same sign as the hours.

```m
DateTimeZone.SwitchZone(#datetimezone(2010, 12, 31, 1, 0, 0, 7, 0), -3, -30)
```

```text
#datetimezone(2010, 12, 30, 14, 30, 0, -3, -30)
```

```m
DateTimeZone.SwitchZone(null, 3)
```

```text
null
```

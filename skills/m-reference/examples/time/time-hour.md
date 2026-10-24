<!-- lab: desktop 2.159.883.0 -->

# Time.Hour

The examples show which hour comes back for time zones, nulls and edge times.

On a datetimezone, the hour stays in the value's own offset and is not converted to UTC.

```m
Time.Hour(#datetimezone(1990, 6, 1, 23, 30, 0, -5, 0))
```

```text
23
```

A null input returns null, and the hour never rounds up from minutes or seconds.

```m
{Time.Hour(null), Time.Hour(#time(9, 59, 59.9)), Time.Hour(#datetime(1990, 1, 1, 0, 0, 0))}
```

```text
{null, 9, 0}
```

The time literal accepts 24:00:00.

```m
Time.Hour(#time(24, 0, 0))
```

```text
0
```

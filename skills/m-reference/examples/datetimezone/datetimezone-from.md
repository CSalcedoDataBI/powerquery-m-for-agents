<!-- lab: desktop 2.159.883.0 -->

# DateTimeZone.From

Null passes through as null, and text keeps the offset it is written with.

```m
[
    FromNull = DateTimeZone.From(null),
    FromText = DateTimeZone.From("2020-01-15T10:30:00+05:00"),
    FromValue = DateTimeZone.From(#datetimezone(2200, 1, 1, 0, 0, 0, -8, 0))
]
```

```text
[FromNull = null, FromText = #datetimezone(2020, 1, 15, 10, 30, 0, 5, 0), FromValue = #datetimezone(2200, 1, 1, 0, 0, 0, -8, 0)]
```

The optional culture decides whether "03/04" is read as March 4 or April 3.

```m
[
    US = DateTimeZone.From("03/04/2020 10:00 +01:00", "en-US"),
    GB = DateTimeZone.From("03/04/2020 10:00 +01:00", "en-GB")
]
```

```text
[US = #datetimezone(2020, 3, 4, 10, 0, 0, 1, 0), GB = #datetimezone(2020, 4, 3, 10, 0, 0, 1, 0)]
```

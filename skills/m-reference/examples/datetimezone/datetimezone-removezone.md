<!-- lab: desktop 2.159.883.0 -->

# DateTimeZone.RemoveZone

The offset is dropped without being applied, so the clock time stays as written.

```m
DateTimeZone.RemoveZone(#datetimezone(2024, 3, 10, 14, 30, 0, 5, 30))
```

```text
#datetime(2024, 3, 10, 14, 30, 0)
```

To get the UTC clock time, convert first and then remove the zone.

```m
[
    Dropped = DateTimeZone.RemoveZone(#datetimezone(2024, 3, 10, 14, 30, 0, 5, 30)),
    UtcFirst = DateTimeZone.RemoveZone(DateTimeZone.ToUtc(#datetimezone(2024, 3, 10, 14, 30, 0, 5, 30))),
    NegativeOffset = DateTimeZone.RemoveZone(DateTimeZone.ToUtc(#datetimezone(2024, 12, 31, 22, 0, 0, -5, 0)))
]
```

```text
[Dropped = #datetime(2024, 3, 10, 14, 30, 0), UtcFirst = #datetime(2024, 3, 10, 9, 0, 0), NegativeOffset = #datetime(2025, 1, 1, 3, 0, 0)]
```

A null input passes through as null.

```m
DateTimeZone.RemoveZone(null)
```

```text
null
```

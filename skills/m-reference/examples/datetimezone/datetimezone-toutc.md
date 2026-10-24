<!-- lab: desktop 2.159.883.0 -->

# DateTimeZone.ToUtc

The examples show that the clock time shifts by the offset, which can cross a date or year boundary, and that null passes through unchanged.

```m
DateTimeZone.ToUtc(#datetimezone(2010, 12, 31, 22, 30, 0, -5, -30))
```

```text
#datetimezone(2011, 1, 1, 4, 0, 0, 0, 0)
```

Different offsets for the same instant give the same UTC value.

```m
{
    DateTimeZone.ToUtc(#datetimezone(2024, 3, 1, 5, 30, 0, 5, 30)),
    DateTimeZone.ToUtc(#datetimezone(2024, 2, 29, 16, 0, 0, -8, 0)),
    DateTimeZone.ToUtc(#datetimezone(2024, 3, 1, 0, 0, 0, 0, 0))
}
```

```text
{#datetimezone(2024, 3, 1, 0, 0, 0, 0, 0), #datetimezone(2024, 3, 1, 0, 0, 0, 0, 0), #datetimezone(2024, 3, 1, 0, 0, 0, 0, 0)}
```

A null input returns null instead of raising an error.

```m
DateTimeZone.ToUtc(null)
```

```text
null
```

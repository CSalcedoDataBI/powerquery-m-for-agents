<!-- lab: desktop 2.159.883.0 -->

# DateTimeZone.FromText

A null input returns null, a trailing "Z" means a +00:00 offset, and the optional options argument can set a custom format and culture.

```m
{DateTimeZone.FromText(null), DateTimeZone.FromText("2010-12-31T01:30:00-08:00"), DateTimeZone.FromText("2010-12-31T01:30:00Z")}
```

```text
{null, #datetimezone(2010, 12, 31, 1, 30, 0, -8, 0), #datetimezone(2010, 12, 31, 1, 30, 0, 0, 0)}
```

With a custom format, month names are read in the given culture.

```m
DateTimeZone.FromText("30 Dez 2010 02:04:50.369730 +02:00", [Format = "dd MMM yyyy HH:mm:ss.ffffff zzz", Culture = "de-DE"])
```

```text
#datetimezone(2010, 12, 30, 2, 4, 50.36973, 2, 0)
```

A culture alone decides the day and month order of an ambiguous date.

```m
{DateTimeZone.FromText("03/04/2010 10:00:00 +01:00", [Culture = "en-GB"]), DateTimeZone.FromText("03/04/2010 10:00:00 +01:00", [Culture = "en-US"])}
```

```text
{#datetimezone(2010, 4, 3, 10, 0, 0, 1, 0), #datetimezone(2010, 3, 4, 10, 0, 0, 1, 0)}
```

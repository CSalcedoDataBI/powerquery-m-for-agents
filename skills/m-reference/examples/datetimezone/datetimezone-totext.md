<!-- lab: desktop 2.159.883.0 -->

# DateTimeZone.ToText

These examples show null input, the options record, and the older text-format argument with a negative offset.

```m
{DateTimeZone.ToText(null), DateTimeZone.ToText(#datetimezone(2010, 12, 31, 1, 30, 25, 2, 0))}
```

```text
{null, "12/31/2010 1:30:25 AM +02:00"}
```

An options record sets the format and culture together, and `zzz` writes the offset.

```m
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 1, 30, 25, 2, 0), [Format = "yyyy-MM-ddTHH:mm:sszzz", Culture = "en-US"])
```

```text
"2010-12-31T01:30:25+02:00"
```

A text format can also be passed directly as the second argument, with the culture as the third argument.

```m
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 1, 30, 25, -5, -30), "dd MMMM yyyy HH:mm zzz", "fr-FR")
```

```text
"31 décembre 2010 01:30 -05:30"
```

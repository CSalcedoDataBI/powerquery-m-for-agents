<!-- lab: desktop 2.159.883.0 -->

# Time.From

Text, numbers and datetimes convert to a time; null stays null.

```m
{Time.From(null), Time.From(0.75), Time.From(#datetime(2200, 1, 1, 13, 45, 0)), Time.From("10:12:31pm")}
```

```text
{null, #time(18, 0, 0), #time(13, 45, 0), #time(22, 12, 31)}
```

The culture argument changes how text is parsed.

```m
{Time.From("15:30", "de-DE"), Time.From("3:30 PM", "en-US")}
```

```text
{#time(15, 30, 0), #time(15, 30, 0)}
```

A number is read as a fraction of a day, so whole days may not be allowed.

```m
try Time.From(1.5)
```

```text
[HasError = true, Error = [Reason = "DataFormat.Error", Message = "We couldn't convert to Time.", Detail = 1.5, #"Message.Format" = "We couldn't convert to Time.", #"Message.Parameters" = null, ErrorCode = "10333"]]
```

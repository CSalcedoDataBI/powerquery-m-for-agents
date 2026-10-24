<!-- lab: desktop 2.159.883.0 -->

# Time.FromText

These examples show that null text returns null, that a custom format can ignore a date part, and that the culture option reads 12-hour times.

```m
{Time.FromText(null), Time.FromText("10:12:31", [Culture = "en-US"])}
```

```text
{null, #time(10, 12, 31)}
```

A `Format` string that includes a date component is rejected, even when the text also carries a time: the engine returns a `Parameter.Error` rather than keeping the time part.

```m
Time.FromText("30 Dec 2010 02:04:50.369730", [Format = "dd MMM yyyy HH:mm:ss.ffffff", Culture = "en-US"])
```

```text
error: Parameter.Error: We couldn't use the specified value as a time format because it includes a date component. | Detail: [Format = "dd MMM yyyy HH:mm:ss.ffffff"]
```

The 12-hour pattern `hh` together with `tt` reads the AM/PM marker. The pattern `HH` reads a 24-hour value.

```m
{Time.FromText("02:30 PM", [Format = "hh:mm tt", Culture = "en-US"]), Time.FromText("14:30", [Format = "HH:mm", Culture = "en-US"])}
```

```text
{#time(14, 30, 0), #time(14, 30, 0)}
```

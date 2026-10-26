<!-- lab: desktop 2.158.1304.0 -->

# DateTime.FromText returns a datetime, not a datetimezone

**What happens:** the card's one-line description (Microsoft's text) says it "creates a
datetimezone", but the signature and the engine return a `datetime`. Trust the signature.

```m
let v = DateTime.FromText("2024-01-02T03:04:05") in {Value.Type(v), v}
```

```text
{type datetime, #datetime(2024, 1, 2, 3, 4, 5)}
```

Text that carries an offset is not read at all: the offset is an error, not dropped.

```m
DateTime.FromText("2024-01-02T03:04:05+02:00")
```

```text
error: DataFormat.Error: We couldn't parse the input provided as a DateTime value. | Detail: "2024-01-02T03:04:05+02:00"
```

When the text has a zone, read it with `DateTimeZone.FromText`, which keeps it:

```m
let v = DateTimeZone.FromText("2024-01-02T03:04:05+02:00") in {Value.Type(v), v}
```

```text
{type datetimezone, #datetimezone(2024, 1, 2, 3, 4, 5, 2, 0)}
```

**Do this:** `DateTime.FromText` for local date and time, `DateTimeZone.FromText` for text with
an offset (then `DateTimeZone.RemoveZone` if the column must be a `datetime`). Pass the culture
of the data (`[Culture = "en-US"]`) when the text is not ISO 8601, as with `Number.FromText`
(★ note there).

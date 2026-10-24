<!-- lab: desktop 2.159.883.0 -->

# Json.FromValue

The result is binary, not text, so wrap it in Text.FromBinary to read it; nulls inside records and lists stay as JSON null.

```m
Text.FromBinary(Json.FromValue([a = null, b = {1, null, "x"}, c = true, d = "say ""hi"""]))
```

```text
"{""a"":null,""b"":[1,null,""x""],""c"":true,""d"":""say \""hi\""""}"
```

Dates, datetimes and decimals are written as JSON values; check the exact format before another system parses them.

```m
Text.FromBinary(Json.FromValue([d = #date(1990, 1, 2), dt = #datetime(2200, 1, 1, 12, 30, 0), n = 1.5, t = #time(9, 5, 0)]))
```

```text
"{""d"":""1990-01-02"",""dt"":""2200-01-01T12:30:00"",""n"":1.5,""t"":""09:05:00""}"
```

The optional encoding argument changes the bytes, not the JSON. The default is UTF-8, and UTF-16 roughly doubles the length.

```m
{Binary.Length(Json.FromValue("é")), Binary.Length(Json.FromValue("é", TextEncoding.Utf16)), Text.FromBinary(Json.FromValue("é", TextEncoding.Utf16), TextEncoding.Utf16)}
```

```text
{8, 16, """\u00e9"""}
```

<!-- lab: desktop 2.159.883.0 -->

# Expression.Identifier

Plain names come back unchanged, while names with spaces, keywords, quotes or a leading digit come back quoted as `#"..."`.

```m
{Expression.Identifier("Sales"), Expression.Identifier("Unit Price"), Expression.Identifier("2024 Total")}
```

```text
{"Sales", "#""Unit Price""", "#""2024 Total"""}
```

Keywords, dotted names and embedded quotes are edge cases.

```m
{Expression.Identifier("if"), Expression.Identifier("each"), Expression.Identifier("Text.Upper"), Expression.Identifier("Say ""hi""")}
```

```text
{"#""if""", "#""each""", "Text.Upper", "#""Say """"hi"""""""}
```

The empty string and null are also edge cases.

```m
{Expression.Identifier(""), try Expression.Identifier(null)}
```

```text
{"#""""", [HasError = true, Error = [Reason = "Expression.Error", Message = "We cannot convert the value null to type Text.", Detail = [Value = null, Type = type text], #"Message.Format" = "We cannot convert the value #{0} to type #{1}.", #"Message.Parameters" = {"null", "Text"}, ErrorCode = "10277"]]}
```

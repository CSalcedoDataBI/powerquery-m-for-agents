<!-- lab: desktop 2.157.879.0 -->

# Executed examples: text-conversions-from-and-to-text

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Character.FromNumber

These examples show how Character.FromNumber treats null, code points above 65535 and fractional numbers.

A null input is allowed by the signature.

```m
{Character.FromNumber(65), Character.FromNumber(9), Character.FromNumber(null)}
```

```text
{"A", "#(tab)", null}
```

A code point above 65535 may come back as more than one UTF-16 unit.

```m
[Char = Character.FromNumber(128512), Length = Text.Length(Character.FromNumber(128512))]
```

```text
[Char = "😀", Length = 2]
```

Fractional numbers and numbers outside the Unicode range.

```m
{try Character.FromNumber(65.6), try Character.FromNumber(-1), try Character.FromNumber(1114112)}
```

```text
{[HasError = true, Error = [Reason = "Expression.Error", Message = "The number is out of range of a 32 bit integer value.", Detail = 65.6, #"Message.Format" = "The number is out of range of a 32 bit integer value.", #"Message.Parameters" = null, ErrorCode = "10108"]], [HasError = true, Error = [Reason = "Expression.Error", Message = "We couldn't convert to Character.", Detail = -1, #"Message.Format" = "We couldn't convert to Character.", #"Message.Parameters" = null, ErrorCode = "10012"]], [HasError = true, Error = [Reason = "Expression.Error", Message = "We couldn't convert to Character.", Detail = 1114112, #"Message.Format" = "We couldn't convert to Character.", #"Message.Parameters" = null, ErrorCode = "10012"]]}
```

## Character.ToNumber

These examples show that the result is the character's code, not its digit value, and how null, empty and multi-character text behave.

```m
[Upper = Character.ToNumber("A"), Lower = Character.ToNumber("a"), Digit = Character.ToNumber("7"), Accented = Character.ToNumber("é")]
```

```text
[Upper = 65, Lower = 97, Digit = 55, Accented = 233]
```

```m
Character.ToNumber(null)
```

```text
null
```

```m
[TwoChars = try Character.ToNumber("AB"), Empty = try Character.ToNumber(""), Space = try Character.ToNumber(" ")]
```

```text
[TwoChars = [HasError = false, Value = 65], Empty = [HasError = true, Error = [Reason = "DataFormat.Error", Message = "We couldn't convert to Number.", Detail = "", #"Message.Format" = "We couldn't convert to Number.", #"Message.Parameters" = null, ErrorCode = "10041"]], Space = [HasError = false, Value = 32]]
```

## Guid.From

Different GUID spellings convert to the same text, and null passes through.

```m
{
    Guid.From("05FE1DADC8C24F3BA4C2D194116B4967"),
    Guid.From("{05FE1DAD-C8C2-4F3B-A4C2-D194116B4967}"),
    Guid.From("05fe1dad-c8c2-4f3b-a4c2-d194116b4967")
}
```

```text
{"05fe1dad-c8c2-4f3b-a4c2-d194116b4967", "05fe1dad-c8c2-4f3b-a4c2-d194116b4967", "05fe1dad-c8c2-4f3b-a4c2-d194116b4967"}
```

```m
Guid.From(null)
```

```text
null
```

Text that is not a GUID raises an error. It does not return null.

```m
try Guid.From("not-a-guid")
```

```text
[HasError = true, Error = [Reason = "DataFormat.Error", Message = "We couldn't convert to a guid.", Detail = "not-a-guid", #"Message.Format" = "We couldn't convert to a guid.", #"Message.Parameters" = null, ErrorCode = "10016"]]
```

## Json.FromValue

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

## Text.Format

Positional arguments from a list, named ones from a record.

```m
{Text.Format("#{0} of #{1}", {3, 10}), Text.Format("#[name] is #[age]", [name = "Ana", age = 30])}
```

```text
{"3 of 10", "Ana is 30"}
```

## Text.From

The culture decides the decimal separator.

```m
{Text.From(1234.5, "en-US"), Text.From(1234.5, "es-ES"), Text.From(null)}
```

```text
{"1234.5", "1234,5", null}
```

## Text.FromBinary

A round trip through UTF-8 bytes.

```m
Text.FromBinary(Text.ToBinary("héllo"), TextEncoding.Utf8)
```

```text
"héllo"
```

## Text.NewGuid

A new value on every call; its length is what is stable.

```m
Text.Length(Text.NewGuid())
```

```text
36
```

## Text.ToBinary

UTF-16 takes two bytes per character here.

```m
Text.ToBinary("AB", TextEncoding.Utf16)
```

```text
#binary({65, 0, 66, 0})
```

## Text.ToList

One item per character.

```m
Text.ToList("abc")
```

```text
{"a", "b", "c"}
```

## Value.FromText

Text is parsed to the type it looks like; culture changes how numbers are read; non-text input may not be parsed.

```m
[Number = Value.FromText("123"), Logical = Value.FromText("true"), Date = Value.FromText("2020-01-15"), Plain = Value.FromText("abc"), Padded = Value.FromText(" 123 ")]
```

```text
[Number = 123, Logical = true, Date = #date(2020, 1, 15), Plain = "abc", Padded = 123]
```

```m
[German = Value.FromText("1,5", "de-DE"), English = Value.FromText("1,5", "en-US"), NoCulture = Value.FromText("1.5")]
```

```text
[German = 1.5, English = 15, NoCulture = 1.5]
```

```m
[FromNull = try Value.FromText(null), FromNumber = try Value.FromText(42), FromNullWord = try Value.FromText("null")]
```

```text
[FromNull = [HasError = false, Value = null], FromNumber = [HasError = false, Value = 42], FromNullWord = [HasError = false, Value = null]]
```

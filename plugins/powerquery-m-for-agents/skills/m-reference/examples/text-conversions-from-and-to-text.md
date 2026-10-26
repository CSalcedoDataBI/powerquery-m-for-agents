<!-- lab: desktop 2.157.879.0 -->

# Executed examples: text-conversions-from-and-to-text

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

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

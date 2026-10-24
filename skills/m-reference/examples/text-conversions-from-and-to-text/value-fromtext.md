<!-- lab: desktop 2.159.883.0 -->

# Value.FromText

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

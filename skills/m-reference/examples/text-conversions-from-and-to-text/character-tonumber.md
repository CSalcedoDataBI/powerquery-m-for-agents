<!-- lab: desktop 2.159.883.0 -->

# Character.ToNumber

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

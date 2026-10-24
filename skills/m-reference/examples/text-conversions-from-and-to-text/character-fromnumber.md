<!-- lab: desktop 2.159.883.0 -->

# Character.FromNumber

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

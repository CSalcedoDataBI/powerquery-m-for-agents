<!-- lab: desktop 2.159.883.0 -->

# Executed examples: expression

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Expression.Constant

The examples show how values are turned back into M source text, including quoting, escapes and special values.

```m
Expression.Constant("Say ""hi""#(lf)now")
```

```text
"""Say """"hi""""#(#)(lf)now"""
```

```m
List.Transform({null, true, -0.5, #nan, #infinity, #date(1990, 1, 31), #duration(1, 2, 3, 4)}, Expression.Constant)
```

```text
{"null", "true", "-0.5", "#nan", "#infinity", "#date(1990, 1, 31)", "#duration(1, 2, 3, 4)"}
```

```m
Expression.Constant([a = {1, "x", null}, #"b c" = #datetime(2200, 12, 31, 23, 59, 59)])
```

```text
error: Expression.Error: Expected a constant value. Record is not a constant. | Detail: [a = {1, "x", null}, #"b c" = #datetime(2200, 12, 31, 23, 59, 59)]
```

## Expression.Identifier

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

## Value.Expression

Value.Expression does not resolve a plain value: a literal, null and a function all return the same error asking for `Value.Expression(Value.Optimize(...))` first.

```m
Value.Expression(42)
```

```text
error: Expression.Error: Value.Expression can only resolve optimized expressions, use: Value.Expression(Value.Optimize(...))
```

```m
Value.Expression(null)
```

```text
error: Expression.Error: Value.Expression can only resolve optimized expressions, use: Value.Expression(Value.Optimize(...))
```

```m
Value.Expression(each _ + 1)
```

```text
error: Expression.Error: Value.Expression can only resolve optimized expressions, use: Value.Expression(Value.Optimize(...))
```

<!-- lab: desktop 2.159.883.0 -->

# Expression.Constant

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

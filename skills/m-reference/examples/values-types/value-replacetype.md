<!-- lab: desktop 2.159.883.0 -->

# Value.ReplaceType

The new type is attached to the value without converting it. Column names change by position, values keep their own type, and an incompatible type is an error.

```m
Value.ReplaceType(#table({"A", "B"}, {{1, 2}}), type table [X = number, Y = number])
```

```text
#table(type table [X = number, Y = number], {{1, 2}})
```

```m
let
    t = Value.ReplaceType(#table({"A"}, {{"1"}}), type table [A = number])
in
    [IsNumber = Value.Is(t{0}[A], type number), IsText = Value.Is(t{0}[A], type text)]
```

```text
[IsNumber = false, IsText = true]
```

```m
Value.ReplaceType(1, type text)
```

```text
error: Expression.Error: We cannot convert the value 1 to type Text. | Detail: [Value = 1, Type = type text]
```

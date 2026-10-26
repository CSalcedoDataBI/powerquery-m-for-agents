<!-- lab: desktop 2.157.879.0 -->

# BinaryFormat.Decimal

These examples show how the .NET decimal's scale byte and null input affect the value returned.

```m
BinaryFormat.Decimal(#binary({1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}))
```

```text
1
```

```m
BinaryFormat.Decimal(#binary({1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0}))
```

```text
0.1
```

```m
BinaryFormat.Decimal(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

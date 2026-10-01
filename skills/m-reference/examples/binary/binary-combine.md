<!-- lab: desktop 2.157.879.0 -->

# Binary.Combine

Combining binaries concatenates their bytes in list order.

```m
Binary.Combine({Text.ToBinary("ab"), Text.ToBinary("cd")})
```

```text
#binary({97, 98, 99, 100})
```

An empty list produces an empty binary rather than an error.

```m
Binary.Combine({})
```

```text
#binary({})
```

A null item is not skipped or treated as empty; it is rejected.

```m
Binary.Combine({Text.ToBinary("a"), null})
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

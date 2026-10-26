<!-- lab: desktop 2.157.879.0 -->

# Binary.Split

Examples cover a short final page, a page size larger than the binary, and a null input.

```m
Binary.Split(Text.ToBinary("abcde"), 2)
```

```text
{#binary({97, 98}), #binary({99, 100}), #binary({101})}
```

```m
Binary.Split(Text.ToBinary("abc"), 5)
```

```text
{#binary({97, 98, 99})}
```

```m
Binary.Split(null, 2)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

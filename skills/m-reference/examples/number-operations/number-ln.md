<!-- lab: desktop 2.157.879.0 -->

# Number.Ln

These examples show null handling and the boundary values where the natural logarithm stops returning an ordinary number.

```m
Number.Ln(null)
```

```text
null
```

```m
List.Transform({0, 1, Number.E}, Number.Ln)
```

```text
{-#infinity, 0, 1}
```

```m
Number.Ln(-1)
```

```text
#nan
```

<!-- lab: desktop 2.157.879.0 -->

# List.SingleOrDefault

Empty gives the default; more than one is still an error.

```m
{List.SingleOrDefault({}, "none"), List.SingleOrDefault({1, 2})}
```

```text
{"none", error: Expression.Error: There were too many elements in the enumeration to complete the operation. | Detail: {1, 2}}
```

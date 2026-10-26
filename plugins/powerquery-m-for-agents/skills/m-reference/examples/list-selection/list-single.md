<!-- lab: desktop 2.157.879.0 -->

# List.Single

Exactly one item, or an error.

```m
{List.Single({7}), List.Single({1, 2})}
```

```text
{7, error: Expression.Error: There were too many elements in the enumeration to complete the operation. | Detail: {1, 2}}
```

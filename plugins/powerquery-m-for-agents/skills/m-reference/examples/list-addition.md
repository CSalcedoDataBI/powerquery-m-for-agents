<!-- lab: desktop 2.157.879.0 -->

# Executed examples: list-addition

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## List.Sum

Nulls ignored, empty gives null, and decimal precision.

```m
{List.Sum({1, null, 2}), List.Sum({}), List.Sum({0.1, 0.2}), List.Sum({0.1, 0.2}, Precision.Decimal)}
```

```text
{3, null, 0.30000000000000004, 0.3}
```

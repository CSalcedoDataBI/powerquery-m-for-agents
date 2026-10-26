<!-- lab: desktop 2.157.879.0 -->

# Executed examples: list-set-operations

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## List.Difference

One match removes one occurrence, not all.

```m
List.Difference({1, 2, 2, 3}, {2})
```

```text
{1, 2, 3}
```

## List.Intersect

Duplicates survive as many times as both lists have them.

```m
List.Intersect({{1, 2, 2, 3}, {2, 2, 4}})
```

```text
{2, 2}
```

## List.Union

Duplicates survive as many times as the list that has most.

```m
List.Union({{1, 2, 2}, {2, 3}})
```

```text
{1, 2, 2, 3}
```

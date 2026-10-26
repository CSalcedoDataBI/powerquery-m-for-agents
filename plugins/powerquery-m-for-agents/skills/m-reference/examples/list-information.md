<!-- lab: desktop 2.157.879.0 -->

# Executed examples: list-information

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## List.Count

Nulls count as items.

```m
List.Count({1, null, 3})
```

```text
3
```

## List.IsEmpty

Empty or not.

```m
{List.IsEmpty({}), List.IsEmpty({null})}
```

```text
{true, false}
```

## List.NonNullCount

Nulls are not counted.

```m
List.NonNullCount({1, null, 3})
```

```text
2
```

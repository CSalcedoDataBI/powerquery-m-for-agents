<!-- lab: desktop 2.157.879.0 -->

# Executed examples: list-averages

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## List.Average

Nulls are ignored; an empty list gives null.

```m
{List.Average({1, 2, null, 6}), List.Average({})}
```

```text
{3, null}
```

## List.Mode

The most frequent item.

```m
List.Mode({1, 2, 2, 3})
```

```text
2
```

## List.Modes

All items tied for most frequent.

```m
List.Modes({1, 1, 2, 2, 3})
```

```text
{1, 2}
```

## List.StandardDeviation

The sample standard deviation.

```m
List.StandardDeviation({2, 4, 4, 4, 5, 5, 7, 9})
```

```text
2.1380899352993952
```

<!-- lab: desktop 2.157.879.0 -->

# Executed examples: list-ordering

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## List.Max

Nulls ignored; empty gives null or the default.

```m
{List.Max({1, 5, null}), List.Max({}), List.Max({}, 0)}
```

```text
{5, null, 0}
```

## List.MaxN

The two largest, largest first.

```m
List.MaxN({5, 1, 9, 3}, 2)
```

```text
{9, 5}
```

## List.Median

Odd and even counts.

```m
{List.Median({1, 3, 2}), List.Median({1, 2, 3, 4})}
```

```text
{2, 2.5}
```

## List.Min

Texts compare too.

```m
List.Min({"b", "a"})
```

```text
"a"
```

## List.MinN

The two smallest.

```m
List.MinN({5, 1, 9, 3}, 2)
```

```text
{1, 3}
```

## List.Percentile

One percentile, or several at once.

```m
{List.Percentile({1, 2, 3, 4}, 0.5), List.Percentile({1, 2, 3, 4}, {0.25, 0.75})}
```

```text
{2.5, {1.75, 3.25}}
```

## List.Sort

Ascending, descending, and how case sorts.

```m
{List.Sort({3, 1, 2}), List.Sort({3, 1, 2}, Order.Descending), List.Sort({"b", "A", "a"})}
```

```text
{{1, 2, 3}, {3, 2, 1}, {"A", "a", "b"}}
```

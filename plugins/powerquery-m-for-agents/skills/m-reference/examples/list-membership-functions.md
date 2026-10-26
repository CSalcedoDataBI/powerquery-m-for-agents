<!-- lab: desktop 2.157.879.0 -->

# Executed examples: list-membership-functions

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## List.AllTrue

An empty list is all true.

```m
{List.AllTrue({true, true}), List.AllTrue({true, false}), List.AllTrue({})}
```

```text
{true, false, true}
```

## List.AnyTrue

An empty list is not any true.

```m
{List.AnyTrue({false, true}), List.AnyTrue({})}
```

```text
{true, false}
```

## List.Contains

Case-sensitive unless given a comparer.

```m
{List.Contains({"a", "b"}, "A"), List.Contains({"a", "b"}, "A", Comparer.OrdinalIgnoreCase)}
```

```text
{false, true}
```

## List.ContainsAll

Every value must be present.

```m
{List.ContainsAll({1, 2, 3}, {1, 3}), List.ContainsAll({1, 2, 3}, {1, 4})}
```

```text
{true, false}
```

## List.ContainsAny

One value is enough.

```m
List.ContainsAny({1, 2, 3}, {4, 3})
```

```text
true
```

## List.PositionOf

Every position, and -1 when absent.

```m
{List.PositionOf({"a", "b", "a"}, "a", Occurrence.All), List.PositionOf({"a"}, "z")}
```

```text
{{0, 2}, -1}
```

## List.PositionOfAny

The first position of any of the values.

```m
List.PositionOfAny({"a", "b", "c"}, {"c", "b"})
```

```text
1
```

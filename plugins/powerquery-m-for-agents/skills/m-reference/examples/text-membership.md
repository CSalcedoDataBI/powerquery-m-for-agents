<!-- lab: desktop 2.157.879.0 -->

# Executed examples: text-membership

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Text.Contains

Case-sensitive by default; a comparer makes it case-insensitive.

```m
{Text.Contains("Hello", "ell"), Text.Contains("Hello", "ELL"), Text.Contains("Hello", "ELL", Comparer.OrdinalIgnoreCase)}
```

```text
{true, false, true}
```

## Text.EndsWith

With and without a case-insensitive comparer.

```m
{Text.EndsWith("report.csv", ".CSV"), Text.EndsWith("report.csv", ".CSV", Comparer.OrdinalIgnoreCase)}
```

```text
{false, true}
```

## Text.PositionOf

First, last, all, and not found.

```m
{Text.PositionOf("banana", "an"), Text.PositionOf("banana", "an", Occurrence.Last), Text.PositionOf("banana", "an", Occurrence.All), Text.PositionOf("banana", "x")}
```

```text
{1, 3, {1, 3}, -1}
```

## Text.PositionOfAny

Every position of any of the characters.

```m
Text.PositionOfAny("hello", {"l", "o"}, Occurrence.All)
```

```text
{2, 3, 4}
```

## Text.StartsWith

Case-sensitive unless given a comparer.

```m
{Text.StartsWith("Hello", "he"), Text.StartsWith("Hello", "he", Comparer.OrdinalIgnoreCase)}
```

```text
{false, true}
```

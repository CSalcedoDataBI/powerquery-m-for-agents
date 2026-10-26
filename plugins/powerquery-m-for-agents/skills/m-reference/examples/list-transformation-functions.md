<!-- lab: desktop 2.157.879.0 -->

# Executed examples: list-transformation-functions

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## List.Accumulate

A running fold: the sum, written by hand.

```m
List.Accumulate({1, 2, 3}, 0, (state, current) => state + current)
```

```text
6
```

## List.Combine

Concatenate lists.

```m
List.Combine({{1, 2}, {3}, {}})
```

```text
{1, 2, 3}
```

## List.ConformToPageReader

Called directly on a list, it returns a table of one-row tables.

```m
List.ConformToPageReader({1, 2})
```

```text
#table(type table [Result = any], {{#table(type table [Value = number], {{1}})}, {#table(type table [Value = number], {{2}})}})
```

## List.RemoveFirstN

Drop the first item.

```m
List.RemoveFirstN({1, 2, 3}, 1)
```

```text
{2, 3}
```

## List.RemoveItems

Every occurrence goes, unlike List.Difference.

```m
List.RemoveItems({1, 2, 2, 3}, {2})
```

```text
{1, 3}
```

## List.RemoveLastN

Drop the last two.

```m
List.RemoveLastN({1, 2, 3}, 2)
```

```text
{1}
```

## List.RemoveMatchingItems

Case-insensitive removal.

```m
List.RemoveMatchingItems({"a", "A", "b"}, {"a"}, Comparer.OrdinalIgnoreCase)
```

```text
{"b"}
```

## List.RemoveNulls

Nulls removed.

```m
List.RemoveNulls({1, null, 2})
```

```text
{1, 2}
```

## List.RemoveRange

Remove two items from position 1.

```m
List.RemoveRange({1..5}, 1, 2)
```

```text
{1, 4, 5}
```

## List.Repeat

The whole list, twice.

```m
List.Repeat({1, 2}, 2)
```

```text
{1, 2, 1, 2}
```

## List.ReplaceMatchingItems

Pairs of old and new values.

```m
List.ReplaceMatchingItems({1, 2, 3}, {{2, 20}})
```

```text
{1, 20, 3}
```

## List.ReplaceRange

Two items replaced by one.

```m
List.ReplaceRange({1..5}, 1, 2, {"x"})
```

```text
{1, "x", 4, 5}
```

## List.ReplaceValue

The replacer decides: part of a text, or the whole value.

```m
{List.ReplaceValue({"ab", "b"}, "b", "z", Replacer.ReplaceText), List.ReplaceValue({"ab", "b"}, "b", "z", Replacer.ReplaceValue)}
```

```text
{{"az", "z"}, {"ab", "z"}}
```

## List.Reverse

Reverse order.

```m
List.Reverse({1, 2, 3})
```

```text
{3, 2, 1}
```

## List.Split

Pages of two.

```m
List.Split({1..5}, 2)
```

```text
{{1, 2}, {3, 4}, {5}}
```

## List.Transform

Apply a function to every item.

```m
List.Transform({1, 2}, each _ * 10)
```

```text
{10, 20}
```

## List.TransformMany

Every item paired with every item of its collection.

```m
List.TransformMany({1, 2}, each {"a", "b"}, (x, y) => Text.From(x) & y)
```

```text
{"1a", "1b", "2a", "2b"}
```

## List.Zip

Shorter lists are padded with null.

```m
List.Zip({{1, 2, 3}, {"a", "b"}})
```

```text
{{1, "a"}, {2, "b"}, {3, null}}
```

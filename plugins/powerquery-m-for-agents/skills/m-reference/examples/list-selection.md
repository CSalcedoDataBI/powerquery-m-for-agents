<!-- lab: desktop 2.157.879.0 -->

# Executed examples: list-selection

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## List.Alternate

Keep the first item, then skip 1 and keep 2, over and over.

```m
List.Alternate({1..10}, 1, 2, 1)
```

```text
{1, 3, 4, 6, 7, 9, 10}
```

## List.Buffer

Buffering returns the same items, held in memory.

```m
List.Buffer({3, 1, 2})
```

```text
{3, 1, 2}
```

## List.Distinct

Plain and case-insensitive.

```m
{List.Distinct({1, 1, 2}), List.Distinct({"a", "A", "b"}, Comparer.OrdinalIgnoreCase)}
```

```text
{{1, 2}, {"a", "b"}}
```

## List.FindText

Items containing the text, case-sensitive.

```m
List.FindText({"apple", "banana", "BANANA"}, "an")
```

```text
{"banana"}
```

## List.First

Empty list: null, or the default given.

```m
{List.First({1, 2}), List.First({}), List.First({}, "none")}
```

```text
{1, null, "none"}
```

## List.FirstN

A count, or a condition that stops at the first item failing it.

```m
{List.FirstN({1, 2, 3, 4}, 2), List.FirstN({1, 2, 5, 1}, each _ < 3)}
```

```text
{{1, 2}, {1, 2}}
```

## List.InsertRange

Insert values at a position.

```m
List.InsertRange({1, 4}, 1, {2, 3})
```

```text
{1, 2, 3, 4}
```

## List.IsDistinct

Any repeat makes it false.

```m
List.IsDistinct({1, 2, 1})
```

```text
false
```

## List.Last

The last item.

```m
List.Last({1, 2, 3})
```

```text
3
```

## List.LastN

The last items.

```m
List.LastN({1, 2, 3, 4}, 2)
```

```text
{3, 4}
```

## List.MatchesAll

Every item passes.

```m
List.MatchesAll({2, 4}, each _ > 1)
```

```text
true
```

## List.MatchesAny

At least one item passes.

```m
List.MatchesAny({1, 2}, each _ > 1)
```

```text
true
```

## List.Positions

Zero-based positions.

```m
List.Positions({"x", "y"})
```

```text
{0, 1}
```

## List.Range

Three items from offset 2.

```m
List.Range({1..10}, 2, 3)
```

```text
{3, 4, 5}
```

## List.Select

Keep the even numbers.

```m
List.Select({1..6}, each Number.Mod(_, 2) = 0)
```

```text
{2, 4, 6}
```

## List.Single

Exactly one item, or an error.

```m
{List.Single({7}), List.Single({1, 2})}
```

```text
{7, error: Expression.Error: There were too many elements in the enumeration to complete the operation. | Detail: {1, 2}}
```

## List.SingleOrDefault

Empty gives the default; more than one is still an error.

```m
{List.SingleOrDefault({}, "none"), List.SingleOrDefault({1, 2})}
```

```text
{"none", error: Expression.Error: There were too many elements in the enumeration to complete the operation. | Detail: {1, 2}}
```

## List.Skip

Skip while the condition holds.

```m
List.Skip({1..5}, each _ < 3)
```

```text
{3, 4, 5}
```

<!-- lab: desktop 2.157.879.0 -->

# Lazy evaluation and streaming

M evaluates a value only when something needs it, and item by item when it can. Three
consequences shape how queries behave.

## What is not read is not computed

A list item that is never read is never evaluated, even when it is an error.

```m
List.First(List.Transform({1, 2, error "boom"}, each _ * 10))
```

```text
10
```

An infinite list is fine as long as only part of it is read.

```m
List.FirstN(List.Generate(() => 1, each true, each _ + 1), 3)
```

```text
{1, 2, 3}
```

## Buffering keeps errors as values

`List.Buffer` and `Table.Buffer` read the whole value into memory, but an item that is an
error is stored as an error, not raised: the other items still read fine, and the error
surfaces only when its own item is read.

```m
List.First(List.Buffer({1, error "boom"}))
```

```text
1
```

```m
List.Buffer({1, error "boom"}){1}
```

```text
error: Expression.Error: boom
```

Buffering does change order-sensitive results: see the ★ note on `Table.Distinct`.

## A name is evaluated once

Inside a `let`, a name holds one value however many times it is used. Two calls of a
non-deterministic function are two values; one name is one.

```m
{Text.NewGuid() = Text.NewGuid(), let g = Text.NewGuid() in g = g}
```

```text
{false, true}
```

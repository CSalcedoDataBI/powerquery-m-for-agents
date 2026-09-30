<!-- lab: desktop 2.157.879.0 -->

# Records, lists and tables

The three structured values. A **list** is ordered and positional, a **record** is a set of
named fields, a **table** is a list of rows that share a record type.

## Lists

`{}` builds a list; `{n}` reads the item at zero-based position `n`. Past the end is an error;
`{n}?` returns null instead.

```m
let L = {"a", "b"} in {L{1}, L{5}?}
```

```text
{"b", null}
```

```m
{"a", "b"}{5}
```

```text
error: Expression.Error: There weren't enough elements in the enumeration to complete the operation. | Detail: {"a", "b"}
```

`..` builds a range, for numbers and for single characters.

```m
{{1..4}, {"a".."d"}}
```

```text
{{1, 2, 3, 4}, {"a", "b", "c", "d"}}
```

## Records

`[]` builds a record; `r[field]` reads a field. A missing field is an error; `r[field]?` returns
null instead.

```m
let r = [a = 1, b = 2] in {r[a], r[c]?}
```

```text
{1, null}
```

```m
[a = 1][c]
```

```text
error: Expression.Error: The field 'c' of the record wasn't found. | Detail: [a = 1]
```

## Tables

`T{n}` is a row (a record), `T[Column]` is a column (a list), and `T{[Key = value]}` finds the
one row whose fields match.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {T{0}, T[Qty], T{[Name = "b"]}}
```

```text
{[Name = "a", Qty = 1], {1, 2, 3}, [Name = "b", Qty = 2]}
```

The lookup must match exactly one row: two matches are an error, not the first one.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    T{[Name = "a"]}
```

```text
error: Expression.Error: The key matched more than one row in the table. | Detail: [Key = [Name = "a"], Table = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})]
```

## Combining with &

`&` concatenates lists and tables and merges records. In a record merge, the right side wins
a field both have.

```m
{{1} & {2}, [a = 1] & [b = 2], [a = 1] & [a = 9]}
```

```text
{{1, 2}, [a = 1, b = 2], [a = 9]}
```

```m
#table({"x"}, {{1}}) & #table({"y"}, {{2}})
```

```text
#table(type table [x = any, y = any], {{1, null}, {null, 2}})
```

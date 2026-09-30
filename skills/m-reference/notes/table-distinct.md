<!-- lab: desktop 2.157.879.0 -->

# Table.Distinct after Table.Sort

**Confirmed here, even in memory:** `Table.Distinct` does not keep the first row of a sorted
table unless the sort is buffered. Without `Table.Buffer`, the row kept for key `a` is the one
that came first in the **original** order (`Date = 1`), not after the sort (`Date = 3`).

**Do this:** to keep the latest (or best) row per key, buffer the sorted table before
`Table.Distinct` - or avoid depending on order at all: `Table.Group` by the key with
`Table.Max` over the rows.

Sorted, not buffered:

```m
let
    T = #table(type table [Key = text, Date = Int64.Type], {{"a", 1}, {"a", 3}, {"b", 2}, {"a", 2}}),
    Sorted = Table.Sort(T, {{"Date", Order.Descending}})
in
    Table.Distinct(Sorted, {"Key"})
```

```text
#table(type table [Key = text, Date = Int64.Type], {{"b", 2}, {"a", 1}})
```

Sorted and buffered:

```m
let
    T = #table(type table [Key = text, Date = Int64.Type], {{"a", 1}, {"a", 3}, {"b", 2}, {"a", 2}}),
    Sorted = Table.Buffer(Table.Sort(T, {{"Date", Order.Descending}}))
in
    Table.Distinct(Sorted, {"Key"})
```

```text
#table(type table [Key = text, Date = Int64.Type], {{"a", 3}, {"b", 2}})
```

The order-independent way:

```m
let
    T = #table(type table [Key = text, Date = Int64.Type], {{"a", 1}, {"a", 3}, {"b", 2}, {"a", 2}})
in
    Table.Group(T, {"Key"}, {{"Latest", each Table.Max(_, "Date"), type record}})
```

```text
#table(type table [Key = text, Latest = [...]], {{"a", [Key = "a", Date = 3]}, {"b", [Key = "b", Date = 2]}})
```

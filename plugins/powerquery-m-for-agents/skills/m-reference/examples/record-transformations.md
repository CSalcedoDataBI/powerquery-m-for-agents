<!-- lab: desktop 2.157.879.0 -->

# Executed examples: record-transformations

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Record.AddField

A null value still adds the field.

```m
Record.AddField([CustomerID = 1, Name = "Bob"], "MiddleName", null)
```

```text
[CustomerID = 1, Name = "Bob", MiddleName = null]
```

With the optional delayed argument set to true, the value is a function and its result becomes the field.

```m
Record.AddField([CustomerID = 1], "Score", () => 42, true)
```

```text
[CustomerID = 1, Score = 42]
```

A record value is stored as a single field and is not merged into the outer record.

```m
Record.AddField([CustomerID = 1], "Address", [City = "Seattle"])
```

```text
[CustomerID = 1, Address = [City = "Seattle"]]
```

## Record.Combine

Nulls survive the combine and edge-case lists still produce a record.

```m
Record.Combine({[A = 1, B = null], [C = null]})
```

```text
[A = 1, B = null, C = null]
```

An empty list of records gives an empty record.

```m
Record.Combine({})
```

```text
[]
```

When a field name appears in more than one record, the later record's value wins.

```m
Record.Combine({[A = 1, B = 2], [B = 3, C = 4]})
```

```text
[A = 1, B = 3, C = 4]
```

## Record.RemoveFields

A null value is still a present field, but removing an absent field name raises an error unless the optional argument ignores it.

```m
Record.RemoveFields([A = null, B = 1], "A")
```

```text
[B = 1]
```

```m
Record.RemoveFields([A = 1, B = 2], "C")
```

```text
error: Expression.Error: The field 'C' of the record wasn't found. | Detail: [A = 1, B = 2]
```

```m
Record.RemoveFields([A = 1, B = 2], {"B", "C"}, MissingField.Ignore)
```

```text
[A = 1]
```

## Record.RenameFields

These examples show a null value, multiple renames, and the optional `missingField` argument.

Renaming a field keeps its value, including a null value.

```m
Record.RenameFields([A = 1, B = null, C = 3], {"B", "Renamed"})
```

```text
[A = 1, Renamed = null, C = 3]
```

Several renames are written as a list of old/new pairs.

```m
Record.RenameFields([Old1 = 1, Old2 = 2, Keep = 3], {{"Old1", "New1"}, {"Old2", "New2"}})
```

```text
[New1 = 1, New2 = 2, Keep = 3]
```

An absent rename source errors by default; `MissingField.Ignore` skips it, while `MissingField.UseNull` adds the new field with a null value.

```m
Record.RenameFields([A = 1, B = 2], {{"A", "X"}, {"Missing", "Y"}}, MissingField.UseNull)
```

```text
[X = 1, B = 2, Y = null]
```

## Record.ReorderFields

The named fields move; every field that is not named keeps its original position.

```m
Record.ReorderFields([CustomerID = 1, OrderID = 2, Item = "Rod", Price = 3.5], {"Price", "OrderID"})
```

```text
[CustomerID = 1, Price = 3.5, Item = "Rod", OrderID = 2]
```

With `MissingField.UseNull`, a name that is absent from the record is added as `null` and still takes a position in the new order.

```m
Record.ReorderFields([CustomerID = 3, Phone = "543-7890"], {"Phone", "Purchase", "CustomerID"}, MissingField.UseNull)
```

```text
[Phone = "543-7890", Purchase = null, CustomerID = 3]
```

With `MissingField.Ignore`, absent names are skipped, and a field whose value is `null` keeps that value.

```m
Record.ReorderFields([A = null, B = 2, C = 3], {"C", "Missing", "A"}, MissingField.Ignore)
```

```text
[C = 3, B = 2, A = null]
```

## Record.TransformFields

The examples show the flat single-field form, the list-of-lists form for several fields, and how null and missing values are handled.

A single field takes a flat two-item list, and the other fields are left alone.

```m
Record.TransformFields([Price = "100", Currency = "usd"], {"Price", Number.FromText})
```

```text
[Price = 100, Currency = "usd"]
```

Several fields take a list of pairs, and a null field stays null under a Text function.

```m
Record.TransformFields(
    [Code = "ab-12", Qty = "3", Note = null],
    {{"Code", Text.Upper}, {"Qty", Number.FromText}, {"Note", Text.Trim}}
)
```

```text
[Code = "AB-12", Qty = 3, Note = null]
```

A field named in the operations but absent from the record is skipped when the optional third argument is MissingField.Ignore.

```m
Record.TransformFields(
    [First = "ada", Last = "lovelace"],
    {{"First", Text.Proper}, {"Last", Text.Proper}, {"Title", Text.Proper}},
    MissingField.Ignore
)
```

```text
[First = "Ada", Last = "Lovelace"]
```

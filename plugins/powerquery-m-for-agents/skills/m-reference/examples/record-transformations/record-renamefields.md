<!-- lab: desktop 2.157.879.0 -->

# Record.RenameFields

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

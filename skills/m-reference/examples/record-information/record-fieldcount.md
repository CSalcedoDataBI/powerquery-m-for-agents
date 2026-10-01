<!-- lab: desktop 2.157.879.0 -->

# Record.FieldCount

Fields holding null still count, an empty record has no fields, and a nested record counts as a single field.

```m
Record.FieldCount([Name = "Bob", MiddleName = null, Nickname = null])
```

```text
3
```

```m
Record.FieldCount([])
```

```text
0
```

```m
Record.FieldCount([Outer = [Inner1 = 1, Inner2 = 2]])
```

```text
1
```

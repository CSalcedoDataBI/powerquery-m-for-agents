<!-- lab: desktop 2.157.879.0 -->

# Record.AddField

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

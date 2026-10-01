<!-- lab: desktop 2.157.879.0 -->

# Record.HasFields

Shows how null field values, missing names in a list, and case mismatches are handled.

```m
Record.HasFields([CustomerID = null, Name = "Bob"], "CustomerID")
```

```text
true
```

```m
Record.HasFields([CustomerID = 1, Name = "Bob"], {"CustomerID", "Address"})
```

```text
false
```

```m
Record.HasFields([Name = "Bob"], "name")
```

```text
false
```

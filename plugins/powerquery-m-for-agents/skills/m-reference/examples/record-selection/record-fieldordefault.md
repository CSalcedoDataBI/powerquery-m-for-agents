<!-- lab: desktop 2.157.879.0 -->

# Record.FieldOrDefault

These examples show what the optional default does when a field is missing, when it exists, and when its value is null.

```m
Record.FieldOrDefault([CustomerID = 1, Name = "Bob"], "Phone")
```

```text
null
```

```m
Record.FieldOrDefault([CustomerID = 1, Name = "Bob"], "Phone", "123-4567")
```

```text
"123-4567"
```

```m
Record.FieldOrDefault([CustomerID = 1, Phone = null], "Phone", "123-4567")
```

```text
null
```

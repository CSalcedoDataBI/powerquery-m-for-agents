<!-- lab: desktop 2.157.879.0 -->

# Record.ReorderFields

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

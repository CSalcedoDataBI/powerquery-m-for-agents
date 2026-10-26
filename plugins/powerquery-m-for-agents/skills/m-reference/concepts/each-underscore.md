<!-- lab: desktop 2.157.879.0 -->

# each and _

`each <body>` is shorthand for a one-parameter function whose parameter is named `_`:
`(_) => <body>`. Both forms give the same result.

```m
{List.Transform({1, 2}, each _ + 1), List.Transform({1, 2}, (_) => _ + 1)}
```

```text
{{2, 3}, {2, 3}}
```

Inside `each`, a bare `[Field]` means `_[Field]`. That is why a row function can say
`[Qty]` without naming the row.

```m
Table.AddColumn(#table({"Qty"}, {{2}, {5}}), "Double", each [Qty] * 2)
```

```text
#table(type table [Qty = any, Double = any], {{2, 4}, {5, 10}})
```

## A nested each shadows the outer _

Each `each` declares its own `_`. Inside the inner one, the outer value is out of reach: here
the outer items 1 and 2 never appear in the result.

```m
List.Transform({1, 2}, each List.Transform({10, 20}, each _ + 1))
```

```text
{{11, 21}, {11, 21}}
```

Name the outer parameter instead, and the inner `each` can still use `_`.

```m
List.Transform({1, 2}, (outer) => List.Transform({10, 20}, each outer + _))
```

```text
{{11, 21}, {12, 22}}
```

The same trap with fields is quieter, because it does not fail. Counting each customer's
orders with two `each`: the inner `[Customer]` refers to the order row on **both** sides of
`=`, so every order matches every customer.

```m
let
    Orders = #table({"Id", "Customer"}, {{1, "a"}, {2, "b"}, {3, "a"}}),
    Customers = #table({"Customer"}, {{"a"}, {"b"}})
in
    Table.AddColumn(Customers, "Orders",
        each Table.RowCount(Table.SelectRows(Orders, each [Customer] = [Customer])))
```

```text
#table(type table [Customer = any, Orders = any], {{"a", 3}, {"b", 3}})
```

Naming the outer row gives the intended count.

```m
let
    Orders = #table({"Id", "Customer"}, {{1, "a"}, {2, "b"}, {3, "a"}}),
    Customers = #table({"Customer"}, {{"a"}, {"b"}})
in
    Table.AddColumn(Customers, "Orders",
        (c) => Table.RowCount(Table.SelectRows(Orders, each [Customer] = c[Customer])))
```

```text
#table(type table [Customer = any, Orders = any], {{"a", 2}, {"b", 1}})
```

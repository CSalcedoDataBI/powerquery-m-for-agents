<!-- lab: desktop 2.159.883.0 -->

# Tables.GetRelationships

The examples show the default `Data` column, a differently named data column passed as `dataColumn`, and a missing `Data` column.

```m
Tables.GetRelationships(
    #table({"Name", "Data"}, {
        {"Orders", Table.AddKey(#table({"OrderID", "CustomerID"}, {{1, 10}, {2, 20}}), {"OrderID"}, true)},
        {"Customers", Table.AddKey(#table({"CustomerID", "City"}, {{10, "Seattle"}, {20, "Redmond"}}), {"CustomerID"}, true)}
    })
)
```

```text
error: Expression.Error: The argument value isn't valid. | Detail: "dataColumn"
```

```m
Tables.GetRelationships(
    #table({"Name", "Tbl"}, {
        {"Orders", Table.AddKey(#table({"OrderID", "CustomerID"}, {{1, 10}}), {"OrderID"}, true)},
        {"Customers", Table.AddKey(#table({"CustomerID", "City"}, {{10, "Seattle"}}), {"CustomerID"}, true)}
    }),
    "Tbl"
)
```

```text
error: Expression.Error: We can't get the relationships. A primary or unique key is required to perform the operation against the table.
```

```m
Tables.GetRelationships(
    #table({"Name", "Tbl"}, {
        {"Orders", #table({"OrderID"}, {{1}})}
    })
)
```

```text
error: Expression.Error: The argument value isn't valid. | Detail: "dataColumn"
```

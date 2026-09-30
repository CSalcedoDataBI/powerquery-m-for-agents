<!-- lab: desktop 2.157.879.0 -->

# Table.ReplaceValue

The replacer decides: the whole value, or part of a text.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.ReplaceValue(T, "a", "A", Replacer.ReplaceValue, {"Name"}), Table.ReplaceValue(#table({"s"}, {{"banana"}}), "an", "AN", Replacer.ReplaceText, {"s"})}
```

```text
{#table(type table [Name = text, Qty = Int64.Type], {{"A", 1}, {"b", 2}, {"A", 3}}), #table(type table [s = nullable text], {{"bANANa"}})}
```

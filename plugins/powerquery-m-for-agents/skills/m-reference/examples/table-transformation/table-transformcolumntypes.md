<!-- lab: desktop 2.157.879.0 -->

# Table.TransformColumnTypes

The culture decides how the same text reads as a date.

```m
{Table.TransformColumnTypes(#table({"d"}, {{"1/2/2024"}}), {{"d", type date}}, "en-US"), Table.TransformColumnTypes(#table({"d"}, {{"1/2/2024"}}), {{"d", type date}}, "es-ES")}
```

```text
{#table(type table [d = nullable date], {{#date(2024, 1, 2)}}), #table(type table [d = nullable date], {{#date(2024, 2, 1)}})}
```

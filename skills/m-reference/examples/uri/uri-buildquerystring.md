<!-- lab: desktop 2.159.883.0 -->

# Uri.BuildQueryString

The examples show how values are encoded, how list values repeat a key, and what happens with non-text values.

Spaces and reserved characters in values are percent-encoded.

```m
Uri.BuildQueryString([q = "a b&c=d", lang = "en-US"])
```

```text
"q=a%20b%26c%3Dd&lang=en-US"
```

A list value repeats its key once for each item.

```m
Uri.BuildQueryString([tag = {"x", "y"}, page = "1"])
```

```text
"tag=x&tag=y&page=1"
```

Numbers and nulls are not converted to text automatically.

```m
[Number = try Uri.BuildQueryString([page = 2]), Null = try Uri.BuildQueryString([page = null])]
```

```text
[Number = [HasError = true, Error = [Reason = "Expression.Error", Message = "We cannot convert the value 2 to type Text.", Detail = [Value = 2, Type = type text], #"Message.Format" = "We cannot convert the value #{0} to type #{1}.", #"Message.Parameters" = {"2", "Text"}, ErrorCode = "10277"]], Null = [HasError = true, Error = [Reason = "Expression.Error", Message = "We cannot convert the value null to type Text.", Detail = [Value = null, Type = type text], #"Message.Format" = "We cannot convert the value #{0} to type #{1}.", #"Message.Parameters" = {"null", "Text"}, ErrorCode = "10277"]]]
```

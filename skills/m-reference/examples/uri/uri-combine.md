<!-- lab: desktop 2.159.883.0 -->

# Uri.Combine

These examples show which parts of the base URI are kept, depending on slashes, dot segments, query strings and empty or null input.

```m
[
    NoTrailingSlash = Uri.Combine("https://example.com/api/v1", "items"),
    TrailingSlash = Uri.Combine("https://example.com/api/v1/", "items"),
    LeadingSlash = Uri.Combine("https://example.com/api/v1/", "/items")
]
```

```text
[NoTrailingSlash = "https://example.com/api/items", TrailingSlash = "https://example.com/api/v1/items", LeadingSlash = "https://example.com/items"]
```

```m
[
    ParentSegment = Uri.Combine("https://example.com/a/b/c", "../d"),
    QueryOnly = Uri.Combine("https://example.com/a/b?x=1", "?y=2"),
    AbsoluteRelative = Uri.Combine("https://example.com/a/", "https://other.org/z")
]
```

```text
[ParentSegment = "https://example.com/a/d", QueryOnly = "https://example.com/a/b?y=2", AbsoluteRelative = error: DataFormat.Error: A relative URI cannot be created because the 'uriString' parameter represents an absolute URI. | Detail: "https://other.org/z"]
```

```m
[
    EmptyRelative = Uri.Combine("https://example.com/a/b?x=1#frag", ""),
    NullRelative = try Uri.Combine("https://example.com/a/", null)
]
```

```text
[EmptyRelative = "https://example.com/a/b?x=1#frag", NullRelative = [HasError = true, Error = [Reason = "Expression.Error", Message = "We cannot convert the value null to type Text.", Detail = [Value = null, Type = type text], #"Message.Format" = "We cannot convert the value #{0} to type #{1}.", #"Message.Parameters" = {"null", "Text"}, ErrorCode = "10277"]]]
```

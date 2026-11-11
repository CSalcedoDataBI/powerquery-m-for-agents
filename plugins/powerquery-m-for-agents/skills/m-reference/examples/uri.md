<!-- lab: desktop 2.159.883.0 -->

# Executed examples: uri

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Uri.BuildQueryString

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

## Uri.Combine

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

## Uri.EscapeDataString

These examples show which characters are escaped, how non-ASCII text is encoded, and what happens with null.

A space becomes `%20`, not `+`. Reserved characters such as `+`, `&`, `=`, `/` and `?` are escaped too.

```m
Uri.EscapeDataString("a b+c&d=e/f?g")
```

```text
"a%20b%2Bc%26d%3De%2Ff%3Fg"
```

The unreserved characters `-`, `.`, `_` and `~` stay as they are. Non-ASCII characters are encoded as UTF-8 bytes.

```m
Uri.EscapeDataString("-._~ é ß €")
```

```text
"-._~%20%C3%A9%20%C3%9F%20%E2%82%AC"
```

The `data` parameter is not nullable: null raises an error rather than passing through.

```m
Uri.EscapeDataString(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Text. | Detail: [Value = null, Type = type text]
```

## Uri.Parts

These examples show the default port, a repeated query key, user info in the URI, and what happens with a relative URI.

```m
Uri.Parts("https://www.contoso.com/a%20b/page?x=1&x=2&y=#top")
```

```text
[Scheme = "https", Host = "www.contoso.com", Port = 443, Path = "/a%20b/page", Query = [x = "1,2", y = ""], Fragment = "top", UserName = "", Password = ""]
```

```m
Uri.Parts("http://user:p%40ss@contoso.com:8080/")
```

```text
[Scheme = "http", Host = "contoso.com", Port = 8080, Path = "/", Query = [], Fragment = "", UserName = "user", Password = "p%40ss"]
```

```m
try Uri.Parts("/relative/path?x=1")
```

```text
[HasError = true, Error = [Reason = "DataFormat.Error", Message = "Invalid URI: The hostname could not be parsed.", Detail = "/relative/path?x=1", #"Message.Format" = "Invalid URI: The hostname could not be parsed.", #"Message.Parameters" = null, ErrorCode = null]]
```

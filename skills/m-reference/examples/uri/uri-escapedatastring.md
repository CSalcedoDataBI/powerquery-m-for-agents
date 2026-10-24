<!-- lab: desktop 2.159.883.0 -->

# Uri.EscapeDataString

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

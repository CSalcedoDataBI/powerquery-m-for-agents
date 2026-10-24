<!-- lab: desktop 2.159.883.0 -->

# Uri.Parts

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

<!-- lab: desktop 2.157.879.0 -->

# Table.WithErrorContext

An error passed through it, caught with try.

```m
try Table.WithErrorContext(error "boom", "my context")
```

```text
[HasError = true, Error = [Reason = "Expression.Error", Message = "boom", Detail = null, #"Message.Format" = "boom", #"Message.Parameters" = null, ErrorCode = null]]
```

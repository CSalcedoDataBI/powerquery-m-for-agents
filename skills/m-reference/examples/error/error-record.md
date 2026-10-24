<!-- lab: desktop 2.159.883.0 -->

# Error.Record

Fields you leave out come back as null, and a raised record keeps its reason, message and detail.

```m
Error.Record("Validation")
```

```text
[Reason = "Validation", Message = "", Detail = null, #"Message.Format" = null, #"Message.Parameters" = null, ErrorCode = null]
```

```m
Error.Record("Validation", "Value #{0} is out of range", [Value = 42], {"42"}, "E042")
```

```text
[Reason = "Validation", Message = "Value 42 is out of range", Detail = [Value = 42], #"Message.Format" = "Value #{0} is out of range", #"Message.Parameters" = {"42"}, ErrorCode = "E042"]
```

```m
try error Error.Record("Validation", null, {1, 2, 3})
```

```text
[HasError = true, Error = [Reason = "Validation", Message = "", Detail = {1, 2, 3}, #"Message.Format" = null, #"Message.Parameters" = null, ErrorCode = null]]
```

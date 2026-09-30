<!-- lab: desktop 2.157.879.0 -->

# Number.FromText

The common text formats.

```m
{Number.FromText("15"), Number.FromText("3,423.10"), Number.FromText("5.0E-10")}
```

```text
{15, 3423.1, 5E-10}
```

Culture, and text that is not a number.

```m
{Number.FromText("3.423,10", "de-DE"), try Number.FromText("12 units")}
```

```text
{3423.1, [HasError = true, Error = [Reason = "DataFormat.Error", Message = "We couldn't convert to Number.", Detail = "12 units", #"Message.Format" = "We couldn't convert to Number.", #"Message.Parameters" = null, ErrorCode = "10041"]]}
```

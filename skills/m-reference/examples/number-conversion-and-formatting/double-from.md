<!-- lab: desktop 2.157.879.0 -->

# Double.From

Text, a date (days since 1899-12-30) and null.

```m
{Double.From("1e3"), Double.From(#date(1900, 1, 1)), Double.From(null)}
```

```text
{1000, 2, null}
```

Text that is not a number.

```m
try Double.From("abc")
```

```text
[HasError = true, Error = [Reason = "DataFormat.Error", Message = "We couldn't convert to Number.", Detail = "abc", #"Message.Format" = "We couldn't convert to Number.", #"Message.Parameters" = null, ErrorCode = "10041"]]
```

<!-- lab: desktop 2.159.883.0 -->

# Guid.From

Different GUID spellings convert to the same text, and null passes through.

```m
{
    Guid.From("05FE1DADC8C24F3BA4C2D194116B4967"),
    Guid.From("{05FE1DAD-C8C2-4F3B-A4C2-D194116B4967}"),
    Guid.From("05fe1dad-c8c2-4f3b-a4c2-d194116b4967")
}
```

```text
{"05fe1dad-c8c2-4f3b-a4c2-d194116b4967", "05fe1dad-c8c2-4f3b-a4c2-d194116b4967", "05fe1dad-c8c2-4f3b-a4c2-d194116b4967"}
```

```m
Guid.From(null)
```

```text
null
```

Text that is not a GUID raises an error. It does not return null.

```m
try Guid.From("not-a-guid")
```

```text
[HasError = true, Error = [Reason = "DataFormat.Error", Message = "We couldn't convert to a guid.", Detail = "not-a-guid", #"Message.Format" = "We couldn't convert to a guid.", #"Message.Parameters" = null, ErrorCode = "10016"]]
```

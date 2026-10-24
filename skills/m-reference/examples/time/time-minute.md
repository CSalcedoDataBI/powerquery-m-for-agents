<!-- lab: desktop 2.159.883.0 -->

# Time.Minute

The minute is read as written: seconds never round it up, a zone offset never shifts it, and null passes through.

```m
Time.Minute(#time(9, 59, 59.999))
```

```text
59
```

The minute comes from the local time, not from the UTC equivalent.

```m
Time.Minute(#datetimezone(2011, 12, 31, 9, 15, 36, 5, 30))
```

```text
15
```

```m
Time.Minute(null)
```

```text
null
```

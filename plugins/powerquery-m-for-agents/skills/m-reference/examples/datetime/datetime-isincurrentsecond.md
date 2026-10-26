<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInCurrentSecond

These examples show how the check treats null and fixed timestamps far from the present.

```m
DateTime.IsInCurrentSecond(null)
```

```text
null
```

```m
DateTime.IsInCurrentSecond(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInCurrentSecond(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

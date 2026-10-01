<!-- lab: desktop 2.157.879.0 -->

# DateTime.FromText

The examples show null input, the legacy text form of the options argument, and culture-sensitive parsing with an explicit format.

```m
DateTime.FromText(null)
```

```text
null
```

```m
DateTime.FromText("01/02/2010 03:04:05", "en-GB")
```

```text
#datetime(2010, 2, 1, 3, 4, 5)
```

```m
DateTime.FromText("30 Dez 2010 02:04:50.369730", [Format = "dd MMM yyyy HH:mm:ss.ffffff", Culture = "de-DE"])
```

```text
#datetime(2010, 12, 30, 2, 4, 50.36973)
```

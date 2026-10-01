<!-- lab: desktop 2.157.879.0 -->

# Type.AddTableKey

Adding a key returns a table type, and `Type.TableKeys` reads the key back.

```m
Type.TableKeys(Type.AddTableKey(type table [Id = number, Name = text], {"Id"}, true))
```

```text
{[Columns = {"Id"}, Primary = true]}
```

```m
Type.TableKeys(Type.AddTableKey(type table [Id = number, Name = text], {"Id"}, false))
```

```text
{[Columns = {"Id"}, Primary = false]}
```

```m
Type.TableKeys(Type.AddTableKey(type table [Region = text, Store = text, Sales = number], {"Region", "Store"}, true))
```

```text
{[Columns = {"Region", "Store"}, Primary = true]}
```

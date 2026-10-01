<!-- lab: desktop 2.157.879.0 -->

# Type.TableKeys

A table type with no keys returns an empty list, not null.

```m
Type.TableKeys(type table [ID = number, Name = text])
```

```text
{}
```

A table type can carry more than one key, and only one is marked primary.

```m
let
    Base = type table [ID = number, Email = text, Name = text],
    WithID = Type.AddTableKey(Base, {"ID"}, true),
    WithEmail = Type.AddTableKey(WithID, {"Email"}, false)
in
    Type.TableKeys(WithEmail)
```

```text
{[Columns = {"ID"}, Primary = true], [Columns = {"Email"}, Primary = false]}
```

A key can span several columns, so `Columns` is a list rather than a single name.

```m
Type.TableKeys(Type.AddTableKey(type table [Region = text, Store = number], {"Region", "Store"}, true))
```

```text
{[Columns = {"Region", "Store"}, Primary = true]}
```

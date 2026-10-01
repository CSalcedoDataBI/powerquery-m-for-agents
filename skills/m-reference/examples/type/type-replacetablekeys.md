<!-- lab: desktop 2.157.879.0 -->

# Type.ReplaceTableKeys

Replace, clear, and validate the keys declared on a table type.

```m
Type.TableKeys(Type.ReplaceTableKeys(type table [ID = number, FirstName = text, LastName = text], {[Columns = {"ID"}, Primary = true], [Columns = {"FirstName", "LastName"}, Primary = false]}))
```

```text
{[Columns = {"ID"}, Primary = true], [Columns = {"FirstName", "LastName"}, Primary = false]}
```

```m
Type.TableKeys(Type.ReplaceTableKeys(Type.AddTableKey(type table [ID = number, Name = text], {"ID"}, true), {}))
```

```text
{}
```

```m
Type.TableKeys(Type.ReplaceTableKeys(type table [ID = number], {[Columns = {"Missing"}, Primary = true]}))
```

```text
error: Expression.Error: The column 'Missing' of the table wasn't found. | Detail: "Missing"
```

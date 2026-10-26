<!-- lab: desktop 2.157.879.0 -->

# Splitter.SplitTextByCharacterTransition

These examples show which character transitions cause a split, using both list and predicate forms.

A split is made before each `after` character that directly follows a `before` character.

```m
Splitter.SplitTextByCharacterTransition({"A".."Z"}, {"a".."z"})("XMLHttpRequest")
```

```text
{"XMLH", "ttpR", "equest"}
```

Either argument can be a predicate function instead of a character list, and the two arguments are chosen independently.

```m
Splitter.SplitTextByCharacterTransition({"0".."9"}, each not List.Contains({"0".."9"}, _))("a1b2c")
```

```text
{"a1", "b2", "c"}
```

A null text gives an empty list, not null.

```m
Splitter.SplitTextByCharacterTransition({"a"}, {"b"})(null)
```

```text
{}
```

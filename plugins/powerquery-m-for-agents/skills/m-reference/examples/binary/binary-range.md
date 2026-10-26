<!-- lab: desktop 2.157.879.0 -->

# Binary.Range

The offset is zero-based, count is optional, and a null count runs to the end of the binary.

```m
Binary.Range(#binary({0..10}), 6)
```

```text
#binary({6, 7, 8, 9, 10})
```

```m
Binary.Range(#binary({0..10}), 6, null)
```

```text
#binary({6, 7, 8, 9, 10})
```

```m
Binary.Range(#binary({0..10}), 6, 0)
```

```text
#binary({})
```

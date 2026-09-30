# M concepts

The language itself, for questions no single function answers. `#shared` exports functions,
not the language, so these pages are written by hand. Each claim sits next to a block that was
run in the engine, with the value it returned right under it.

| Page | Read it for |
|---|---|
| [`concepts/let-in.md`](concepts/let-in.md) | Steps, their order, unused steps, quoted names, recursion with `@` |
| [`concepts/each-underscore.md`](concepts/each-underscore.md) | What `each` and `_` expand to, `[Field]` inside `each`, and the nested `each` that shadows `_` |
| [`concepts/records-lists-tables.md`](concepts/records-lists-tables.md) | Building and reading lists, records and tables; `?` access; row lookup; `&` |
| [`concepts/types-metadata.md`](concepts/types-metadata.md) | `is`, types as claims, `Int64.Type` versus `number`, `meta`, function types |
| [`concepts/errors-try-otherwise-catch.md`](concepts/errors-try-otherwise-catch.md) | `try`, `otherwise`, `catch`, raising errors, and errors that live in cells |
| [`concepts/lazy-evaluation-streaming.md`](concepts/lazy-evaluation-streaming.md) | What is evaluated when, buffering, and names evaluated once |

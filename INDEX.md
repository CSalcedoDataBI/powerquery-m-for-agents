# Skills — index and routing

Four skills, one idea: **the Power Query M language**. No modeling, no TMDL, no connector
development — there are better repos for those, linked from the [README](README.md).

---

## Routing

```
A question about Power Query M
  ├─ does this function exist? what does it take/return? which hosts?  → m-reference
  ├─ does this step fold? why is the refresh slow?                     → m-folding
  ├─ I am going to write my own function                               → m-custom-functions
  └─ loop / paginate / running total / buffer                          → m-iteration

Partitions, TMDL, incremental refresh policy? → not here. Use data-goblin's power-query skill.
```

## Catalogue

| Skill | Use it when | Status |
|---|---|---|
| **`m-reference`** | Language reference: whether a function exists, its signature and types, what it returns, which hosts have it. Cards generated from the engine's own `#shared`, plus field notes measured in the lab. | ✅ Desktop export · 🚧 more hosts, notes |
| **`m-folding`** | Whether a step folds to the source, what breaks it, how to verify, `Value.NativeQuery` with `EnableFolding`. | 🚧 stub |
| **`m-custom-functions`** | Typed and optional parameters, recursion, documenting your function with `Value.ReplaceType`. | 🚧 stub |
| **`m-iteration`** | `List.Generate`, `List.Accumulate`, buffering, pagination, `GroupKind.Local`. | 🚧 stub |

## Conventions

Same as [dax-for-agents](https://github.com/CSalcedoDataBI/dax-for-agents/blob/main/INDEX.md#conventions):

1. **One skill = one folder under `skills/`** with a `SKILL.md`. Supporting material in
   `scripts/`, `references/`, `evals/` inside that same folder.
2. **YAML frontmatter** with `name` (kebab-case, identical to the folder) and `description`
   (third person, starts with **"Use when …"**).
3. **Token-efficient:** `SKILL.md` is short; the detail lives in files read on demand.
4. **Cross-link by name** (`` `m-reference` ``), never by path.
5. **The `m-` prefix stays.** Installed, the skills are `m:m-reference`, `m:m-folding`,
   `m:m-custom-functions` and `m:m-iteration`.
6. **Every skill is listed by path in `.claude-plugin/plugin.json`**, checked by
   `scripts/check_plugin_manifest.py`.

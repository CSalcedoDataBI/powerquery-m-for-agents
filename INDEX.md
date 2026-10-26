# Skills — index and routing

Two skills today, three planned, one idea: **the Power Query M language**. No modeling, no TMDL, no connector
development — there are better repos for those, linked from the [README](README.md).

---

## Routing

```
A question about Power Query M
  ├─ does this function exist? what does it take/return? which hosts?  → m-reference
  ├─ does this step fold? why is the refresh slow?                     → m-folding (planned)
  ├─ I am going to write my own function                               → m-custom-functions (planned)
  ├─ loop / paginate / running total / buffer                          → m-iteration (planned)
  └─ the reference is wrong or misses a trap; report it                 → m-feedback

Partitions, TMDL, incremental refresh policy? → not here. Use data-goblin's power-query skill.
```

## Catalogue

| Skill | Use it when | Status |
|---|---|---|
| **`m-reference`** | Language reference: whether a function exists, its signature and types, what it returns, which hosts have it. Cards generated from the engine's own `#shared`, plus field notes measured in the lab. | ✅ Desktop export, concepts, Text/List/Table examples · 🚧 more hosts |
| **`m-feedback`** | m-reference proved wrong or incomplete while you worked in another project: drafts a sanitized issue for this public repo and files it only after the user approves the text. | ✅ |
| **`m-folding`** | Whether a step folds to the source, what breaks it, how to verify, `Value.NativeQuery` with `EnableFolding`. | 🚧 planned, in `planned/` |
| **`m-custom-functions`** | Typed and optional parameters, recursion, documenting your function with `Value.ReplaceType`. | 🚧 planned, in `planned/` |
| **`m-iteration`** | `List.Generate`, `List.Accumulate`, buffering, pagination, `GroupKind.Local`. | 🚧 planned, in `planned/` |

## Conventions

Same as [dax-for-agents](https://github.com/CSalcedoDataBI/dax-for-agents/blob/main/INDEX.md#conventions):

1. **One skill = one folder under `plugins/powerquery-m-for-agents/skills/`** with a
   `SKILL.md`. Only what the skill reads at run time goes there: maintainer scripts, tests and
   evals stay outside the plugin folder (`scripts/`, `lab/`, `evals/`), which is all that
   ships.
2. **YAML frontmatter** with `name` (kebab-case, identical to the folder) and `description`
   (third person, starts with **"Use when …"**).
3. **Token-efficient:** `SKILL.md` is short; the detail lives in files read on demand.
4. **Cross-link by name** (`` `m-reference` ``), never by path.
5. **The `m-` prefix stays.** The plugin is `powerquery-m-for-agents`, so installed the skill
   is `powerquery-m-for-agents:m-reference`; the planned ones will be
   `powerquery-m-for-agents:m-folding`, `powerquery-m-for-agents:m-custom-functions` and
   `powerquery-m-for-agents:m-iteration`.
6. **Every skill is listed by path in `plugins/powerquery-m-for-agents/.claude-plugin/plugin.json`**,
   checked by `scripts/check_plugin_manifest.py`.
7. **A skill ships only when it has content.** Claude Code loads every folder under `skills/`
   whatever `plugin.json` lists, so an outline waits in `planned/` and moves to `skills/`
   when it is ready.

# powerquery-m-for-agents

**The canonical Power Query M language reference for AI agents**: every library function
with its signature, types and the hosts that have it, plus the gotchas the documentation
doesn't tell you.

> **Status: early.** The catalogue is generated from one export, Power BI Desktop; its size
> and the build it came from are in the header of
> [`catalog.md`](skills/m-reference/generated/catalog.md), counted by the generator rather
> than typed here. Executed examples cover the Text, List and Table functions, and the language
> itself has hand-written concept pages. No second host or evals yet. Plan and open questions:
> [design spec](docs/superpowers/specs/2026-09-28-powerquery-m-for-agents-design.md).

Sibling of [dax-for-agents](https://github.com/CSalcedoDataBI/dax-for-agents), with the same
architecture: an agent reads one flat index, finds the function, and opens **one** card.

## What is different from DAX: the upstream is the engine

The DAX library was derived from `MicrosoftDocs/query-docs`, which has returned 404 since
2026-08. M does not need a documentation repo at all. `#shared` lists every function the
engine has loaded, and each one carries its documentation as metadata on its type:
description, category, examples, parameter types and return type.

So the catalogue is **exported, not scraped**:

- A function in the catalogue exists in the host it was exported from.
- Exporting several hosts (Desktop, Excel, Dataflows Gen2) and merging them gives every card
  a `hosts` field. No public document carries that.
- Regenerating means running one query in a new Desktop build.

## Skills

| Skill | For | Status |
|---|---|---|
| `m-reference` | Does it exist, what does it take and return, which hosts | ✅ Desktop export · 🚧 more hosts |
| `m-folding` | Does this step fold, what breaks it, how to verify | 🚧 stub |
| `m-custom-functions` | Writing and documenting your own functions | 🚧 stub |
| `m-iteration` | `List.Generate`, `List.Accumulate`, buffering, pagination | 🚧 stub |

Routing and conventions: [INDEX.md](INDEX.md).

## Install

```bash
/plugin marketplace add CSalcedoDataBI/powerquery-m-for-agents
/plugin install m@powerquery-m-for-agents
```

## Not here

- **Modeling, partitions, TMDL, incremental refresh policy**: the `power-query` skill in
  [data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development).
- **DAX**: [dax-for-agents](https://github.com/CSalcedoDataBI/dax-for-agents).

## Checking it yourself

```bash
pip install pyyaml
python scripts/validate_skills.py
python scripts/check_plugin_manifest.py
python scripts/check_workflow_cost.py
python -m unittest discover -s scripts -t scripts
python -m unittest discover -s skills/m-reference/scripts -t skills/m-reference/scripts
```

## License

MIT © CSalcedoDataBI. The licence of the function descriptions exported from `#shared` is
an open question, and the repository will not go public until it is answered (spec §9).

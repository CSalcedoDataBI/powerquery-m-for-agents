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

Planned, not shipped yet: `m-folding`, `m-custom-functions` and `m-iteration`. Their outlines
are in [`planned/`](planned/), outside `skills/`, so the plugin does not load them until
they have content.

Routing and conventions: [INDEX.md](INDEX.md).

## Install

```bash
/plugin marketplace add CSalcedoDataBI/powerquery-m-for-agents
/plugin install powerquery-m-for-agents@powerquery-m-for-agents
```

Needs Claude Code 2.1.142 or later: earlier versions install the plugin and load none of its
skills (`scripts/check_plugin_manifest.py`).

## What it runs, sends and downloads

**The plugin itself runs nothing.** It is one skill, `m-reference`, and nothing else: no hooks, no agents,
no MCP or LSP servers (`claude plugin details` lists that one skill and zero of each).
The skill is Markdown that Claude reads; installing or using it starts no process,
sends nothing anywhere and downloads nothing.

The repository also holds maintainer tools. None runs unless you run it:

| Tool | Runs | Sends | Downloads |
|---|---|---|---|
| `skills/m-reference/scripts/sync_shared.py` | Python, standard library only | Nothing | Nothing. Reads `exports/*.json` (in the git repository only, not in the plugin archive), writes `generated/` |
| `skills/m-reference/scripts/export_shared.pq` | M, pasted into your own Power BI or Excel | Nothing | Nothing. Reads `#shared` |
| `scripts/*.py` | Python checks, the same ones CI runs | Nothing | Nothing |
| `lab/runner/`, `lab/shared-export/` | Open Power BI Desktop on this machine; the runner evaluates the example blocks there, limited to functions that compute on values (`scripts/m_blocks.py`) | Nothing | Nothing |
| `lab/review/build_review.py` | Python; writes the review PBIPs, which you open yourself | Nothing | Nothing |
| `lab/drafting/pilot.py` (pilot) | Python; writes the prompts, and turns the answers `run_dsh.ps1` saved into example pages | Nothing | Nothing |
| `lab/drafting/run_dsh.ps1` (pilot, opt-in) | A Docker container with DeepSeek's `dsh` CLI | Each prompt to the DeepSeek API, with `DEEPSEEK_API_KEY` read from your Windows user environment | When the image is built: the `node:24-bookworm-slim` base image, and `@deepseek-ai/dsh` from npm at a pinned version |

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

MIT © CSalcedoDataBI. The one-line function and constant descriptions are Microsoft's,
from the MIT-licensed standard library of
[microsoft/vscode-powerquery](https://github.com/microsoft/vscode-powerquery): see
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The engine's own long descriptions and
examples carry no stated licence, so they are not copied (#1); each card links its Microsoft
Learn page instead, when that page exists.

# powerquery-m-for-agents

The Power Query M language reference for AI agents: every library function with its
signature, parameter and return types and the hosts that have it, exported from the engine's
own `#shared` rather than scraped from documentation, plus language concept pages, field notes
and examples executed in Power BI Desktop. A name the catalogue does not hold does not exist
in any exported host, so the agent can say so instead of inventing one.

Not modeling, partitions or TMDL.

## Skills

| Skill | For |
|---|---|
| `m-reference` | Does a function exist, what it takes and returns, which hosts have it, and the M language itself (`let`/`in`, `each _`, types, `try`/`otherwise`) |
| `m-feedback` | The reference proved wrong or incomplete: drafts a sanitized issue for the public repository and files it only after you approve the text |

## Install

```bash
/plugin marketplace add CSalcedoDataBI/powerquery-m-for-agents
/plugin install powerquery-m-for-agents@powerquery-m-for-agents
```

Needs Claude Code 2.1.142 or later.

## What this plugin runs, sends and fetches

Installed, the plugin is text: two skills, their Markdown reference pages and the catalogue
that indexes them. It ships no hooks, no agents, no MCP or LSP server, no telemetry and no
background process, and nothing it contains runs on its own.

| When | What happens | Where it goes |
|---|---|---|
| Any skill is used | Claude reads Markdown from the installed plugin folder | Nowhere: local reads only |
| You ask `m-feedback` to report a gap **and approve the drafted text** | Claude runs your own `gh issue create` with that text; without `gh` it hands you the text | A public issue on [CSalcedoDataBI/powerquery-m-for-agents](https://github.com/CSalcedoDataBI/powerquery-m-for-agents/issues), under your GitHub account |

The maintainer tools (the `#shared` export, the sync, the lab and the evals) live in
[the repository](https://github.com/CSalcedoDataBI/powerquery-m-for-agents), outside this
folder; they are not installed with the plugin.

Privacy policy: [PRIVACY.md](PRIVACY.md). License: [MIT](LICENSE). The one-line function
descriptions are Microsoft's, MIT: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

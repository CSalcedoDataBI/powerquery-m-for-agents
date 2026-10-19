# Privacy policy — powerquery-m-for-agents

*Effective 2026-10-02, updated 2026-10-19. Maintainer: Cristóbal Salcedo — contacto@csalcedodatabi.com*

This policy covers the **powerquery-m-for-agents** plugin for Claude. The website
[csalcedodatabi.com](https://csalcedodatabi.com) has [its own policy](https://csalcedodatabi.com/privacidad).

## What the plugin collects

**Nothing.** The plugin is text: two skills, `m-reference` (Markdown and JSON reference pages)
and `m-feedback` (instructions for reporting a gap in them). It ships no hooks, no agents, no
MCP or LSP server, no telemetry, no analytics and no background process. It has no server of
its own. The only thing that can reach the maintainer is a public GitHub issue you approve
and file through `m-feedback`, below.

## What it reads and sends

| When | What happens | Where it goes |
|---|---|---|
| A skill is used | Claude reads Markdown and JSON from the installed plugin folder | Nowhere: local reads only |
| You ask `m-feedback` to report a gap **and approve the drafted text** | Claude runs your own `gh issue create` with that text | A public issue on [github.com/CSalcedoDataBI/powerquery-m-for-agents](https://github.com/CSalcedoDataBI/powerquery-m-for-agents/issues), under your GitHub account and [GitHub's privacy statement](https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement) |

Your queries, models and conversations stay between you, Claude and the tools you already use.
The plugin keeps no copy of them and retains no data.

Maintainer scripts in this repository are **not** run by the plugin; they run only when a
maintainer starts them by hand. Three of them reach the network, as the README's table "What
it runs, sends and downloads" lists: `evals/hallucination/run_ab.py` sends benchmark questions
to the Anthropic or DeepSeek API and `lab/drafting/run_dsh.ps1` sends drafting prompts to the
DeepSeek API, each with the maintainer's own key read from the environment; and
`lab/shared-export/learn_links.py` sends one HEAD request per function to
`learn.microsoft.com`, to check which Microsoft Learn pages exist.

## Children

The plugin is a developer tool and is not directed at anyone under 18.

## Changes and contact

Changes to this policy are made in this file and recorded in the repository history.
Questions: contacto@csalcedodatabi.com.

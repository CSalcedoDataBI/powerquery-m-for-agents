# Privacy policy — powerquery-m-for-agents

*Effective 2026-10-02. Maintainer: Cristóbal Salcedo — contacto@csalcedodatabi.com*

This policy covers the **powerquery-m-for-agents** plugin for Claude. The website
[csalcedodatabi.com](https://csalcedodatabi.com) has [its own policy](https://csalcedodatabi.com/privacidad).

## What the plugin collects

**Nothing.** The plugin is text: one skill, `m-reference`, made of Markdown and JSON reference
pages. It ships no hooks, no agents, no MCP or LSP server, no telemetry, no analytics and no
background process. It has no server of its own, so nothing you do with it reaches the
maintainer.

## What it reads and sends

| When | What happens | Where it goes |
|---|---|---|
| The skill is used | Claude reads Markdown and JSON from the installed plugin folder | Nowhere: local reads only |

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

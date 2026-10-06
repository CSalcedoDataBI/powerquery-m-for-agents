# Contributing

Repository conventions (language, generated files, how counts are checked) are in
[INDEX.md](INDEX.md#conventions) and [CLAUDE.md](CLAUDE.md). Work lands on `main` through a pull
request; CI (`.github/workflows/validate-skills.yml`) must pass.

## Releases and the plugin directory

The claude.ai plugin directory tracks the **`stable`** branch, not `main`. It scans every
commit that lands on the branch it tracks and puts each one in review, replacing the one
before. `stable` moves only when a release is published, so `main` can take commits every day.
Claude Code users who install from this repo's marketplace still get `main`.

This repo has no release automation, so a release is three steps by hand:

1. Bump `version` in `.claude-plugin/plugin.json` on `main`, through a pull request.
2. Tag the merged commit and publish the release: `git tag -a vX.Y.Z <sha>`,
   `git push origin vX.Y.Z`, `gh release create vX.Y.Z --verify-tag`.
3. Move `stable` to it, fast-forward only: `git push origin vX.Y.Z^{commit}:refs/heads/stable`.
   If git refuses because it is not a fast-forward, stop: never force `stable`.

- **Batch the work.** A release is a review cycle measured in days, not a deploy.
- **Test before releasing**, in Claude Code against the local plugin
  (`claude --plugin-dir .`): what is on claude.ai is only ever what the reviewer approved.
- **Do not release while a version is in review**, unless it carries a security fix: it
  replaces the version the reviewer is reading.
- Never push to `stable` outside a release, and never force it.

---
name: pr-description
description: Generates a description of a PR
license: MIT
user-invocable: true
---

# PR description

This skill generates a Pull Request description of the current branch against the `origin/main` branch.

The skill generates:
- A title for the PR
- A description for the PR, in Mardown format for copy-pasting by the user.

The skill ignores:
- Trivial input (e.g. number of lines changed, added or deleted)
- Any file covered by `.gitignore`

---
name: pr-description
description: Generates a description of a PR
license: MIT
user-invocable: true
---

# PR description

Generate a Pull Request description of the current branch against the `origin/main` branch.

The output consists of:
- A title for the PR
- A description for the PR, in Mardown format for copy-pasting by the user.

The output ignores:
- Trivial input (e.g. number of lines changed, added or deleted)

The evaluation ignores:
- Any file covered by `.gitignore`

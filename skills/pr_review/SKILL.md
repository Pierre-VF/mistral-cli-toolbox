---
name: pr-review
description: Perform automated code reviews.
license: MIT
user-invocable: true
---

# PR review skill

Generate a Pull Request review of the current branch against the `origin/main` branch.

The evaluation ignores:
- Any file covered by `.gitignore`

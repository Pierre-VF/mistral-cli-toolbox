---
name: pr-review
description: Perform automated code reviews.
license: MIT
user-invocable: true
---

# PR review skill

This skill generates a Pull Request review of the current branch against the `origin/main` branch.

The skill ignores:
- Any file covered by `.gitignore`

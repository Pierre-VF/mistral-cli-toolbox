---
name: pr-review
description: Perform automated code reviews.
license: MIT
user-invocable: true
---

# PR review skill

Generate a Pull Request review of the current branch against the `origin/main` branch.

## Overall guidelines

The evaluation ignores:
- Any file covered by `.gitignore`

If there is no difference between branches, just say it and exit.


## Specific focus

Pay specific attention to the following:
- Typos
- Implementation of docstrings in public methods
- Logic gaps and edge-cases
- Maintainability of the code

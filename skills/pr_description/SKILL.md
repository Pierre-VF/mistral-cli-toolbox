---
name: pr-description
description: Use this skill when asked to generate a description for a pull request (PR). This will generate a title and description for the PR.
license: MIT
user-invocable: true
allowed-tools:
  - read_file
  - grep
  - ask_user_question
---

# PR description

Generate a Pull Request description of the current branch against the `origin/main` branch.

The output consists of:
- A title for the PR
- A description for the PR, in Markdown format for copy-pasting by the user. The base title level should be 2 (i.e. `##`)

The output should not contain:
- Trivial input (e.g. number of lines changed, added or deleted)

## Evaluation

The evaluation ignores:
- Any file covered by `.gitignore`
- Large data files (JSON, CSV, ...) - instead just mention a change in the file with the number of lines changed.

If there is no difference between branches, just say it and exit.

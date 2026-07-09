---
name: pr-review-security
description: Use this skill when asked to review a pull request with strong emphasis on security. Reviews the diff between the current branch and origin/main, flagging vulnerabilities, insecure patterns, and compliance issues alongside standard code quality concerns.
license: MIT
user-invocable: true
---

# PR Review Skill (Security-Focused)

Generate a Pull Request review of the current branch against `origin/main`, with security as the primary lens while still covering correctness, maintainability, and style.

## Overall guidelines

The evaluation ignores:
- Any file covered by `.gitignore`
- Large data files (JSON, CSV, binary blobs, generated assets)
- Auto-generated code or vendor dependencies unless they are directly invoked in new logic

If there is no diff between branches, state that and exit.

## Review workflow

1. **Understand scope** — read the PR description, commit messages, and any linked issues to grasp intent before inspecting diffs.
2. **Security sweep first** — scan every changed file for vulnerability patterns (see Security checklist below). Flag anything critical or high immediately; do not wait until a final pass.
3. **Correctness & logic** — verify the implementation matches requirements, handles edge cases, and does not introduce regressions in existing behavior.
4. **Maintainability & style** — check naming consistency, docstrings on public APIs, code organization, and adherence to project conventions.
5. **Summarize findings** — present results grouped by severity (Critical / High / Medium / Low) with file paths, line references, actionable remediation advice, and a brief rationale for each finding.

## Security checklist

### Injection & input handling
- SQL injection: string concatenation or f-string interpolation in raw queries; prefer parameterized queries or an ORM that escapes automatically.
- Command injection: unsanitized user data passed to `subprocess`, `os.system()`, shell=True, backticks, eval(), exec().
- Template / XSS injection: unescaped output rendered into HTML templates or client-side contexts.
- Path traversal: file paths constructed from user input without canonicalization and prefix validation (e.g., realpath checks).

### Authentication & authorization
- Bypassable auth guards — routes or functions that skip authentication/authorization in new code or tests.
- Privilege escalation vectors — missing role/group checks on write, delete, admin endpoints; IDOR patterns where resource ownership is not verified server-side.
- Session / token handling: tokens stored insecurely (plain text logs, client-side storage without HttpOnly/Secure flags), weak signing algorithms, expired or revoked tokens still accepted.

### Secrets & credentials
- Hardcoded API keys, passwords, private keys, connection strings in source code — flag any literal secrets found in diffs.
- Credentials committed to version control history (even if removed now); recommend secret scanning tools and .gitignore rules.
- Sensitive data logged or exposed in error messages / stack traces.

### Cryptography & hashing
- Weak algorithms: MD5, SHA1 for integrity; DES/RC4 for encryption; ECB mode. Prefer AES-GCM, ChaCha20-Poly1305, bcrypt/scrypt/Argon2id for passwords.
- Improper key management — keys hardcoded, derived from weak entropy sources (e.g., time-based seeds), or shared across environments without rotation support.

### Data handling & privacy
- PII / sensitive data stored in plaintext logs, caches, databases, or error responses; missing masking/redaction.
- Missing input validation on deserialization endpoints — unsafe YAML/JSON/XML parsing that could lead to object injection (e.g., Python `yaml.load` without SafeLoader).

### Dependencies & supply chain
- New dependencies added with known CVEs or unmaintained status; check version pins and lock files for consistency.
- Transitive dependency risks in newly introduced packages — flag if the PR adds a package that pulls in risky transitive deps (e.g., build tools, network clients).

### API & networking
- Insecure transport: HTTP instead of HTTPS for sensitive endpoints or credentials; missing TLS verification bypasses (`verify=False`, `rejectUnauthorized: false`).
- CORS misconfigurations — overly permissive origins, methods, or headers in new middleware.
- Rate limiting / DoS exposure on newly added public-facing routes or bulk operations without throttling.

### Error handling & information disclosure
- Stack traces, internal paths, database schemas, or query plans exposed to clients via error responses.
- Generic success messages that leak existence of resources (e.g., "User not found" vs. "Invalid credentials").

## Specific focus areas

Beyond security, pay attention to:
- Typos and misleading variable/function names
- Docstrings on public methods — are they accurate for the new code?
- Logic gaps, race conditions, off-by-one errors, unhandled exceptions
- Maintainability of the code (DRY principle, single responsibility)
- Test coverage for changed logic — do existing tests still pass and should new ones be added?

## Output format

Structure your review as follows:

```markdown
# PR Review Summary

**Branch:** `<branch>` → `origin/main`
**Files reviewed:** N files (N hunks)

---

## Critical / High severity findings

| # | File | Line(s) | Issue | Severity | Recommendation |
|---|------|---------|-------|----------|----------------|
| 1 | path/to/file.py:42 | SQL injection via f-string in query construction. Use parameterized queries with `?` or `%s`. |

## Medium / Low severity findings

| # | File | Line(s) | Issue | Severity | Recommendation |
|---|------|---------|-------|----------|----------------|

## General feedback (non-security, non-critical)

- Bullet points for style, naming, docstring gaps, maintainability notes.

## Overall assessment

[One or two sentences: approve with comments, request changes, or informational.]
```

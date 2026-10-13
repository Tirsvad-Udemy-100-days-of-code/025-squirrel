# RC Review of ci.yml against the YAML checklist

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [WF-MIL-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [d71b586] |

---

## Artifact Under Review

- Instance reviewed: [WF-MIL-001]
- Checklist used: [QC-YML-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping (Mandatory) | Pass | Parsed by yamllint (PyYAML based); no duplicate keys. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces (Mandatory) | Pass | 2 spaces, LF, single trailing newline. |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments (Mandatory) | Pass | `yamllint` with `.yamllint.yml` committed: no errors. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` (Mandatory) | Pass | Values quoted: "3.13", "26.2.1". |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it (Mandatory) | Pass | No tags or extensions. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool (Mandatory) | Pass | No secret in the file. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it (Mandatory) | Pass | The longest `run:` block has 3 lines. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) (Mandatory) | Pass | No repeated block. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them (Mandatory) | Pass | No anchors used. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated (Optional) | Pass | `actionlint 1.7.12` validates the workflow schema. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded (Mandatory) | Pass | Header comment states purpose, reader, side effects and decision. |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) (Mandatory) | Pass | Keys are kebab-case as Gitea Actions expects; env names UPPER_SNAKE. |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters (Optional) | Pass | Block scalar `|` used for the 3-line script; trailing newline is not significant. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository (Optional) | Pass | `ci.yml` is lowercase; `.yml` is the only extension used. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool (Optional) | Pass | yamllint and actionlint run without the real target. |

## Overall Verdict

Go — all Mandatory criteria pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[WF-MIL-001]: ../../../.gitea/workflows/ci.yml
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[d71b586]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/d71b5863eba3dc29c5a5e09e4ffa087c67565fae

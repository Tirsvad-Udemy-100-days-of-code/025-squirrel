# RC Review of ci.yml, delta re-review for the lint steps (YAML)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-031 |
| CrossReference | [WF-MIL-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [WF-MIL-001]
- Checklist used: [QC-YML-001]
- Scope: delta re-review of criteria 3, 7, 10 and 15 of QC-YML-001: two lint steps added to ci.yml; earlier record RC-009
- Language and domain: n/a
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments (Mandatory) | Pass | `yamllint 1.38.0` with `.yamllint.yml` runs in CI on `.gitea` and `.yamllint.yml`; no errors. `new-lines` is disabled with a comment because git normalises line endings. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it (Mandatory) | Pass | The two new `run:` blocks have one line each; the longest block is still 3 lines. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated (Optional) | Pass | `actionlint` validates the workflow schema in CI. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool (Optional) | Pass | yamllint and actionlint now run on every push and pull request without the real target. |

## Overall Verdict

Go — the changed rows pass; the other rows of RC-009 still hold.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[WF-MIL-001]: ../../../.gitea/workflows/ci.yml
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md

# RC Review of ci.yml, delta re-review for the lint steps (workflow)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-032 |
| CrossReference | [WF-MIL-001], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [WF-MIL-001]
- Checklist used: [QC-WF-001]
- Scope: delta re-review of criteria 5, 6, 17, 20, 22 and 24 of QC-WF-001: two lint steps added; earlier records RC-010, RC-025, RC-030
- Language and domain: n/a
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 5 | Every job and step has a descriptive `name`, unique within its job (Mandatory) | Pass | The new steps are named "Lint the YAML files" and "Lint the workflow files"; step names stay unique. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated (Mandatory) | Pass | `actionlint 1.7.12` runs in CI against `.gitea/workflows/*.yml` and passes. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place (Mandatory) | Pass | `yamllint==1.38.0` and `actionlint-py==1.7.12.25` are exact pins in the dev extra of `pyproject.toml`. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` (Mandatory) | Pass | Each new `run:` block is one line. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header (Mandatory) | Pass | The changed workflow completed with success on Gitea 1.27.3: run 1087 on pull request #39. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit (Optional) | Pass | `tests/test_workflow.py` still passes (33 tests) with the new steps. |

## Overall Verdict

Go — the changed rows pass; the other rows of RC-010, RC-025 and RC-030 still hold.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[WF-MIL-001]: ../../../.gitea/workflows/ci.yml
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md

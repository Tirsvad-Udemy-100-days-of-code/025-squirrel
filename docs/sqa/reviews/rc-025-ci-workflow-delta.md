# RC Review of ci.yml, delta re-review of criterion 22

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-025 |
| CrossReference | [WF-MIL-001], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [WF-MIL-001]
- Checklist used: [QC-WF-001]
- Scope: delta re-review of criterion 22 of QC-WF-001; reason: the condition of RC-010 (run 1012 queued); earlier record RC-010
- Language and domain: n/a
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header (Mandatory) | Pass | Gitea 1.27.3, runner labels ubuntu-latest. `ci.yml` completed with success on the instance: pull_request runs 1037, 1040 and 1043, and the push run 1044 on main (commit c4e88c6). Header states the host and that only github.* contexts are used. |

## Overall Verdict

Go — criterion 22, the only open Mandatory criterion of RC-010, now passes; the other rows of RC-010 still hold, so the workflow is Go. Closes the condition of RC-010.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[WF-MIL-001]: ../../../.gitea/workflows/ci.yml
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md

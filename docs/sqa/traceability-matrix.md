# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001]

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f1b3c03] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | - (no checklist; accepted by S01 in chat) |
| [MIL-001] | Milestone | en | it | [BC-001], [PP-001] | - | [RC-003] |
| [MIL-002] | Milestone | en | it | [BC-001], [PP-001], [MIL-001] | - | [RC-004] |
| [MIL-003] | Milestone | en | it | [BC-001], [PP-001], [MIL-002] | - | [RC-005] |
| [MIL-004] | Milestone | en | it | [BC-001], [PP-001], [MIL-003] | - | [RC-006] |
| [DICT-001] | Domain Dictionary | en | it | [BC-001], [SA-001] | - | [RC-007] |

## Coverage Notes

- `-` in Upstream means foundational; in Downstream, nothing is built on it yet; in Last Reviewed, no `RC-*` exists yet.
- No instance yet of US, UC, SSD, DM, ADR or source code; they are added in MIL-002.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-scaffold.md
[MIL-002]: ../milestones/mil-002-census-analysis.md
[MIL-003]: ../milestones/mil-003-documentation.md
[MIL-004]: ../milestones/mil-004-wiki-publication.md
[DICT-001]: ../dictionary.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001-project-scaffold.md
[RC-004]: ./reviews/rc-004-mil-002-census-analysis.md
[RC-005]: ./reviews/rc-005-mil-003-documentation.md
[RC-006]: ./reviews/rc-006-mil-004-wiki-publication.md
[RC-007]: ./reviews/rc-007-dictionary.md
[f1b3c03]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/f1b3c034dc3880b7884646b4a4ed28e5f98fbcd3

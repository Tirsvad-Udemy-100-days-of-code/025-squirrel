# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001]

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f1b3c03] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Rows added for UCD-001, US-001, UC-001, SSD-001, DM-001, DM-002, ADR-0001 and the source files; Last Reviewed updated up to RC-030<br>Version History rows added for edits made since the first version (the git history holds each edit) | [dfaa840] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-001], [RC-019], [RC-026] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | - (no checklist; accepted by S01 in chat) |
| [MIL-001] | Milestone | en | it | [BC-001], [PP-001] | - | [RC-003], [RC-020], [RC-028], [RC-033] |
| [MIL-002] | Milestone | en | it | [BC-001], [PP-001], [MIL-001] | - | [RC-004], [RC-021] |
| [MIL-003] | Milestone | en | it | [BC-001], [PP-001], [MIL-002] | - | [RC-005], [RC-022] |
| [MIL-004] | Milestone | en | it | [BC-001], [PP-001], [MIL-003] | - | [RC-006], [RC-023], [RC-027] |
| [DICT-001] | Domain Dictionary | en | it | [BC-001], [SA-001] | - | [RC-007], [RC-018] |
| [UCD-001] | Use Case Diagram | en | it | [SA-001], [BC-001] | [US-001], [UC-001] | [RC-011] |
| [US-001] | User Story | en | it | [UCD-001], [BC-001], [MIL-002] | [UC-001] | [RC-012] |
| [UC-001] | Use Case | en | it | [UCD-001], [US-001], [SA-001] | [SSD-001], [DM-001] | [RC-013] |
| [SSD-001] | System Sequence Diagram | en | it | [UC-001] | - | [RC-014] |
| [DM-001] | Domain Model | en | it | [UC-001], [DICT-001] | [DM-002] | [RC-015] |
| [DM-002] | Domain Model | en | it | [DM-001], [DICT-001] | - | [RC-016] |
| [ADR-0001] | Architecture Decision Record | - | - | [BC-001], [SA-001], [MIL-002] | `src/squirrel/census.py` | [RC-017] |
| `src/squirrel/census.py`, `cli.py`, `__main__.py`, `tests/` | Python Source Code | - | - | [UC-001], [SSD-001], [ADR-0001] | - | [RC-024] |
| `src/squirrel/constants.py`, `tests/test_constants.py` | Python Source Code | - | - | [MIL-001] | - | [RC-008] |
| `tests/test_workflow.py` | Python Source Code | - | - | [MIL-001], [RC-010] | - | [RC-029] |
| `.gitea/workflows/ci.yml` | CI Workflow | - | - | [MIL-001] | - | [RC-009], [RC-010], [RC-025], [RC-030], [RC-031], [RC-032] |

## Coverage Notes

- `-` in Upstream means foundational; in Downstream, nothing is built on it yet; in Last Reviewed, no `RC-*` exists yet.
- No instance of OC, SD, DCD, ERD or KPI; the project creates none (see RC-018).

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
[RC-008]: ./reviews/rc-008-python-constants.md
[RC-009]: ./reviews/rc-009-ci-workflow-yaml.md
[RC-010]: ./reviews/rc-010-ci-workflow.md
[f1b3c03]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/f1b3c034dc3880b7884646b4a4ed28e5f98fbcd3
[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[UC-001]: ../uc-001/uc.md
[SSD-001]: ../uc-001/ssd.md
[DM-001]: ../uc-001/dm.md
[DM-002]: ../domain-model.md
[ADR-0001]: ../adr/adr-0001-standard-library-instead-of-pandas.md
[RC-011]: ./reviews/rc-011-use-case-diagram.md
[RC-012]: ./reviews/rc-012-user-stories.md
[RC-013]: ./reviews/rc-013-use-case.md
[RC-014]: ./reviews/rc-014-ssd.md
[RC-015]: ./reviews/rc-015-dm-use-case.md
[RC-016]: ./reviews/rc-016-dm-project.md
[RC-017]: ./reviews/rc-017-adr-0001.md
[RC-018]: ./reviews/rc-018-dictionary-2.md
[RC-019]: ./reviews/rc-019-business-case-delta.md
[RC-020]: ./reviews/rc-020-mil-001-delta.md
[RC-021]: ./reviews/rc-021-mil-002-delta.md
[RC-022]: ./reviews/rc-022-mil-003-delta.md
[RC-023]: ./reviews/rc-023-mil-004-delta.md
[RC-024]: ./reviews/rc-024-python-census.md
[RC-025]: ./reviews/rc-025-ci-workflow-delta.md
[RC-026]: ./reviews/rc-026-business-case-wiki-path.md
[RC-027]: ./reviews/rc-027-mil-004-wiki-path.md
[RC-028]: ./reviews/rc-028-mil-001-task-7.md
[RC-029]: ./reviews/rc-029-python-workflow-test.md
[RC-030]: ./reviews/rc-030-ci-workflow-delta-24.md
[dfaa840]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/dfaa8400c3bd24b086a2c3eab1bef1e4e7ea6b45
[RC-031]: ./reviews/rc-031-ci-yaml-lint-steps.md
[RC-032]: ./reviews/rc-032-ci-workflow-lint-steps.md
[RC-033]: ./reviews/rc-033-mil-001-task-8.md

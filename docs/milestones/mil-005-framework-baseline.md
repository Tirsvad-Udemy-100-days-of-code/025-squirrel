# MIL-005 Framework baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [PP-001], [MIL-004] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | [6a931f9] |

---

## Purpose

This gate decides whether Squirrel Census has the baseline of the framework: the adopted framework release, the wiki in English, Danish and Malay in the framework's location and page naming, the README in the framework template, complete licence metadata and reviewed documents, merged to the default branch with a green build. The work is delivered on the branch `mil-005-baseline` and one pull request.

## Deliverable

A merged pull request that holds: the updated Business Case, Stakeholder Analysis, Project Plan, dictionary, milestones MIL-001 to MIL-004 and Traceability Matrix with their review records; the wiki in English, Danish and Malay in `docs/wiki/`; the README in the framework template; `pyproject.toml` with complete licence metadata; and the framework release adopted by the project. The program and its tests do not change.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, SA-001, PP-001, DICT-001, MIL-001 to MIL-004 and MIL-005 each have an `Accepted` Version History row and a review record with the verdict `Go` | All of them | Any missing or `Go-with-conditions` |
| 2 | `python -m pytest` runs | Exit code 0 | Any failure |
| 3 | `docs/wiki/` has `_Sidebar.md` and the pages Home, Install, Usage, Description and Project-Documents in en, da and ms | 15 pages and the sidebar | A page or language missing |
| 4 | `framework/scripts/check-readme.sh` and `framework/scripts/check-languages.sh` run | Exit code 0 | Any finding |
| 5 | `pyproject.toml` sets `license`, `license-files` and the project URLs for the documentation and the issue tracker | All set | Any missing |
| 6 | All CI (continuous integration) checks of the pull request | Green | Red or pending |
| 7 | The pull request carries one `Closes #N` line per task of this milestone | Every issue is closed after the merge | An issue stays open |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] accepted | Documents and baselines the finished program and its wiki |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 4 | Criterion 2 (the behaviour is unchanged and its tests pass) |
| Objectives 5 and 6 | Criteria 1, 3, 4, 5 and 7 (documents, wiki, README, licence and issues) |
| Success criterion 6 | Criteria 1 and 6 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-22: one week after the start, as the Business Case assumption requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Track the `framework/` submodule and `.gitmodules`, install the skills, hooks and `.editorconfig`, and track `.env.example`, so the project follows the same rules as the other projects of the portfolio. | No | Objective 6 |
| 2 | Update and review the planning documents | Add this milestone to the Business Case and Project Plan, add concern IDs to the Stakeholder Analysis, set the domain of the dictionary and the earlier milestones, extend the traceability matrix and review each changed document against its QC checklist, so the plan-first gate is met. | No | Objective 6 |
| 3 | Move the wiki to docs/wiki and complete it | Move the existing pages from `wiki/` to `docs/wiki/`, where the framework publishes them, name the Danish and Malay pages `-da` and `-ms`, write the sidebar in the framework shape and add the Project-Documents page in English, Danish and Malay. | No | Objective 6 |
| 4 | Restore the README to the framework template | Bring the original text of the README into the template's sections and the document appendix, with the project links, so the README is complete and checkable. | No | Objective 6 |
| 5 | Complete the licence metadata | Set the authors and the project URLs next to the existing licence expression and `license-files` in `pyproject.toml`, so package tools can read them. | No | Objective 6 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-004]: ./mil-004-wiki-publication.md
[6a931f9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/6a931f9675858d8031a88c3db7f14fb07468d68e

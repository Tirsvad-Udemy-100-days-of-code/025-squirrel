# MIL-004 Wiki and publication

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f1b3c03] |

---

## Purpose

Decide whether the repository is published with a wiki in English, Danish and Bahasa Malaysia and whether the final repository metadata is correct.

## Deliverable

Wiki pages `Home`, `Install`, `Usage` and `Description` in English plus `-da` and `-ms` variants following the framework wiki layout, with screenshots, pushed to the wiki of the repository, and a final verification of description and topics.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Each wiki page exists in English, Danish (`-da`) and Bahasa Malaysia (`-ms`) | All present | Any missing |
| 2 | The sidebar links every page in all three languages | All linked | Missing link |
| 3 | Wiki pages are on the git host wiki, or kept under `docs/wiki/` with the failure reported | Published or reported | Neither |
| 4 | Screenshots appear on the wiki pages | Present | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The wiki reuses README content and screenshots |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5, Success Criteria 4 and 5 | [BC-001] |
| S02 and S03 communication needs | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-16 — same day as MIL-003

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write English wiki pages | Create `Home`, `Install`, `Usage` and `Description` pages and a `_Sidebar`, after the structure of the framework wiki and the TirSystem github-action wiki example. | No |  |
| 2 | Write Danish wiki pages | Translate the English pages into Danish with the `-da` suffix and a language switch in the sidebar. | No |  |
| 3 | Write Bahasa Malaysia wiki pages | Translate the English pages into Bahasa Malaysia with the `-ms` suffix and a language switch in the sidebar. | No |  |
| 4 | Add screenshots to the wiki | Add the images from `docs/images/` to the pages of all three languages. | No |  |
| 5 | Publish the wiki and verify metadata | Push the pages to the repository wiki with the token from `.env` and read back the repository description and topics from the API. | No |  |

---

[BC-001]: ../business-case.md
[f1b3c03]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/f1b3c034dc3880b7884646b4a4ed28e5f98fbcd3

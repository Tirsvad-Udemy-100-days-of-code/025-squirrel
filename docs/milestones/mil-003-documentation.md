# MIL-003 README, source documentation and screenshots

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f1b3c03] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | CrossReference: added [US-001] | pending |
---

## Purpose

Decide whether a newcomer (S02, S03) can set up, run, test and understand the project from the README and the generated source documentation alone.

## Deliverable

A branch merged to `main` containing `README.md` with the requested sections, Doxygen comments in the source that build cleanly, and screenshots stored under `docs/images/` and used in the README.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README contains the sections Requirements, Set up (Windows PowerShell, Linux Debian, MacOS), Run, Run the tests, Continuous integration, Build the source documentation, Project layout, License | All present | Any missing |
| 2 | README documents creating a `.venv` and `python -m pip install --upgrade pip` | Present | Missing |
| 3 | `doxygen Doxyfile` completes with no warnings (when Doxygen is installed) | No warnings | Warnings |
| 4 | README shows at least one screenshot of the real program output | Present | Missing |
| 5 | Commands in the README were executed in a fresh `.venv` in this session | Verified | Not run |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The README documents a working program |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3 and 4, Success Criterion 4 | [BC-001] |
| S02 and S03 concerns on README | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-16 — one day after MIL-002

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add Doxygen comments to the source | Document every module, function and constant with Doxygen comment blocks (`##` and `@param`/`@return`) so the Doxyfile produces useful output. | No |  |
| 2 | Write README.md | Write the README from the framework template using the section list required by the Product Owner, including the venv and pip upgrade instructions for Windows PowerShell, Linux Debian and MacOS. | No |  |
| 3 | Create screenshots | Render images of the real command output (program run and test run) as Portable Network Graphics (PNG) files under `docs/images/`, and reference them from the README and later the wiki. | No |  |
| 4 | Verify the README commands | Follow the README in a fresh `.venv` and record the result in the review record, so the instructions are known to work. | No |  |

---

[BC-001]: ../business-case.md
[f1b3c03]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/f1b3c034dc3880b7884646b4a4ed28e5f98fbcd3
[US-001]: ../user-stories.md

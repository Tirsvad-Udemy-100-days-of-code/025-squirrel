# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f1b3c03] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added concern IDs CN-001 to CN-006 (QC-SA-001 criterion 9), the baseline concern CN-007, the baseline milestone in the communication table and a conflict about the stand-in reviewer; set the domain to education; reviewed in autonomous mode, not independent | [6a931f9] |

---

## Purpose

This analysis names the people who use or judge the squirrel census project and fixes the stakeholder IDs that every other artifact cites for ownership, review and RACI. It classifies each stakeholder by the power/interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad (personal) | HIGH | HIGH | Manage Closely | A correct, reviewed solution to the day 25 assignment that can be shown as a portfolio piece |
| S02 | Udemy coursists | Fellow participants of the 100 Days of Code course | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews every artifact and accepts every milestone; no other stakeholder can block the project.
- **Keep Informed (S02, S03):** they cannot change the scope, but their needs shape the deliverables: S02 sets the code readability and run instructions, S03 sets the repository presentation. Their interest is high (S02) or medium (S03) because they choose whether to reuse the repository.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute (functionality, usability, reliability, performance, supportability) |
| --- | --- | --- | --- |
| CN-001 | S01 | Counts match the census file and the assignment | Functionality |
| CN-002 | S01 | Work is reviewed and traceable through branches and pull requests | Supportability |
| CN-003 | S02 | Code is readable and uses the assignment's function names | Usability |
| CN-004 | S02 | README states how to set up and run the project and its tests | Usability |
| CN-005 | S03 | Repository has a description, topics and README | Usability |
| CN-006 | S03 | No runtime dependencies to install | Implementation (+) |
| CN-007 | S01 | The project follows the common baseline of the framework, with the wiki in the framework's location | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Plan, review records, run summary | All milestones |
| S02 | README and wiki | On release of each milestone | Run instructions in three languages | MIL-003, MIL-004 |
| S03 | Repository description, topics, README | Once, then on change | Repository metadata and README | MIL-001, MIL-003 |
| S01 | Pull request on the git host and end-of-run summary in chat | Once, for the baseline milestone | Documents, wiki and review records to read, and the stand-in decisions | [MIL-005] |
| S02, S03 | Wiki in English, Danish and Malay | Once, updated on change | Wiki pages | [MIL-005] |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01's course lecture uses Pandas, S03 expects no runtime dependencies | S01, S03 | Implement with the standard library and name functions after the lecture steps; record the decision in an architecture decision record (ADR) |
| S02 wants the assignment's function names, S01 wants professional structure | S01, S02 | Keep the lecture's step names as public functions inside a structured package |
| The documents of the baseline milestone are accepted by an AI stand-in for S01, so that review is not independent | S01 | S01 authorised the stand-in for the baseline milestone only; every review record says `Mode: autonomous, not independent`, and the end-of-run summary lists each stand-in decision so that S01 can challenge it |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct counts, reviewed work (CN-001, CN-002) | [BC-001] Objectives 1 and 2 |
| S02 | Runnable code and instructions (CN-003, CN-004) | [BC-001] Objectives 1 and 3 |
| S03 | Description, topics, no dependencies (CN-005, CN-006) | [BC-001] Objective 5 and Success Criterion 3 |
| S01 | The project follows the common baseline of the framework (CN-007) | [BC-001] Objective 6 and Success Criterion 6 |

## Sign-Off

| Stakeholder | Role in sign-off | Status |
| --- | --- | --- |
| S01 | Product Owner and reviewer | Proposed |

The changes of the baseline milestone were accepted by the AI stand-in for S01 after the review record of this document (Go), autonomous, not independent.

---

[BC-001]: ./business-case.md
[f1b3c03]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/f1b3c034dc3880b7884646b4a4ed28e5f98fbcd3
[MIL-005]: ./milestones/mil-005-framework-baseline.md
[6a931f9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/6a931f9675858d8031a88c3db7f14fb07468d68e

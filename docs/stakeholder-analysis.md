# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

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

| ID | Concern | FURPS+ attribute (functionality, usability, reliability, performance, supportability) |
| --- | --- | --- |
| S01 | Counts match the census file and the assignment | Functionality |
| S01 | Work is reviewed and traceable through branches and pull requests | Supportability |
| S02 | Code is readable and uses the assignment's function names | Usability |
| S02 | README states how to set up and run the project and its tests | Usability |
| S03 | Repository has a description, topics and README | Usability |
| S03 | No runtime dependencies to install | Implementation (+) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Plan, review records, run summary | All milestones |
| S02 | README and wiki | On release of each milestone | Run instructions in three languages | MIL-003, MIL-004 |
| S03 | Repository description, topics, README | Once, then on change | Repository metadata and README | MIL-001, MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01's course lecture uses Pandas, S03 expects no runtime dependencies | S01, S03 | Implement with the standard library and name functions after the lecture steps; record the decision in an architecture decision record (ADR) |
| S02 wants the assignment's function names, S01 wants professional structure | S01, S02 | Keep the lecture's step names as public functions inside a structured package |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct counts, reviewed work | [BC-001] Objectives 1 and 2 |
| S02 | Runnable code and instructions | [BC-001] Objectives 1 and 3 |
| S03 | Description, topics, no dependencies | [BC-001] Objective 5 and Success Criterion 3 |

## Sign-Off

| Stakeholder | Role in sign-off | Status |
| --- | --- | --- |
| S01 | Product Owner and reviewer | Proposed |

---

[BC-001]: ./business-case.md

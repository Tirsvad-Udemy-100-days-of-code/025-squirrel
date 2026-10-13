# User Story

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [UCD-001], [BC-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose and Scope

Covers the epic delivered by [MIL-002]: the participant counts squirrels by fur colour. Objective 1 of [BC-001].

## Story List

### US-001.01 — Count squirrels by fur colour

**As a** Participant, **I want** to count the squirrels of each fur colour in the census file, **so that** I get a summary file with the number of gray, cinnamon and black squirrels.

**Acceptance Criteria**

- Given a census file with squirrel sightings, when the participant counts by fur colour, then the summary lists Gray, Cinnamon and Black with the number of sightings of each.
- Given the 2018 census file, when the participant counts by fur colour, then the summary shows Gray 2473, Cinnamon 392 and Black 103.
- Given a census file with a sighting that has no fur colour, when the participant counts, then that sighting is in no colour count.
- Given a census file that does not exist, when the participant counts, then the participant is told that the file is missing and no summary is written.

| Traces to | Size | INVEST exceptions |
| --- | --- | --- |
| [UC-001], [MIL-002] | fits one iteration | none |

## INVEST Check

Independent (the only story), Negotiable (file names are defaults), Valuable (delivers the assignment result), Estimable, Small (one iteration), Testable (the criteria are checkable with fixture rows and the 2018 census file). No exceptions.

---

[UCD-001]: ./use-case-diagram.md
[BC-001]: ./business-case.md
[MIL-001]: ./milestones/mil-001-project-scaffold.md
[MIL-002]: ./milestones/mil-002-census-analysis.md
[MIL-003]: ./milestones/mil-003-documentation.md
[MIL-004]: ./milestones/mil-004-wiki-publication.md
[UC-001]: ./uc-001/uc.md

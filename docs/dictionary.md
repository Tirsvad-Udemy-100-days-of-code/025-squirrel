# Domain Dictionary (PO and IT terms)

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f1b3c03] |

---

## Purpose and Scope

Maps each Product Owner (PO) term of the squirrel census project to its professional IT term. PO language: English (`en`), domain `it`. It covers the terms of the Business Case, Stakeholder Analysis, milestones, user story, use case and Domain Model.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| Census file | en | source file | The file with the 2018 squirrel census that the participant supplies to the program. | BC, SA, MIL, user story (US), use case (UC), domain model (DM) | system sequence diagram (SSD), source code |
| Squirrel sighting | en | sighting row | One recorded observation of one squirrel in the census file. | BC, MIL, US, UC, DM | SSD, source code |
| Fur colour | en | fur_color | The primary fur colour of a squirrel: Gray, Cinnamon or Black. | BC, SA, MIL, US, UC, DM | SSD, source code |
| Colour count | en | color_count | The number of squirrel sightings with one fur colour. | BC, MIL, US, UC, DM | SSD, source code |
| Summary | en | summary table | The table of fur colours and their counts that is exported as `squirrel_count.csv`. | BC, MIL, US, UC, DM | SSD, source code |
| Participant | en | command line user | The course participant who runs the program on the census file. | BC, SA, US, UC | SSD |

## Rules

- The Domain Model, use cases and user stories use the PO term; the Operation
  Contract, Sequence Diagram, Design Class Diagram, ERD and source code use the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.
- A new concept in the Domain Model gets a row in the same change.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[f1b3c03]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/f1b3c034dc3880b7884646b4a4ed28e5f98fbcd3

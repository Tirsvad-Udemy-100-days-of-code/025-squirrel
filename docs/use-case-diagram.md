# Use Case Diagram

## Metadata
| Key | Value |
| --- | --- |
| ID | UCD-001 |
| CrossReference | [SA-001], [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose and Scope

The system is the squirrel census program. The boundary contains the one goal of the assignment: counting squirrels by fur colour from the census file and writing the summary. The participant is the only actor.

## Diagram

```plantuml
@startuml
left to right direction
actor "Participant" as A1
rectangle "Squirrel Census Program" {
  usecase "Count squirrels by fur colour" as UC1
}
A1 --> UC1
@enduml
```

## Actor Table

| Actor | Stereotype | Stakeholder ID (SA) | Goals (use cases) |
| --- | --- | --- | --- |
| Participant | <<Actor>> | S01, S02 | Count squirrels by fur colour |
| Squirrel Census Program | <<System>> | S01 | - |

## Use Case Table

| Use Case | Actor(s) | Goal |
| --- | --- | --- |
| Count squirrels by fur colour | Participant | Get the number of squirrels of each fur colour as a summary file |

## Relationships

| From | Relationship (`<<include>>` / `<<extend>>`) | To | Justification |
| --- | --- | --- | --- |
| - | - | - | There is only one use case, so there is no include or extend relationship |

---

[SA-001]: ./stakeholder-analysis.md
[BC-001]: ./business-case.md

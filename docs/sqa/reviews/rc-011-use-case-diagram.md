# RC-011 Review of UCD-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [UCD-001], [QC-UCD-001], [QC-LANG-001], [DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [UCD-001]
- Checklist used: [QC-UCD-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Actors are defined with correct UML stereotypes (e.g. `<<System>>`, `<<Actor>>`) (Mandatory) | Pass | Participant is <<Actor>> and Squirrel Census Program is <<System>> in the Actor Table. |
| 2 | System boundary is clearly drawn and labeled (Mandatory) | Pass | The diagram draws the labelled rectangle "Squirrel Census Program". |
| 3 | Include/extend relationships are used correctly per UML 2.5.1, not as generic "uses" arrows (Mandatory) | Pass | No include or extend relationship is used; the Relationships table says why. |
| 4 | Every actor participates in at least one use case (no orphan actors) (Mandatory) | Pass | The Participant takes part in the only use case. |
| 5 | Diagram is traceable to a documented stakeholder need (Mandatory) | Pass | The actor table traces the Participant to S01 and S02 of [SA-001]. |
| 6 | Use case names are verb phrases describing actor goals, not internal system operations (Mandatory) | Pass | The use case "Count squirrels by fur colour" is a verb phrase of the actor goal. |
| 7 | Diagram is free of implementation detail (e.g. UI widgets, database tables) (Optional) | Pass | No UI or storage detail. |
| 8 | Actor and use case naming is consistent with corresponding Use Case and User Story documents (Optional) | Pass | Names match [UC-001] and [US-001]. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder (Mandatory) | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list (Mandatory) | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language (Mandatory) | Pass | The use case diagram is written in English throughout. |
| 4 | The register matches the one the registry gives for the artifact type (Mandatory) | Pass | Professional register: actors, stereotypes and goals. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms (Mandatory) | Pass | Terms Participant, Census file, Squirrel sighting, Fur colour, Colour count, Summary and Summary file match [DICT-001]. |
| 6 | Metadata keys, section headings, IDs and statuses are in English (Mandatory) | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document (Mandatory) | Pass | No translated twin exists in `docs/`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again (Mandatory) | Pass | First version; no earlier accepted language. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly (Mandatory) | Pass | Reviewer reads English and knows the software domain; no second reviewer needed. |
| 10 | Abbreviations are spelled out on first use, in the stated language (Optional) | Pass | Abbreviations are expanded on first use in the body (S-IDs and artifact IDs are framework labels). |

## Overall Verdict

Go — all Mandatory criteria pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[UCD-001]: ../../use-case-diagram.md
[QC-UCD-001]: ../../../framework/qc/artifacts/qc-use-case-diagram.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[DICT-001]: ../../dictionary.md

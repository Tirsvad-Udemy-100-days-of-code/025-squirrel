# RC-013 Review of UC-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [UC-001], [QC-UC-001], [QC-LANG-001], [DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [259d017] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Link definitions added for the IDs cited in the text | pending |

---

## Artifact Under Review

- Instance reviewed: [UC-001]
- Checklist used: [QC-UC-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Consists of a single, concise paragraph summarizing only the primary success scenario (Mandatory) | N-A | The format is Fully Dressed, not Brief. |
| 2 | Written as an informal multi-paragraph narrative; may mention some alternate flows without formal structure (Mandatory) | N-A | The format is Fully Dressed, not Casual. |
| 3 | All standard sections are present: actors, preconditions, postconditions, main success scenario, alternative/exception flows (Mandatory) | Pass | Scope, level, primary actor, stakeholders, pre- and postconditions, main scenario, extensions, business rules and open issues are present. |
| 4 | Preconditions and postconditions are explicitly defined (Mandatory) | Pass | Preconditions and postconditions are stated. |
| 5 | Primary actor is explicitly stated (Mandatory) | Pass | Primary actor is Participant. |
| 6 | Stakeholders and their interests are stated (Mandatory) | Pass | S01, S02 and S03 with their interests. |
| 7 | Main success scenario is written as clear, numbered steps (Mandatory) | Pass | Main success scenario has four numbered steps. |
| 8 | Alternative/exception flows correctly reference `<<include>>`/`<<extend>>` use cases where relevant, per UML 2.5.1 (Mandatory) | Pass | Extensions 1a and 2a need no include or extend use case. |
| 9 | Explicit business rules are captured per step where applicable, rather than embedded loosely in narrative text (Optional) | Pass | Business rules are listed per step. |
| 10 | Naming of actors and use case title is consistent with the corresponding Use Case Diagram and User Stories (Mandatory) | Pass | Title and actor match [UCD-001] and [US-001]. |
| 11 | Scope/level (e.g. summary, user-goal, subfunction) is explicitly stated (Optional) | Pass | Level is user-goal. |
| 12 | Use case is written from the actor's goal perspective, free of UI or implementation detail (Mandatory) | Pass | Written from the goal of the participant; no UI detail. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder (Mandatory) | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list (Mandatory) | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language (Mandatory) | Pass | The use case is written in English throughout. |
| 4 | The register matches the one the registry gives for the artifact type (Mandatory) | Pass | Professional register: numbered scenario and business rules. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms (Mandatory) | Pass | Terms Participant, Census file, Squirrel sighting, Fur colour, Colour count, Summary and Summary file match [DICT-001]. |
| 6 | Metadata keys, section headings, IDs and statuses are in English (Mandatory) | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document (Mandatory) | Pass | No translated twin exists in `docs/`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again (Mandatory) | Pass | First version; no earlier accepted language. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly (Mandatory) | Pass | Reviewer reads English and knows the software domain; no second reviewer needed. |
| 10 | Abbreviations are spelled out on first use, in the stated language (Optional) | Pass | Abbreviations are expanded on first use in the body (S-IDs and artifact IDs are framework labels). |

## Overall Verdict

Go — all Mandatory criteria pass; criteria 1 and 2 apply to other formats.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[UC-001]: ../../uc-001/uc.md
[QC-UC-001]: ../../../framework/qc/artifacts/qc-use-case.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[DICT-001]: ../../dictionary.md
[259d017]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/259d017ad257059330eb9a8bdbf940c9d082664e
[UCD-001]: ../../use-case-diagram.md
[US-001]: ../../user-stories.md

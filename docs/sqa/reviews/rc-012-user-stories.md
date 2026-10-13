# RC-012 Review of US-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [US-001], [QC-US-001], [QC-LANG-001], [DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [259d017] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Link definitions added for the IDs cited in the text | pending |

---

## Artifact Under Review

- Instance reviewed: [US-001]
- Checklist used: [QC-US-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Follows INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable) (Mandatory) | Pass | INVEST check line states each property; one story, no exceptions. |
| 2 | Written in "As a / I want / So that" form (Mandatory) | Pass | US-001.01 uses "As a / I want / so that". |
| 3 | Clear, testable acceptance criteria are included (Mandatory) | Pass | Four Given/When/Then criteria, including the figures 2473, 392 and 103. |
| 4 | Traceable to a use case or epic (Mandatory) | Pass | Traces to [UC-001] and [MIL-002]. |
| 5 | Story is sized to fit within a single iteration (Optional) | Pass | Fits one iteration. |
| 6 | Story statement avoids technical implementation detail (Optional) | Pass | The story names no technology. |
| 7 | Role named in the story matches an actor defined in the Use Case Diagram (Mandatory) | Pass | Role "Participant" is the actor of [UCD-001]. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder (Mandatory) | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list (Mandatory) | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language (Mandatory) | Pass | The user story is written in English throughout. |
| 4 | The register matches the one the registry gives for the artifact type (Mandatory) | Pass | Professional register: story form and acceptance criteria. |
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

[US-001]: ../../user-stories.md
[QC-US-001]: ../../../framework/qc/artifacts/qc-user-story.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[DICT-001]: ../../dictionary.md
[259d017]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/259d017ad257059330eb9a8bdbf940c9d082664e
[MIL-002]: ../../milestones/mil-002-census-analysis.md
[UC-001]: ../../uc-001/uc.md
[UCD-001]: ../../use-case-diagram.md

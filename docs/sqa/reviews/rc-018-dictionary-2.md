# RC-018 Review of DICT-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-018 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001], [DM-002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001] and [QC-LANG-001]
- Scope: full review (second review; conditions of RC-007 closed)
- Language and domain: en / it
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition (Mandatory) | Pass | All seven rows have PO term, language, IT term and definition. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) (Mandatory) | Pass | One IT term per PO term and the reverse; no synonyms. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term (Mandatory) | Pass | Every concept of [DM-001] and [DM-002] has a row (Participant, Census file, Squirrel sighting, Fur colour, Colour count, Summary, Summary file) and the model uses the PO terms. |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term (Mandatory) | N-A | The project creates no Operation Contract, Sequence Diagram, Design Class Diagram or ERD; design is the system sequence diagram and source code. |
| 5 | Definitions are written in the PO language and are one sentence (Optional) | Pass | Definitions are single English sentences. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project (Optional) | Pass | Used-in columns name existing types. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry (Mandatory) | Pass | Language en and Domain it match the registry. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder (Mandatory) | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list (Mandatory) | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language (Mandatory) | Pass | The dictionary is written in English throughout. |
| 4 | The register matches the one the registry gives for the artifact type (Mandatory) | Pass | Professional register: term pairs. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms (Mandatory) | Pass | This document is the dictionary. |
| 6 | Metadata keys, section headings, IDs and statuses are in English (Mandatory) | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document (Mandatory) | Pass | No translated twin exists in `docs/`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again (Mandatory) | Pass | First version; no earlier accepted language. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly (Mandatory) | Pass | Reviewer reads English and knows the software domain; no second reviewer needed. |
| 10 | Abbreviations are spelled out on first use, in the stated language (Optional) | Pass | Abbreviations are expanded on first use in the body (S-IDs and artifact IDs are framework labels). |

## Overall Verdict

Go — all Mandatory criteria that can apply pass; criterion 4 has no object in this project. Supersedes the conditions of RC-007.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[DM-002]: ../../domain-model.md

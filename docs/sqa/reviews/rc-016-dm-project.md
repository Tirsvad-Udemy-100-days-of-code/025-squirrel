# RC-016 Review of DM-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [DM-002], [QC-DM-001], [QC-LANG-001], [DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [DM-002]
- Checklist used: [QC-DM-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Uses ubiquitous/business language throughout; no technical or implementation jargon (e.g. no "table", "class", "pointer") (Mandatory) | Pass | Concepts are business terms from [DICT-001]; no table or class names. |
| 2 | Multiplicities on associations are correct and complete (e.g. `1..*`, `0..1`) (Mandatory) | Pass | All six associations have multiplicities at both ends. |
| 3 | No operation/method signatures shown — attributes and associations only (Mandatory) | Pass | Concepts show attributes and associations only. |
| 4 | Associations are named with an unambiguous reading direction (Optional) | Pass | Association names have a reading direction (supplies, contains, has, counts sightings of, consists of, is written to, receives). |
| 5 | Generalization/specialization used correctly, reflecting true "is-a" relationships, not misused for code reuse (Optional) | Pass | No generalization is used. |
| 6 | Every concept traces to a noun phrase found in the use cases or glossary (Mandatory) | Pass | Every concept traces to a noun in [UC-001] or [DICT-001]. |
| 7 | Attributes are simple domain data (no foreign-key-like references or object pointers modeled as attributes) (Mandatory) | Pass | Attributes are name and number of sightings; relations are associations. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder (Mandatory) | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list (Mandatory) | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language (Mandatory) | Pass | The domain model is written in English throughout. |
| 4 | The register matches the one the registry gives for the artifact type (Mandatory) | Pass | Professional register: concepts and associations. |
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

[DM-002]: ../../domain-model.md
[QC-DM-001]: ../../../framework/qc/artifacts/qc-domain-model.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[DICT-001]: ../../dictionary.md

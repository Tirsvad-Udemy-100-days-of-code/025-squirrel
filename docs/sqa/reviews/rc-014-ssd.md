# RC-014 Review of SSD-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [SSD-001], [QC-SSD-001], [QC-LANG-001], [DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [259d017] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Link definitions added for the IDs cited in the text | [5b948e5] |

---

## Artifact Under Review

- Instance reviewed: [SSD-001]
- Checklist used: [QC-SSD-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Input/output messages match the corresponding Use Case's main success scenario step-for-step (Mandatory) | Pass | One message `countByFurColor` covers use case steps 1 to 4; the table justifies it. |
| 2 | Actor and System are treated strictly as black boxes (system shown as `:System`) (Mandatory) | Pass | Only Participant and :System appear. |
| 3 | Object creation/destruction of the System instance handled explicitly where relevant (Optional) | Pass | Lifecycle Notes: the instance lives for one run. |
| 4 | Return values are shown for operations that produce one, using dashed return arrows (Mandatory) | Pass | Dashed return arrows `summary` and `censusFileMissing`. |
| 5 | Alternate/exceptional flows are represented separately (or explicitly out of scope noted) (Mandatory) | Pass | The alternate flow 1a is the second diagram; 2a is stated to have no message. |
| 6 | Message names are verb phrases consistent with the use case's system responsibilities (Optional) | Pass | `countByFurColor` is a verb phrase. |
| 7 | Diagram references the specific Use Case (name and ID) it depicts (Mandatory) | Pass | Source Use Case names Count squirrels by fur colour ([UC-001]). |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder (Mandatory) | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list (Mandatory) | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language (Mandatory) | Pass | The system sequence diagram is written in English throughout. |
| 4 | The register matches the one the registry gives for the artifact type (Mandatory) | Pass | Professional register: messages, parameters and returns. |
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

[SSD-001]: ../../uc-001/ssd.md
[QC-SSD-001]: ../../../framework/qc/artifacts/qc-ssd.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[DICT-001]: ../../dictionary.md
[259d017]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/259d017ad257059330eb9a8bdbf940c9d082664e
[UC-001]: ../../uc-001/uc.md
[5b948e5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/5b948e5a66bbcea5ef062f4557f47aae113a4e07

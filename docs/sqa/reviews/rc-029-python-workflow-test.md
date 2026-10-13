# RC Review of the workflow test

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-029 |
| CrossReference | [PY-MIL-001-7], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [7202aac] |

---

## Artifact Under Review

- Instance reviewed: [PY-MIL-001-7]
- Checklist used: [QC-PY-001]
- Scope: full review of tests/test_workflow.py and the dev extra of pyproject.toml
- Language and domain: n/a
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) (Mandatory) | Pass | Functions, constants (`MAX_RUN_LINES`) and class (`UniqueKeyLoader`) follow PEP 8 casing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes (Mandatory) | Pass | Names state purpose (`exceeds_line_limit`, `load_workflow`). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions (Mandatory) | Pass | `ruff check` and `ruff format --check` pass with no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` (Mandatory) | Pass | Every function is annotated; `mypy --strict` passes on 11 files; `Any` is justified by a comment. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) (Mandatory) | Pass | The duplicate-key loader raises `ValueError` with the key named; no bare except. |
| 6 | No mutable default arguments and no shadowed builtins (Mandatory) | Pass | No mutable defaults; no builtins shadowed. |
| 7 | Files, locks and connections are managed with context managers (Mandatory) | Pass | The workflow file is read through `pathlib` and the YAML loader, which close the file. |
| 8 | Public modules, classes and functions have docstrings that say what, not how (Optional) | Pass | Helpers and tests have docstrings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output (Mandatory) | Pass | No print and no logging; no secrets. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded (Mandatory) | N-A | Test code; no class or operation of a design class diagram. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network (Mandatory) | Pass | 14 tests, one behaviour each, plus a negative self-test of the line limit; no order or network dependence. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment (Optional) | Pass | `mypy --strict` passes; `Any` is commented. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused (Optional) | Pass | `pyyaml` and `types-PyYAML` are dev dependencies pinned exactly; no runtime dependency added. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike (Mandatory) | Pass | The line limit is the single constant `MAX_RUN_LINES`, matching the rule in the YAML convention. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles (Mandatory) | Pass | The test imports the standard library and `yaml`; it imports no application code. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations (Mandatory) | Pass | One module of small single-purpose helpers and tests. |

## Overall Verdict

Go — all Mandatory criteria pass; criterion 10 is not applicable.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[PY-MIL-001-7]: ../../../tests/test_workflow.py
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[7202aac]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/7202aac5956ef92ab6a4efc6cb1917de075d771a

# RC Review of the MIL-002 Python files

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-024 |
| CrossReference | [PY-MIL-002], [QC-PY-001], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [259d017] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Link definitions added for the IDs cited in the text | [5b948e5] |

---

## Artifact Under Review

- Instance reviewed: [PY-MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review of src/squirrel/census.py, cli.py, __main__.py, constants.py and tests/
- Language and domain: n/a
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) (Mandatory) | Pass | Modules, functions and constants use snake_case and UPPER_SNAKE; helper `_build_parser` has one leading underscore. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes (Mandatory) | Pass | Names state purpose (`count_by_fur_color`, `write_csv`); the lecture step names are kept (ADR-0001). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions (Mandatory) | Pass | `ruff check` and `ruff format --check` (0.17.0) pass with no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` (Mandatory) | Pass | Every function is annotated including `-> None`; `mypy --strict` passes on 10 files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) (Mandatory) | Pass | No exception handling; a missing file is checked with `is_file()` and reported with exit status 2. |
| 6 | No mutable default arguments and no shadowed builtins (Mandatory) | Pass | The only default argument is the immutable tuple `FUR_COLORS`; no builtin is shadowed. |
| 7 | Files, locks and connections are managed with context managers (Mandatory) | Pass | Files are opened with `with path.open(...)`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how (Optional) | Pass | Public modules and functions have Doxygen blocks and docstrings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output (Mandatory) | Pass | `print` is used only for the CLI output to the participant and the stderr error line, not for logging; no secrets. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded (Mandatory) | N-A | No class is defined and no Design Class Diagram exists; operations trace to [SSD-001] (`countByFurColor`). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network (Mandatory) | Pass | 20 tests: unit tests per function, CLI tests, a real-census test and an imports test; none depends on order or network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment (Optional) | Pass | `mypy 2.4.0 --strict` reports no issues. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused (Optional) | Pass | No runtime dependency; dev tools pinned in `pyproject.toml`. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike (Mandatory) | Pass | All literals live in `constants.py`; each step is defined once. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles (Mandatory) | Pass | `census.py` imports only the standard library and constants; `cli.py` imports `census`; no cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations (Mandatory) | Pass | `census.py` holds four single-purpose functions; the CLI only wires them. |

## Overall Verdict

Go — all Mandatory criteria pass; criterion 10 is not applicable because no class exists.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[PY-MIL-002]: ../../../src/squirrel/census.py
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[ADR-0001]: ../../adr/adr-0001-standard-library-instead-of-pandas.md
[259d017]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/259d017ad257059330eb9a8bdbf940c9d082664e
[SSD-001]: ../../uc-001/ssd.md
[5b948e5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/5b948e5a66bbcea5ef062f4557f47aae113a4e07

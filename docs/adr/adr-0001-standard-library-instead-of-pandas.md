# ADR-0001 Use the standard library instead of Pandas

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001], [MIL-002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The day 25 lecture reads the census with `pandas.read_csv`, filters rows by fur colour and builds a DataFrame for the export. The Business Case sets a success criterion of zero third-party runtime packages ([BC-001], criterion 3), and stakeholder S03 wants a repository with no runtime dependencies ([SA-001]). Stakeholder S02 wants the function names of the assignment.

Options evaluated:

1. **Pandas** — closest to the lecture; adds a large runtime dependency (with NumPy) that every visitor must install.
2. **Standard library** — the `csv` module to read and write and `collections.Counter` to count; no runtime dependency, a few more lines than Pandas.
3. **Pandas as an optional extra** — two code paths for one result; more code to test and explain.

## Decision

Use the standard library (`csv` and `collections.Counter`) for reading, counting and writing, and keep the lecture's step names (`read_csv`, `count_by_fur_color`, `build_summary`, `write_csv`) as public function names.

## Consequences

**Positive:**

- The project has no runtime dependency; `pip install .` installs only the package ([BC-001] criterion 3).
- Setup is the same on Windows PowerShell, Linux Debian and macOS, with no compiled wheels.
- The code is short enough to read in one sitting (S02).

**Negative:**

- The code differs from the lecture's Pandas calls, so a participant comparing line by line sees different statements.
- A later assignment that needs DataFrame features must introduce Pandas then.

## Affected Artifacts

- [BC-001] — meets success criterion 3 and mitigates the Pandas risk.
- [SA-001] — resolves the conflict between S01's lecture and S03's expectation.
- [MIL-002] — the tasks "Read the census file" to "Add the command line entry point" implement it.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-002]: ../milestones/mil-002-census-analysis.md

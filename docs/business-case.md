# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | CrossReference: added [UCD-001] | [259d017] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Corrected the wiki folder `docs/wiki/` to `wiki/` | pending |
---

## Executive Summary

Day 25 of the Udemy "100 Days of Code" bootcamp asks the participant to analyse the 2018 Central Park Squirrel Census with Pandas: count the gray, cinnamon and black squirrels by primary fur colour and export the counts to `squirrel_count.csv`. This project delivers that assignment as a small, readable, runnable Python repository with tests, source documentation, a README and a three-language wiki, so that the participant keeps a reviewed solution and other course participants and GitHub visitors can reuse it.

## Methodological and Standards Foundation

The artifacts follow the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/` (Business Case, Stakeholder Analysis, Project Plan, milestones, tasks, code). Quality is judged against ISO/IEC 25010:2023 characteristics through the QC checklists of the framework; source code is reviewed against `qc-programming-python`.

## Problem Statement

The lecture shows the analysis as a sequence of notebook-style steps. A participant who wants to keep, share and compare the solution has no structured repository: no repeatable set-up, no tests, no documentation and no instructions that another participant can run.

## Business Opportunity

A single, well-structured example repository lets the participant practise professional project hygiene (virtual environment, tests, continuous integration, documentation) on a small assignment, and gives other participants a solution to compare against.

## Objectives

1. Deliver a Python program that reads the squirrel census file (comma-separated values, CSV), counts squirrels by primary fur colour (gray, cinnamon, black) and writes `squirrel_count.csv`.
2. Cover the program with automated pytest tests that run without the full census file.
3. Document how to create a local `.venv`, upgrade pip, run the program and run the tests, for Windows PowerShell, Linux Debian and macOS.
4. Document the source with Doxygen comments and a `Doxyfile`.
5. Publish the repository with a description, topics, a README and a wiki in English, Danish and Bahasa Malaysia, with screenshots.

## Scope

### In Scope

- Reading the census file and counting squirrels by primary fur colour.
- Creating a summary table and exporting it as `squirrel_count.csv`.
- A command-line entry point, `constants.py`, `pyproject.toml`, a Python `.gitignore`, pytest tests and a continuous integration (CI) workflow.
- Doxygen comments, a `Doxyfile` and build instructions.
- README from the framework template, a three-language wiki and screenshots.
- Repository description and topics on the git host.

### Out of Scope

- Analysis beyond the three fur colours of the assignment.
- Charts, notebooks or a graphical interface.
- Publishing a package to PyPI.
- Using or importing the `.env` file in the project; it holds personal tokens for publishing only.

## Expected Benefits

### Tangible Benefits

- A runnable solution with passing tests and a CI pipeline.
- A repository other participants can clone and run from the README alone.
- A published description, topics and wiki in three languages.

### Intangible Benefits

- Practice in a plan-first, reviewed workflow on a small project.
- A reusable repository layout for later days of the bootcamp.

## Strategic Alignment

The project supports the participant's goal of finishing the 100 Days of Code bootcamp with portfolio-quality results, and the framework's goal of showing the SQA workflow on a real, small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Fur colour counts are correct | Gray 2473, Cinnamon 392, Black 103 on the 2018 census file | Run the program on the census file and compare with `squirrel_count.csv` |
| 2 | Tests pass | 100 % of pytest tests pass on Python 3.13 or later | `python -m pytest` exit code 0 and CI green |
| 3 | Runtime dependencies | 0 third-party runtime packages | `pyproject.toml` lists no runtime dependencies |
| 4 | Documentation present | README sections, Doxyfile and wiki pages in 3 languages | Files exist; `doxygen Doxyfile` completes without warnings |
| 5 | Repository metadata | Description and at least 5 topics set | Read back from the git host application programming interface (API) |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The lecture uses Pandas but the repository must have no runtime dependencies | The solution differs from the lecture code | Use the standard library `csv` module; record the decision in an architecture decision record (ADR) and keep the lecture's step names as function names |
| The census file is large and not part of the repository | Others cannot run the program | Keep the census file under `data/` and let the program accept a path argument |
| Tokens in `.env` leak into the repository | Credential exposure | `.env` is git-ignored, never read by the project and never printed |
| Wiki push is not available on the host | Wiki pages are not published | Keep the pages in the repository under `wiki/` and report the failure |
| Fur colour spelling differs in the data | Wrong counts | Count exact values `Gray`, `Cinnamon`, `Black` and test with fixture rows |

## Assumptions

- The participant (S01) is Product Owner, developer and reviewer of every artifact.
- The census file is the 2018 Central Park Squirrel Census file the participant downloaded.
- The git host `git.tirsystem.com` accepts the personal tokens held in `.env`.
- Python 3.13 or later is installed on the machines that run the project.
- The Product Owner's language is English; the wiki is the only multilingual deliverable.

## Constraints

- Python 3.13 or later, virtual environment with `venv`, tests with pytest.
- Constants live in `constants.py`; configuration lives in `pyproject.toml`.
- Folder structure `src/`, `tests/`, `docs/`.
- Work is tracked by one branch and pull request per milestone.
- Tokens come from `.env` and are never tested, imported or committed.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one working day of effort by S01 and the AI assistant | A reviewed, documented solution reusable by S02 and S03 |
| Maintenance of three wiki languages | Broader reach for S02 and S03 |

The assessment is qualitative: the project is a personal learning exercise with no revenue, so a monetary return would not be meaningful.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a correct, reviewed solution |
| S02 | Course participants; want readable, runnable code and run instructions |
| S03 | GitHub viewers; want a clear description, topics and README with no runtime dependencies |

## Recommendation

Proceed — the scope is small, the risks are mitigated and the result is directly reusable by the other stakeholders.

---

[UCD-001]: ./use-case-diagram.md
[259d017]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/259d017ad257059330eb9a8bdbf940c9d082664e

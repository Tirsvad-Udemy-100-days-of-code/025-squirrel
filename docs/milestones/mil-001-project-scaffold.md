# MIL-001 Project scaffold and tooling

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | CrossReference: added [US-001] | [259d017] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added task 7: static workflow test (RC-010 action item) | pending |
---

## Purpose

Decide whether the repository has the tooling baseline (ignore rules, project configuration, constants module, Doxygen configuration and continuous integration (CI)) on which the analysis code can be built and reviewed.

## Deliverable

A branch merged to `main` containing `.gitignore`, `pyproject.toml`, `src/squirrel/constants.py`, `Doxyfile`, a CI workflow, and the repository description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python = ">=3.13"` and no runtime dependencies | Present | Missing or has runtime dependencies |
| 2 | `.gitignore` ignores `.venv/`, `__pycache__/`, `.env` and `.pytest_cache/` | Present | Any missing |
| 3 | `python -m pytest` runs in a fresh `.venv` and exits 0 (collects at least the constants test) | Exit 0 | Non-zero exit |
| 4 | Repository description and at least 5 topics read back from the git host application programming interface (API) | Set | Not set |
| 5 | Review record for each reviewed artifact is `Go` | All Go | Any No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| BC-001, SA-001, PP-001 | The baseline must be accepted before milestones |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4, Success Criteria 3 and 5 | [BC-001] |
| S03 concern: description and topics | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — one day after the plan, inside the single-day effort in the Business Case cost assessment

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add Python .gitignore | Add the standard Python ignore rules plus `.env`, `.venv/` and Doxygen output (`docs/doxygen/`), so tokens and build output never reach the repository. | No |  |
| 2 | Add pyproject.toml | Configure the `squirrel` package in a `src/` layout: `requires-python >=3.13`, no runtime dependencies, an optional `dev` extra with pytest, and pytest `pythonpath` and `testpaths`. This is the single configuration file the Business Case constraints require. | No |  |
| 3 | Add constants module | Create `src/squirrel/constants.py` holding file names, column names and fur colour values so no literal is repeated in the code, as the constraint requires. Add a first test that imports it. | No |  |
| 4 | Add Doxyfile | Create a `Doxyfile` that reads `src/` and writes to `docs/doxygen/`, with Python optimisation enabled, so the source documentation can be built with `doxygen Doxyfile`. | No |  |
| 5 | Add CI workflow | Add a Gitea Actions workflow that sets up Python 3.13, creates a venv, upgrades pip, installs the dev extra and runs pytest on push and pull request. It backs the "Continuous integration" section of the README. | No |  |
| 6 | Set repository description and topics | Use the Gitea API with the token from `.env` (read by the shell only, never by the project) to set a description and topics such as `python`, `csv`, `squirrel-census`, `udemy`, `100-days-of-code`, `pytest`. Satisfies stakeholder S03. | No |  |
| 7 | Add static workflow test | Add `tests/test_workflow.py`, run by pytest on every pull request, that parses `.gitea/workflows/ci.yml` with a safe YAML loader and checks the required keys, explicit permissions, runner and timeout, named steps, exact-tag action pins and the five-line limit on `run:` blocks. Closes criterion 24 (optional) of the workflow review RC-010. | No | RC-010 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[259d017]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/259d017ad257059330eb9a8bdbf940c9d082664e

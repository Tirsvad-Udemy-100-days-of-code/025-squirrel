# MIL-002 Squirrel census analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f1b3c03] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | CrossReference: added [US-001] | [259d017] |
---

## Purpose

Decide whether the squirrel census analysis is modelled, implemented and tested well enough to produce the assignment result, `squirrel_count.csv`, from the 2018 census file.

## Deliverable

A branch merged to `main` containing the user story, use case, system sequence diagram and domain model, ADR-0001, the `squirrel` package with its command line entry point, the pytest tests, the census file under `data/` and the generated `squirrel_count.csv`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Running the program on the 2018 census file writes `squirrel_count.csv` with Gray 2473, Cinnamon 392, Black 103 | Matches | Differs |
| 2 | `python -m pytest` exits 0 and covers reading, counting, summary and export | Exit 0 | Failure or a function untested |
| 3 | The package imports no third-party module (checked by `pyproject.toml` and a test) | None | Any import |
| 4 | Source review against `qc-programming-python` has verdict `Go` | Go | No-Go |
| 5 | Model artifacts (user story (US), use case (UC), system sequence diagram (SSD), domain model (DM)) and ADR-0001 have review verdict `Go` | All Go | Any No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Tooling, constants and test infrastructure are needed first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 2, Success Criteria 1, 2 and 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-15 — one day after MIL-001, inside the single-day effort

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write user story and use case | Write US-001 and brief UC-001 "Count squirrels by fur colour": the participant supplies the census file and receives `squirrel_count.csv`. Needed because it is a goal an actor pursues. | No |  |
| 2 | Model the interaction and concepts | Create `ssd.md` and `dm.md` in `docs/uc-001/`, then reconcile `docs/domain-model.md`. Concepts: Census file, Sighting, Fur colour, Colour count, Summary. | No | UC-001 |
| 3 | Record ADR-0001 standard library instead of Pandas | Decide to use the `csv` module and `collections.Counter` so the repository has no runtime dependencies (S03), while the function names follow the lecture steps (S02). | No |  |
| 4 | Read the census file | Implement `read_csv(path)` returning the sightings with the primary fur colour column, using only the standard library. The file is read as UTF-8. | Yes | UC-001 |
| 5 | Count squirrels by fur colour | Implement `count_by_fur_color(rows, colors)` returning the count for gray, cinnamon and black, using the values defined in `constants.py`. | Yes | UC-001 |
| 6 | Build the summary and export it | Implement `build_summary(counts)` and `write_csv(summary, path)` producing `squirrel_count.csv` with the columns `Fur Color` and `Count`, mirroring the lecture's DataFrame-to-comma-separated-values (CSV) step. | Yes | UC-001 |
| 7 | Add the command line entry point | Add `python -m squirrel [input] [output]` with the census file path defaulting under `data/` and the output defaulting to `squirrel_count.csv`. Exit non-zero with a message when the input is missing. | Yes | UC-001 |
| 8 | Add pytest tests with fixture rows | Test each function with a small fixture CSV file so the tests run without the 730 kilobytes (KB) census file, plus one test that checks the real census file counts when the file is present. | No |  |
| 9 | Add the census file and generate the result | Copy the 2018 census file into `data/` and run the program once to produce `squirrel_count.csv`, so others can run the project without downloading the file. | No |  |

---

[BC-001]: ../business-case.md
[f1b3c03]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/f1b3c034dc3880b7884646b4a4ed28e5f98fbcd3
[US-001]: ../user-stories.md
[259d017]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/259d017ad257059330eb9a8bdbf940c9d082664e

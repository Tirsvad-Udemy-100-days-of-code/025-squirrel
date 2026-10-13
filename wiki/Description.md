🌐 **English** · [Dansk](Description.da) · [Bahasa Melayu](Description.ms)

# Description

## What it does

The program follows the steps of the lecture:

1. `read_csv` reads the census file.
2. `count_by_fur_color` counts the sightings of Gray, Cinnamon and Black.
3. `build_summary` turns the counts into the rows of a summary.
4. `write_csv` writes the summary to `squirrel_count.csv`.

On the 2018 census file the result is Gray 2473, Cinnamon 392 and Black 103. Sightings without a fur colour are counted in none of them.

## Why no Pandas

The lecture uses Pandas. This project uses only the Python standard library (`csv` and `collections.Counter`) so that there is nothing to install to run it. The decision is recorded as ADR-0001 in the repository.

## Layout

| Path | Content |
| --- | --- |
| `src/squirrel/census.py` | The four steps above |
| `src/squirrel/cli.py` | The command line, `python -m squirrel` |
| `src/squirrel/constants.py` | Every literal, defined once |
| `tests/` | The pytest tests |
| `docs/` | Business case, plan, models, review records |

## Quality

Every document and every piece of code was reviewed against the checklists of the SQA and QC framework, in autonomous mode: the reviewer is an AI stand-in, so the reviews are not independent.

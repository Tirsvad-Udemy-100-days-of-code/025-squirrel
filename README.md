# Squirrel Census

Day 25 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*: count the
squirrels of the 2018 Central Park Squirrel Census by primary fur colour (gray,
cinnamon, black) and export the counts to `squirrel_count.csv`. Python 3.13 or
later, no runtime dependencies, with tests and source documentation.

![Program run][img-run]

## Requirements

- Python 3.13 or later (`python --version` on Windows, `python3 --version` on Linux and macOS).
- `venv`, which ships with Python (on Debian: the `python3-venv` package).
- The 2018 census file. It is already in the repository under `data/`.
- Optional: [Doxygen][doxygen] 1.9 or later, only to build the source documentation.

There are no runtime dependencies: the program uses only the Python standard library
([ADR-0001][adr-0001]). `pytest` is needed only to run the tests.

## Set up

Create a local virtual environment named `.venv` in the project folder, upgrade `pip`
and install the project with its development tools (pytest, ruff, mypy).

### Windows powershell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, allow it for the current session:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`.

### Linux debian

```bash
sudo apt install python3 python3-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### MacOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On macOS, Python 3.13 can be installed with `brew install python@3.13`.

## Run

With the virtual environment active, run from the project folder:

```bash
python -m squirrel
```

The program reads `data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv`, prints
the colour counts and writes `squirrel_count.csv`:

```text
Gray: 2473
Cinnamon: 392
Black: 103
```

Use other files by passing them as arguments, `python -m squirrel <census file> <summary file>`.
If the census file does not exist the program prints a message and exits with status 2.

## Run the tests

```bash
python -m pytest
```

![Test run][img-tests]

The tests use small fixture rows; one test also checks the real 2018 census file when
it is present.

## Continuous integration

The workflow [`.gitea/workflows/ci.yml`][ci] runs for every push to `main` and for every
pull request. It sets up Python 3.13, creates a `.venv`, upgrades `pip`, installs the
project with `.[dev]` and runs `python -m pytest`. It uses `github.*` contexts only, so
it also runs on GitHub Actions.

## Build the source documentation

The source is documented with Doxygen comments and configured by [`Doxyfile`][doxyfile].

```bash
doxygen Doxyfile
```

Open `docs/doxygen/html/index.html` in a browser. The output folder is ignored by git.

## Project layout

```text
.gitea/workflows/ci.yml   continuous integration workflow
data/                     the 2018 census file
docs/                     business case, plan, milestones, models, reviews, ADRs
docs/images/              screenshots used by this README and the wiki
src/squirrel/             the package: census.py, cli.py, constants.py
tests/                    pytest tests
wiki/                     wiki pages in English, Danish (.da) and Bahasa Malaysia (.ms)
Doxyfile                  Doxygen configuration
pyproject.toml            project configuration (Python >=3.13, no runtime dependencies)
squirrel_count.csv        the result of the assignment
```

The project documents, in reading order: [Business Case][bc], [Stakeholder
Analysis][sa], [Project Plan][pp], [Use Case][uc], [Domain Model][dm], [ADR-0001][adr-0001].
The repository also has a wiki in English, Danish and Bahasa Malaysia.

## License

GNU Affero General Public License v3.0 or later. See [LICENSE][license].

---

[img-run]: docs/images/run.png
[img-tests]: docs/images/tests.png
[doxygen]: https://www.doxygen.nl/
[adr-0001]: docs/adr/adr-0001-standard-library-instead-of-pandas.md
[ci]: .gitea/workflows/ci.yml
[doxyfile]: Doxyfile
[bc]: docs/business-case.md
[sa]: docs/stakeholder-analysis.md
[pp]: docs/project-plan.md
[uc]: docs/uc-001/uc.md
[dm]: docs/domain-model.md
[license]: LICENSE

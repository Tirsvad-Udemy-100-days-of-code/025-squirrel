🌐 [English](Install) · **Dansk** · [Bahasa Melayu](Install.ms)

# Installation

Projektet kræver **Python 3.13 eller nyere**. Det har ingen kørselsafhængigheder; `pytest`, `ruff`, `mypy`, `yamllint` og `actionlint` er udviklingsværktøjer.

## Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux Debian

På Debian 13 (trixie) eller nyere er `python3` 3.13:

```bash
sudo apt install python3 python3-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

På Debian 12 (bookworm) er `python3` 3.11, og `pip` nægter at installere projektet (`requires a different Python`). Hent Python 3.13 med [uv](https://docs.astral.sh/uv/) og brug den til `.venv`:

```bash
sudo apt install python3 python3-venv
python3 -m venv .uvenv
.uvenv/bin/python -m pip install uv
.uvenv/bin/uv python install 3.13
.uvenv/bin/uv venv --seed --python 3.13 .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Næste: [Brug](Usage.da).

🌐 [English](Install) · **Dansk** · [Bahasa Melayu](Install.ms)

# Installation

Projektet kræver **Python 3.13 eller nyere**. Det har ingen kørselsafhængigheder; `pytest`, `ruff` og `mypy` er udviklingsværktøjer.

## Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux Debian

```bash
sudo apt install python3 python3-venv
python3 -m venv .venv
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

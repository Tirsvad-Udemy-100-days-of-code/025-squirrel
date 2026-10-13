🌐 **English** · [Dansk](Install.da) · [Bahasa Melayu](Install.ms)

# Install

The project needs **Python 3.13 or later**. It has no runtime dependencies; `pytest`, `ruff` and `mypy` are development tools.

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

Next: [Usage](Usage).

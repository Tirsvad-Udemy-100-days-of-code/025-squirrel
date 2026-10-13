🌐 **English** · [Dansk](Install.da) · [Bahasa Melayu](Install.ms)

# Install

The project needs **Python 3.13 or later**. It has no runtime dependencies; `pytest`, `ruff`, `mypy`, `yamllint` and `actionlint` are development tools.

## Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux Debian

On Debian 13 (trixie) or later, `python3` is 3.13:

```bash
sudo apt install python3 python3-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Debian 12 (bookworm), `python3` is 3.11 and `pip` refuses to install the project (`requires a different Python`). Get Python 3.13 with [uv](https://docs.astral.sh/uv/) and use it for the `.venv`:

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

Next: [Usage](Usage).

🌐 [English](Install) · [Dansk](Install.da) · **Bahasa Melayu**

# Pemasangan

Projek ini memerlukan **Python 3.13 atau lebih baharu**. Ia tiada kebergantungan masa jalan; `pytest`, `ruff`, `mypy`, `yamllint` dan `actionlint` ialah alat pembangunan.

## Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux Debian

Pada Debian 13 (trixie) atau lebih baharu, `python3` ialah 3.13:

```bash
sudo apt install python3 python3-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Pada Debian 12 (bookworm), `python3` ialah 3.11 dan `pip` enggan memasang projek (`requires a different Python`). Dapatkan Python 3.13 dengan [uv](https://docs.astral.sh/uv/) dan gunakannya untuk `.venv`:

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

Seterusnya: [Penggunaan](Usage.ms).

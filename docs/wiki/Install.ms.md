🌐 [English](Install) · [Dansk](Install.da) · **Bahasa Melayu**

# Pemasangan

Projek ini memerlukan **Python 3.13 atau lebih baharu**. Ia tiada kebergantungan masa jalan; `pytest`, `ruff` dan `mypy` ialah alat pembangunan.

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

Seterusnya: [Penggunaan](Usage.ms).

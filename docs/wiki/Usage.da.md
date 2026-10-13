🌐 [English](Usage) · **Dansk** · [Bahasa Melayu](Usage.ms)

# Brug

## Kør programmet

Med det virtuelle miljø aktivt, fra projektmappen:

```bash
python -m squirrel
```

Programmet læser `data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv`, skriver tallene for hver pelsfarve og gemmer `squirrel_count.csv`.

![Programkørsel](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/raw/branch/main/docs/images/run.png)

Brug andre filer med `python -m squirrel <optællingsfil> <opsummeringsfil>`. Findes optællingsfilen ikke, skriver programmet `Census file not found` og afslutter med status 2.

## Kør testene

```bash
python -m pytest
```

![Testkørsel](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/raw/branch/main/docs/images/tests.png)

## Byg kildedokumentationen

```bash
doxygen Doxyfile
```

Åbn `docs/doxygen/html/index.html`.

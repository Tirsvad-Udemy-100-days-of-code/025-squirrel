🌐 **English** · [Dansk](Usage.da) · [Bahasa Melayu](Usage.ms)

# Usage

## Run the program

With the virtual environment active, from the project folder:

```bash
python -m squirrel
```

The program reads `data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv`, prints the colour counts and writes `squirrel_count.csv`.

![Program run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/raw/branch/main/docs/images/run.png)

Use other files with `python -m squirrel <census file> <summary file>`. If the census file does not exist, the program prints `Census file not found` and exits with status 2.

## Run the tests

```bash
python -m pytest
```

![Test run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/raw/branch/main/docs/images/tests.png)

## Build the source documentation

```bash
doxygen Doxyfile
```

Open `docs/doxygen/html/index.html`.

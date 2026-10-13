##
# @file constants.py
# @brief Literals used by the squirrel census analysis, each defined once.

"""Literals used by the squirrel census analysis, each defined once."""

import pathlib

## @brief Default location of the census CSV file, relative to the working directory.
DEFAULT_INPUT_PATH: pathlib.Path = (
    pathlib.Path("data") / "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

## @brief Default location of the summary CSV file that is written.
DEFAULT_OUTPUT_PATH: pathlib.Path = pathlib.Path("squirrel_count.csv")

## @brief Text encoding of the input and output files.
FILE_ENCODING: str = "utf-8"

## @brief Name of the census column that holds the primary fur colour.
FUR_COLOR_COLUMN: str = "Primary Fur Color"

## @brief Fur colours that are counted, in the order they appear in the summary.
FUR_COLORS: tuple[str, ...] = ("Gray", "Cinnamon", "Black")

## @brief Header of the summary file: the colour column, then the count column.
SUMMARY_COLUMNS: tuple[str, str] = ("Fur Color", "Count")

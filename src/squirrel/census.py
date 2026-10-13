##
# @file census.py
# @brief Pure steps of the census analysis: read, count, summarise, write.

"""Pure steps of the census analysis: read, count, summarise, write."""

import collections
import csv
import pathlib
from collections.abc import Iterable, Mapping, Sequence

from squirrel.constants import (
    FILE_ENCODING,
    FUR_COLOR_COLUMN,
    FUR_COLORS,
    SUMMARY_COLUMNS,
)


##
# @brief Read a CSV file into one dictionary per row, keyed by the header names.
# @param path Location of the CSV file.
# @return The rows of the file, in file order.
def read_csv(path: pathlib.Path) -> list[dict[str, str]]:
    """Read a CSV file into one dictionary per row, keyed by the header names."""
    with path.open(encoding=FILE_ENCODING, newline="") as file:
        return list(csv.DictReader(file))


##
# @brief Count the rows per fur colour; other or blank colours are counted in none.
# @param rows Census rows, each holding the fur colour column.
# @param colors Fur colours to count, in the order of the result.
# @return Count per colour of `colors`, 0 for a colour that does not occur.
def count_by_fur_color(
    rows: Iterable[Mapping[str, str]],
    colors: Sequence[str] = FUR_COLORS,
) -> dict[str, int]:
    """Count the rows per fur colour; other or blank colours are counted in none."""
    seen = collections.Counter(row.get(FUR_COLOR_COLUMN) for row in rows)
    return {color: seen[color] for color in colors}


##
# @brief Turn the counts into summary rows, keeping the order of the counts.
# @param counts Count per fur colour.
# @return One (colour, count) pair per colour.
def build_summary(counts: Mapping[str, int]) -> list[tuple[str, int]]:
    """Turn the counts into summary rows, keeping the order of the counts."""
    return list(counts.items())


##
# @brief Write the summary as a CSV file: the header row, then one row per colour.
# @param summary Rows to write, as built by `build_summary`.
# @param path Location of the CSV file; its folder must exist.
# @return None.
def write_csv(summary: Sequence[tuple[str, int]], path: pathlib.Path) -> None:
    """Write the summary as a CSV file: the header row, then one row per colour."""
    with path.open("w", encoding=FILE_ENCODING, newline="") as file:
        writer = csv.writer(file)
        writer.writerow(SUMMARY_COLUMNS)
        writer.writerows(summary)

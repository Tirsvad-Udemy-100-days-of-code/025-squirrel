"""Tests for the squirrel.census module."""

import pathlib

from squirrel import census
from squirrel.constants import (
    FILE_ENCODING,
    FUR_COLOR_COLUMN,
    FUR_COLORS,
    SUMMARY_COLUMNS,
)

OTHER_COLUMN = "Unique Squirrel ID"


def _row(color: str) -> dict[str, str]:
    return {FUR_COLOR_COLUMN: color}


def test_read_csv_returns_one_dict_per_row(tmp_path: pathlib.Path) -> None:
    path = tmp_path / "census.csv"
    path.write_text(
        f"{OTHER_COLUMN},{FUR_COLOR_COLUMN}\n1,{FUR_COLORS[0]}\n2,\n",
        encoding=FILE_ENCODING,
    )

    rows = census.read_csv(path)

    assert rows == [
        {OTHER_COLUMN: "1", FUR_COLOR_COLUMN: FUR_COLORS[0]},
        {OTHER_COLUMN: "2", FUR_COLOR_COLUMN: ""},
    ]


def test_count_by_fur_color_counts_each_colour() -> None:
    gray, cinnamon, black = FUR_COLORS
    rows = [
        _row(gray),
        _row(gray),
        _row(cinnamon),
        _row(black),
        _row(black),
        _row(black),
    ]

    counts = census.count_by_fur_color(rows)

    assert counts == {gray: 2, cinnamon: 1, black: 3}


def test_count_by_fur_color_ignores_blank_and_unknown_colours() -> None:
    rows = [_row(""), _row("White"), _row(FUR_COLORS[0].lower()), {OTHER_COLUMN: "1"}]

    counts = census.count_by_fur_color(rows)

    assert sum(counts.values()) == 0


def test_count_by_fur_color_includes_zero_counts_in_colour_order() -> None:
    counts = census.count_by_fur_color([_row(FUR_COLORS[1])])

    assert list(counts.items()) == [
        (FUR_COLORS[0], 0),
        (FUR_COLORS[1], 1),
        (FUR_COLORS[2], 0),
    ]


def test_count_by_fur_color_uses_given_colours() -> None:
    counts = census.count_by_fur_color([_row("White"), _row("White")], colors=["White"])

    assert counts == {"White": 2}


def test_build_summary_keeps_order_of_counts() -> None:
    counts = {"Black": 3, "Gray": 1, "Cinnamon": 2}

    assert census.build_summary(counts) == [("Black", 3), ("Gray", 1), ("Cinnamon", 2)]


def test_write_csv_writes_header_then_rows(tmp_path: pathlib.Path) -> None:
    path = tmp_path / "summary.csv"
    summary = [(FUR_COLORS[0], 5), (FUR_COLORS[1], 0)]

    census.write_csv(summary, path)

    header = ",".join(SUMMARY_COLUMNS)
    expected = f"{header}\n{FUR_COLORS[0]},5\n{FUR_COLORS[1]},0\n"
    assert path.read_bytes().decode(FILE_ENCODING).replace("\r\n", "\n") == expected

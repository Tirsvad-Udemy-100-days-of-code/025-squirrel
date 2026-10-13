"""Tests for the squirrel.cli module."""

import pathlib

import pytest

from squirrel import cli
from squirrel.constants import (
    FILE_ENCODING,
    FUR_COLOR_COLUMN,
    FUR_COLORS,
    SUMMARY_COLUMNS,
)


def _write_census(path: pathlib.Path) -> None:
    gray, cinnamon, _black = FUR_COLORS
    lines = [FUR_COLOR_COLUMN, gray, gray, cinnamon, ""]
    path.write_text("\n".join(lines) + "\n", encoding=FILE_ENCODING)


def test_main_writes_summary_file_and_returns_zero(tmp_path: pathlib.Path) -> None:
    census_path = tmp_path / "census.csv"
    summary_path = tmp_path / "summary.csv"
    _write_census(census_path)

    status = cli.main([str(census_path), str(summary_path)])

    assert status == 0
    lines = summary_path.read_text(encoding=FILE_ENCODING).splitlines()
    assert lines == [
        ",".join(SUMMARY_COLUMNS),
        f"{FUR_COLORS[0]},2",
        f"{FUR_COLORS[1]},1",
        f"{FUR_COLORS[2]},0",
    ]


def test_main_prints_one_line_per_colour(
    tmp_path: pathlib.Path, capsys: pytest.CaptureFixture[str]
) -> None:
    census_path = tmp_path / "census.csv"
    _write_census(census_path)

    cli.main([str(census_path), str(tmp_path / "summary.csv")])

    out_lines = capsys.readouterr().out.splitlines()
    assert out_lines == [
        f"{FUR_COLORS[0]}: 2",
        f"{FUR_COLORS[1]}: 1",
        f"{FUR_COLORS[2]}: 0",
    ]


def test_main_returns_2_and_writes_nothing_when_census_missing(
    tmp_path: pathlib.Path, capsys: pytest.CaptureFixture[str]
) -> None:
    missing = tmp_path / "missing.csv"
    summary_path = tmp_path / "summary.csv"

    status = cli.main([str(missing), str(summary_path)])

    captured = capsys.readouterr()
    assert status == 2
    assert not summary_path.exists()
    assert captured.err.strip() == f"Census file not found: {missing}"
    assert captured.out == ""

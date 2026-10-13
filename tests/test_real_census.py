"""Check the counts of the real 2018 Central Park census file, when present."""

import pathlib

import pytest

from squirrel import census
from squirrel.constants import DEFAULT_INPUT_PATH, FUR_COLORS

REPO_ROOT = pathlib.Path(__file__).parents[1]


def test_real_census_counts_match_published_figures() -> None:
    path = REPO_ROOT / DEFAULT_INPUT_PATH
    if not path.is_file():
        pytest.skip(f"census file not present: {path}")

    counts = census.count_by_fur_color(census.read_csv(path))

    gray, cinnamon, black = FUR_COLORS
    assert counts == {gray: 2473, cinnamon: 392, black: 103}

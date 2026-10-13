"""Tests for the squirrel.constants module."""

import ast
import pathlib
import sys

from squirrel import constants


def test_fur_colors_are_gray_cinnamon_black_in_order() -> None:
    assert constants.FUR_COLORS == ("Gray", "Cinnamon", "Black")


def test_summary_columns_are_fur_color_and_count() -> None:
    assert constants.SUMMARY_COLUMNS == ("Fur Color", "Count")


def test_default_input_path_has_census_file_name() -> None:
    assert constants.DEFAULT_INPUT_PATH.name == (
        "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
    )
    assert constants.DEFAULT_INPUT_PATH.parent == pathlib.Path("data")


def test_default_output_path_has_summary_file_name() -> None:
    assert constants.DEFAULT_OUTPUT_PATH == pathlib.Path("squirrel_count.csv")


def test_file_encoding_and_column_name_values() -> None:
    assert constants.FILE_ENCODING == "utf-8"
    assert constants.FUR_COLOR_COLUMN == "Primary Fur Color"


def test_module_imports_only_standard_library() -> None:
    source = pathlib.Path(constants.__file__).read_text(encoding="utf-8")
    imported: set[str] = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            imported.add(node.module.split(".")[0])

    assert imported <= sys.stdlib_module_names

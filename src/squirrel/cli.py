##
# @file cli.py
# @brief Command line entry point: count the squirrels and write the summary.

"""Command line entry point: count the squirrels and write the summary."""

import argparse
import pathlib
import sys
from collections.abc import Sequence

from squirrel import census
from squirrel.constants import (
    DEFAULT_INPUT_PATH,
    DEFAULT_OUTPUT_PATH,
    EXIT_INPUT_MISSING,
)


##
# @brief Build the argument parser of the command line.
# @return The parser with the optional `input` and `output` positionals.
def _build_parser() -> argparse.ArgumentParser:
    """Build the argument parser of the command line."""
    parser = argparse.ArgumentParser(
        prog="squirrel",
        description="Count the census squirrels by primary fur colour.",
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=pathlib.Path,
        default=DEFAULT_INPUT_PATH,
        help="census CSV file (default: %(default)s)",
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=pathlib.Path,
        default=DEFAULT_OUTPUT_PATH,
        help="summary CSV file to write (default: %(default)s)",
    )
    return parser


##
# @brief Run the census analysis from the command line.
# @param argv Arguments without the program name; `sys.argv` is used when None.
# @return 0 on success, 2 when the census file does not exist.
def main(argv: Sequence[str] | None = None) -> int:
    """Run the census analysis from the command line."""
    args = _build_parser().parse_args(argv)
    input_path: pathlib.Path = args.input
    output_path: pathlib.Path = args.output

    if not input_path.is_file():
        print(f"Census file not found: {input_path}", file=sys.stderr)
        return EXIT_INPUT_MISSING

    counts = census.count_by_fur_color(census.read_csv(input_path))
    summary = census.build_summary(counts)
    census.write_csv(summary, output_path)

    # print is the intended output here: the counts are shown to the participant.
    for color, count in summary:
        print(f"{color}: {count}")
    return 0

##
# @file __main__.py
# @brief Allows `python -m squirrel` to run the command line.

"""Allows `python -m squirrel` to run the command line."""

from squirrel.cli import main

if __name__ == "__main__":
    raise SystemExit(main())

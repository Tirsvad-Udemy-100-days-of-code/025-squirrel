"""Every module of the package imports only the standard library or itself."""

import ast
import pathlib
import sys

import squirrel

PACKAGE_NAME = squirrel.__name__
PACKAGE_DIR = pathlib.Path(squirrel.__file__).parent
ALLOWED = sys.stdlib_module_names | {PACKAGE_NAME}


def _imported_top_level_names(source: str) -> set[str]:
    imported: set[str] = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif (
            isinstance(node, ast.ImportFrom)
            and node.module is not None
            and node.level == 0
        ):
            imported.add(node.module.split(".")[0])
    return imported


def test_package_has_modules_to_check() -> None:
    assert list(PACKAGE_DIR.glob("*.py"))


def test_every_module_imports_only_standard_library_or_squirrel() -> None:
    offenders: dict[str, set[str]] = {}
    for module in PACKAGE_DIR.rglob("*.py"):
        source = module.read_text(encoding="utf-8")
        foreign = _imported_top_level_names(source) - ALLOWED
        if foreign:
            offenders[module.name] = foreign

    assert offenders == {}

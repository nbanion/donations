"""General project utilities.
"""
import pathlib


# The project root directory.
ROOT = pathlib.Path(__file__, "..", "..").resolve()


# Standard project directory paths.
PATHS = {
    "root": ROOT,
    "data": ROOT / "data",
    "raw": ROOT / "data" / "raw",
}

"""Utilities for working with raw data.
"""
import pandas as pd
import re
from src import utils
import zipfile


# Path to the zipped raw data download.
PATH = utils.PATHS["raw"] / "io.zip"


def donations(*args, **kwargs):
    """Read raw donation data.

    Args:
        args: Positional arguments for ``pandas.read_csv``.
        kwargs: Keyword arguments for ``pandas.read_csv``.

    Returns:
        Raw donation data.

    """
    io = zipfile.ZipFile(PATH)
    with io.open("Donations.csv") as f:
        return (pd.read_csv(f, *args, **kwargs)
                  .rename(columns=snake_case))


def snake_case(string):
    """Convert a string to snake case.

    This function replaces consecutive non-alphanumeric characters with a single
    underscore, and it replaces uppercase letters with lowercase letters.

    For example, "Hello, world!" becomes "hello_world_"

    Args:
        string (str): A string to convert.

    Returns:
        str: A converted string.
    """
    return re.sub("[^a-z0-9]+", "_", string.lower())

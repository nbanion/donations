"""Utilities for working with raw data.
"""
import pandas as pd
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
        return pd.read_csv(f, *args, **kwargs)

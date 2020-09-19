from src import utils


def test_paths():
    for path in utils.PATHS.values():
        assert path.exists()

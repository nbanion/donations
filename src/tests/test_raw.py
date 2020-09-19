from src import raw


def test_snake_case():
    assert raw.snake_case("Hello, world!") == "hello_world_"

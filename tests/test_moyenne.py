from src.moyenne import moyenne


def test_moyenne_simple():
    assert moyenne([10, 12, 14]) == 12

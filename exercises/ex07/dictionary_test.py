"""Dictionary tests!"""
__author__ = "730463838"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_empty() -> None:
    """Look through empty dict using invert."""
    test_list = {}
    assert invert(test_list) == {}


def test_one_element() -> None:
    """Look through one item dict using invert."""
    test_list: dict[str, str] = {"a": "c"}
    assert invert(test_list) == {"c": "a"}


def test_many() -> None:
    """Look through multiple item dict using invert."""
    test_list: dict[str, str] = {"a": "c", "b": "r"}
    assert invert(test_list) == {"c": "a", "r": "b"}


def test_alot() -> None:
    """Look through filled dict using favorite color."""
    test_list = {"marc": "yellow", "brian": "yellow", "paul": "green", "gale": "green"}
    assert favorite_color(test_list) == "yellow"


def test_one_element_1() -> None:
    """Look through one item dict using favorite color."""
    test_list: dict[str, str] = {"marc": "yellow"}
    assert favorite_color(test_list) == "yellow"


def test_many_1() -> None:
    """Look through multiple item dict using favorite color."""
    test_list: dict[str, str] = {"marc": "yellow", "brian": "yellow", "paul": "green"}
    assert favorite_color(test_list) == "yellow"


def test_empty_2() -> None:
    """Look through empty list using count."""
    test_list = []
    assert count(test_list) == {}


def test_many_2() -> None:
    """Look through multiple item list using count."""
    test_list: list[str] = ["pie"]
    assert count(test_list) == {"pie": 1}


def test_one_2() -> None:
    """Look through list one item list using count."""
    test_list: list[str] = ["pie", "water", "water", "water"]
    assert count(test_list) == {"pie": 1, "water": 3}
"""Utils test!"""
__author__ = "730463838"

from exercises.ex05.utils import only_evens, concat, sub


def test_empty() -> None:
    """Look through empty list using only_evens."""
    assert only_evens([]) == []  


def test_one_element() -> None:
    """Look through one item list using only_evens."""
    test_list: list[int] = [4]
    assert only_evens(test_list) == [4]


def test_many() -> None:
    """Look through multiple item list using only_evens."""
    test_list: list[int] = [1, 2, 3, 4]
    assert only_evens(test_list) == [2, 4]


def test_empty_1() -> None:
    """Look through empty lists using concat."""
    assert concat([], []) == []


def test_one_element_1() -> None:
    """Look through one item lists using concat."""
    test_list: list[int] = [3]
    test_list_2: list[int] = [4]
    assert concat(test_list, test_list_2) == [3, 4]


def test_many_1() -> None:
    """Look through multiple item lists using concat."""
    test_list: list[int] = [1, 2, 3]
    test_list_2: list[int] = [4, 5, 6]
    assert concat(test_list, test_list_2) == [1, 2, 3, 4, 5, 6]


def test_empty_2() -> None:
    """Look through empty list using sub."""
    test_list = []
    assert sub(test_list, 1, 2) == []


def test_many_2() -> None:
    """Look through multiple item list using sub."""
    test_list: list[int] = [1, 2, 3]
    assert sub(test_list, 0, 1) == [1]


def test_many_with_negatives() -> None:
    """Look through list with neg items list using sub."""
    test_list: list[int] = [1, -2, 1, 2, 3]
    assert sub(test_list, 2, 4) == [1, 2]
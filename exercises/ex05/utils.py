"""Utils!"""
__author__ = "730463838"


def only_evens(integers: list[int]) -> list[int]:
    """Given a list if ints, return even ints."""
    empty_list = []
    for idx in range(0, len(integers)):
        if integers[idx] % 2 == 0:
            empty_list.append(integers[idx])
    return empty_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given two list of ints, concat lists."""
    empty_list = []
    for idx in range(0, len(list_1)):
        empty_list.append(list_1[idx])
    for idx in range(0, len(list_2)):
        empty_list.append(list_2[idx])
    return empty_list


def sub(list_ints: list[int], idx_0: int, idx_last: int) -> list[int]:
    """Given list of ints, return first and last index."""
    if list_ints == []:
        return []
    if idx_0 >= len(list_ints):
        return []
    if idx_last <= 0:
        return []
    if idx_0 < 0:
        idx_0 = 0
    if idx_last > len(list_ints):
        idx_last = len(list_ints)
    empty_list = []
    for idx in range(idx_0, idx_last):
        empty_list.append(list_ints[idx])
    return empty_list
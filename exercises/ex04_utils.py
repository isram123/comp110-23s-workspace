"""EX04 - 'list Utility Functions!"""
__author__ = "730463838"


def all(list_int: list[int], number: int) -> bool:
    """Give a list of ints and an int return a bool."""
    i = 0
    if len(list_int) == 0:
        return False
    while i < len(list_int): 
        if list_int[i] == number:
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Given a list of ints return the max."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    high: int = -1000000000000000
    while idx < len(input):
        if (input[idx] > high):
            #  update high # to be our value of our current max
            high = input[idx]
        idx += 1
    return (high)


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given a list of ints return the max."""
    i = 0
    if len(list_1) != len(list_2):
        return False
    while i < len(list_1): 
        if list_1[i] == list_2[i]:
            i += 1
        else:
            return False
    return True

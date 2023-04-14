"""Dictionary!"""
__author__ = "730463838"


def invert(invert_dict: dict[str, str]) -> dict[str, str]:
    """Given a dict of ints, intvert the dict."""
    inv_dict: dict[str, str] = {}
    for elem in invert_dict:
        if invert_dict[elem] in inv_dict:
            raise KeyError
        inv_dict[invert_dict[elem]] = elem
    return inv_dict
    

def favorite_color(fc_dict: dict[str, str]) -> str:
    """Given a dict of strings, return most frequent string."""
    number: dict[str, int] = {}
    biggest: int = 0
    color: str = ""
    for item in fc_dict:
        if fc_dict[item] in number:
            number[fc_dict[item]] += 1
        else: 
            number[fc_dict[item]] = 1
    for elem in number:
        if number[elem] > biggest:
            biggest = number[elem]
            color: str = elem
    return color


def count(count_list: list[str]) -> dict[str, int]: 
    """Given a list of strings, and counnt."""
    result_dict: dict[str, int] = {}
    for values in count_list:
        if values in result_dict:
            result_dict[values] += 1 
        else: 
            result_dict[values] = 1
    return result_dict
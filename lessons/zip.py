"""Challenge question"""
___author___ = "740363838"

def zip(key: list[str], value: list[int]) -> dict[str, int]:
    dict_list: dict[str, int] = {}
    if len(key) != len(value) or len(value) == 0 or len(key) == 0:
        return dict_list
    idx: int = 0 
    while idx < len(key):
        dict_list[key[idx]] = value[idx]
        idx += 1
    return dict_list 
    

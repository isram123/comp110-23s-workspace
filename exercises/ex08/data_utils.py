"""EX08 - Data Wrangling”!"""
__author__ = "730463838"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table under a cerain header."""
    result: list[str] = [] 
    #step through table 
    for row in table:
    #save every value undery key "header"
        result.append(row[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column header."""
    result: dict[str, list[str]] = {}
    #loop through kets of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row: 
    #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result

def head(name: dict[str, list[str]], data_cols: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first rows of data for each column."""
    result: dict[str, list[str]] = {}
    for keys in name:
    #make an entry with "key" as the key and firdt two elements a lsit of values
        sub_list = []
        idx: int = 0
        while idx < data_cols and idx < len(name[keys]):
            sub_list.append(name[keys][idx])
            idx += 1
        result[keys] = sub_list
    return result

def select(selected_data: dict[str, list[str]], names: list[str]) ->dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for keys in names:
        if keys in selected_data:
            result[keys] = selected_data[keys]
    return result

def concat(table: dict[str, list[str]], table0: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for keys in table:
        result[keys] = table[keys]
    for keys in table0:
        if keys in result:
            result[keys] += table0[keys]
        else:
            result[keys] = table0[keys]
    return result

def count(values: list[str]) -> dict[str, int]:
    """Given a list produce a dict, where each key is a unique value, with the given count."""
    result: dict[str, int] = {}
    for keys in values:
        if keys in result:
            result[keys] += 1
        else:
            result[keys] = 1
    return result



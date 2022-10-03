import json
from pprint import pprint


def get_data_from_json_file(name_of_json_file: str) -> dict:
    """
    get data from json file
    """
    with open(name_of_json_file, 'r', encoding='utf-8') as f:
        data_from_json_file = json.load(f)
        return data_from_json_file


def get_symbols(data_from_json_file) -> dict:
    """
    get symbols in data from json file
    """
    symbols = data_from_json_file.get('symbols')
    return symbols


def check_correct_currency(symbols) -> bool:
    """
    checking the correctness of the currency with file
    """
    currency_of_user = input("Enter your currency: ")
    upper_currency_of_user = currency_of_user.upper()
    if [key for key in symbols if key == upper_currency_of_user]:
        return True
    if [key for key in symbols if key != upper_currency_of_user]:
        raise ValueError("Incorrect currency!")


pprint(check_correct_currency(get_symbols(get_data_from_json_file("symbols.json"))))

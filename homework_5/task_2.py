from typing import Any
import requests
import task_1_url


# створіть функцію для перевірки, що за замовчуванням число не менше 0 та не
# більше 100 (потрібно, щоб верхня та нижня межа могли налаштовуватися)
def is_valid_number(number_to_check: int, lower_limit: int,
                    upper_bound: int) -> bool:
    """
    checks that the number is not less than the lower limit
    and not greater than the upper bound
    :param number_to_check: int
    :param lower_limit: int
    :param upper_bound: int
    :return: bool
    """
    if lower_limit < number_to_check < upper_bound:
        return True
    else:
        return False


# створіть функцію для перевірки, що отриманий аргумент є числом (інт)

def is_element_int(element_to_check: Any) -> bool:
    """
    checks if the type of the argument is a number (int)
    :param element_to_check: Any
    :return: bool
    """
    if type(element_to_check) == int:
        return True
    return False


# створіть функцію, що отримує урл та віддає json, отриманий через цей урл
# (валідувати не потрібно, ми поки що працюємо з даними, вважаючи,
# що вони валідні)

def get_data(url: str = None) -> dict:
    """
    get data from given url
    :param url: str
    :return: dict
    """
    response = requests.get(url)
    data = response.json()

    return data


# створити функцію, яка приймає стрічку, і має її повернути, враховуючи , що ця
# стрічка має бути довжиною не більше 150 символів (може регулюватися через
# передачу аргумента функції), а якщо отримана стрічка буде довшою за 150
# символів, то стрічка має бути обрізана до 150 символів, причому останні
# три символи мають бути ... (трьома крапками)

def is_valid_length(string: str, length: int = 150):
    """
    checks the length of a string. If the string is less than 150 characters,
    it returns a string.
    If more - returns 150 characters of the string + "...".
    :param string: str
    :param length: int = 150
    :return: str
    """
    if len(string) <= length:
        return string
    if len(string) > length:
        return f"{string[:150]}..."


# написати функцію, котра дозаписує (режим "а") в файл певні текстові дані

def append_data_to_the_file(path_to_file: str = 'test_file.txt', data=''):
    """
    append (mode "a") to a file of full text data
    :param path_to_file: str: 'test_file.txt'
    :param data: str
    :return: some data in file
    """
    with open(path_to_file, 'a') as file:
        file.write(data)


if __name__ == '__main__':
    assert is_valid_number(60, 0, 100)
    assert is_valid_number(120, 0, 100) is False
    assert is_element_int(28)
    assert is_element_int('some') is False
    assert is_element_int(7.99) is False
    assert get_data(task_1_url.URL)
    assert is_valid_length("fggggggggggggggggggggggggggggggggggggggggggggggggg"
                           "ggggggggggggggggggggggggggggggggggggggggggggggggg"
                           "ggggggggggggggggggggggggggggggggggggggggggggggggg"
                           "ggttt")
    assert is_valid_length("fggggggggggggggggggggggggggggggggggggggggggggggggg"
                           "ggggggggggggggggggggggggggggggggggggggggggggggggg"
                           "ggggggggggggggggggggggggggggggggggggggggggggggggg"
                           "gg")

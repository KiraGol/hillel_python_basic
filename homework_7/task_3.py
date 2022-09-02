# 3. Даний перелік значень. Напишіть функцію яка поверне словник,
# де кожен ключ - це індекс листа, а значення листа – це значення ключа:
#   Input:
#   ['a', 'b', 'c', 'd', 'e']
#   Output
#   {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

input = ['a', 'b', 'c', 'd', 'e']


def from_list_to_dict(income_list: list) -> dict:
    """
    converts the list to a dictionary, where key is the index of the list
    value and value is the value in the list.
    :param income_list: list
    :return: dict
    """
    new_dict = dict((index, value) for index, value in enumerate(income_list))
    return new_dict


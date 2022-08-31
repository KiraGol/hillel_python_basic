# 1.Дано два кортежі, напишіть функцію яка з'єднає їх в один dict:
#
#   Input:
#
#     coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
#     code = ('BTC', 'ETH', 'XRP', 'LTC')
#   Output:
#
#     {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def from_two_tuples_to_dict(first_tuple: tuple, second_tuple: tuple) -> dict:
    """
    return dict from two tuples
    :param second_tuple: tuple
    :param first_tuple: tuple
    :return: dict
    """
    new_dict = dict(zip(first_tuple, second_tuple))
    return new_dict


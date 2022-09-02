# 4. Написати функцію, яка повертає поточний час. І обернути її на декоратор
# який відрахує 3 секунди.
#   Приклад:
#   >>> what_time_is_it_now()
#   3
#   2
#   1
#   '16:21'
#   Повернути час допоможе метод time.strftime з аргументом '%H:%M'
from time import strftime
import time


def timer(function_to_decorate):
    """

    :param function_to_decorate:
    :return:
    """
    def inner(number_of_seconds_plus_one: int = 4):
        for sec in range(3):
            time.sleep(1)
            number_of_seconds_plus_one -= 1
            print(number_of_seconds_plus_one)
        return function_to_decorate()

    return inner()


@timer
def what_time_is_it_now():
    """
    displays the current time on the clock in the format %H:%M
    :return:
    """
    current_time = strftime('%H:%M')
    return current_time


print(what_time_is_it_now)

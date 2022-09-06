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
    counts seconds with counter output
    """
    def inner(*args, **kwargs):
        countdown_start = 4
        for sec in range(3):
            time.sleep(1)
            countdown_start -= 1
            print(countdown_start)
        return function_to_decorate(*args, **kwargs)

    return inner()


@timer
def what_time_is_it_now():
    """
    displays the current time on the clock in the format %H:%M
    :return: str
    """
    current_time = strftime('%H:%M')
    return current_time


if __name__ == '__main__':
    print(what_time_is_it_now)

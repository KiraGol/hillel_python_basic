# 1. Формат українських номерів: ВН1010НС чи АА1010АА
#
#   На введення програма отримує рядок, у відповідь має повернути чи є рядок автомобільним номером чи ні.
#   * Дод. Повинна повернути регіон (має знати регіони 2004 та 2013 рр.)
#       Повинна однаково сприймати AI – англійський та АІ – український варіанти.
#       (Для BI, AI, IA і т.д.)
import re


def find_auto_code():
    """finds car number"""
    user_input = input("Enter auto code: ")
    match = re.search(r'^[AKBCEHIMOPTXАКВСЕНІМОРТХ]{2}\d{4}(?<!0{4})[AKBCEHIMOPTXАКВСЕНІМОРТХ]{2}$', user_input)
    if match:
        return 'It is car number'


print(find_auto_code())
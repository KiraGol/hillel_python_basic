import calendar


def is_valid_user_date_format(value) -> bool:
    """Expect date in format data in str format %Y-%m-%d"""
    if not value:
        return False

    try:
        year, month, day = [int(value) for value in value.split('-')]
    except Exception:
        return False

    is_valid_year = False
    is_valid_month = False
    is_valid_day = False

    if 1919 < year < 9999:  # https://www.in2013dollars.com/us/inflation/1919
        is_valid_year = True

    if 0 < month < 13:
        is_valid_month = True

    if all([calendar.isleap(year), month == 2, (0 < day <= 29)]):
        is_valid_day = True
    elif all([calendar.isleap(year), month == 2, (0 < day <= 28)]):
        is_valid_day = True
    elif month in [1, 3, 5, 7, 8, 10, 12] and (0 < day <= 31):
        is_valid_day = True
    elif month in [4, 6, 9, 11] and 0 < day <= 30:
        is_valid_day = True

    return all([is_valid_year, is_valid_month, is_valid_day])

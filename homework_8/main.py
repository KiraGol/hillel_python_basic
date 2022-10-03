import sys

import lib
import validators as val


def get_data_from_user_cli() -> list:
    """data from CLI"""
    return sys.argv[1:]


def get_date_for_currency_rate() -> str:
    user_data = get_data_from_user_cli()
    day_today = lib.get_current_date()
    if user_data:
        is_valid_date_format = val.is_valid_user_date_format(*user_data)
        if is_valid_date_format:
            date = lib.datetime(*[int(value) for value in user_data[0].split('-')])
        else:
            date = day_today
    else:
        date = day_today

    if date <= day_today:
        return date.strftime('%Y-%m-%d')

    return day_today.strftime('%Y-%m-%d')


if __name__ == '__main__':
    pass

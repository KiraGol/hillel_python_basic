import datetime
from pprint import pprint

import requests


def do_list_with_date() -> list:
    """
    get list with dates that user entered
    """
    date_today = datetime.datetime.now()
    start_date = input("Enter start date: ")
    start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    dates_list = [start_date_obj]
    while start_date_obj < date_today:
        start_date_obj += datetime.timedelta(days=1)
        dates_list.append(start_date_obj)
    return dates_list


def get_data_from_list_of_dates(dates_list) -> list:
    """
    get data with currency conversion results
    """
    data = []
    URL = "https://api.exchangerate.host/convert"
    currency_from = input("Enter currency from: ")
    currency_to = input("Enter currency to: ")
    amount = input("Enter amount: ")
    for date in dates_list:
        res = requests.get(URL,
                           params={"from": currency_from, "to": currency_to,
                                   "amount": amount, "date": date})
        data.append(res.json())
    return data


# def get_parameters_from_data(data):
#     new = []
#     for param in data:
#         new = param['date'], param['info']['rate'], param['query']['amount'], param['query']['from'], param['query']['to'], param['result']
#     return new

# print(get_parameters_from_data(get_data_from_list_of_dates(do_list_with_date())))
pprint(get_data_from_list_of_dates(do_list_with_date()))



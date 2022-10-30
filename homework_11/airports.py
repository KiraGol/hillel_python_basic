import csv
import re


class AirportNotFoundError(Exception):
    def __init__(self, message="Airport not found"):
        self.message = message
        super().__init__(self.message)
        

class CountryNotFoundError(Exception):
    def __init__(self, message="Country not found"):
        self.message = message
        super().__init__(self.message)

class NoOptionsFoundError(Exception):
    def __init__(self, message="No Options Found"):
        self.message = message
        super().__init__(self.message)

class MultipleOptionsError(Exception):
    def __init__(self, message="Only one option allowed"):
        self.message = message
        super().__init__(self.message)


def get_data_from_csv_file(name_of_csv_file: str):
    """
    get data from json file
    """
    with open(name_of_csv_file, encoding='utf-8') as f:
        airports = []
        reader = csv.reader(f)
        for row in reader:
            airports.append(row)
        return airports


def find_airport_with_iata_code(airports):
    user_input = input("Enter iata code of airport: ")
    upper_user_input = user_input.upper()
    for airport in airports:
        for elem in airport:
            if upper_user_input == elem:
                return airport
    if re.search(r'\s', user_input) is True:
        raise MultipleOptionsError("Only one option allowed")
    if user_input == None:
        raise NoOptionsFoundError("No Options Found")
    else:
        raise AirportNotFoundError("Airport not found")


def find_airport_with_country(airports):
    list_of_airports = []
    user_input = input("Enter country of airport: ")
    upper_user_input = user_input.upper()
    for airport in airports:
        for elem in airport:
            if upper_user_input == elem:
                list_of_airports.append(airport)
        return list_of_airports
    if re.search(r'\s', user_input) is True:
        raise MultipleOptionsError("Only one option allowed")
    if user_input == None:
        raise NoOptionsFoundError("No Options Found")
    else:
        raise CountryNotFoundError("Country not found")


def find_airport_with_name(airports):
    list_of_airports_with_names = []
    user_input = str(input("Enter name or part of name of the airport: "))
    for airport in airports:
        for elem in airport:
            if user_input in elem:
                list_of_airports_with_names.append(elem)
    return list_of_airports_with_names



print(find_airport_with_iata_code(get_data_from_csv_file('airport-codes_csv.csv')))

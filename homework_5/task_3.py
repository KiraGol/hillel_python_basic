import datetime
from pprint import pprint
import task_1_url
import SMILES
import requests


# створити функцію, котра приймає урл (та опційний параметр bd булевого формату
# для завдання 4), і очікує там словник з ключами, описаними в завданні 1
# в функції перевіряється, що якщо в учня бали від 90 до 100, учень має
# винагороди, його вік від 9 до 18 років, то формуємо стрічку типу:
#
# "[Запит від {}] Учень {імя} {смайл} є відмінником, його бал {бал},
# відзначимо, що {примітки}"

def get_data(url: str = None) -> dict:
    """
    get data from given url
    :param url: str
    :return: dict
    """
    response = requests.get(url)
    data = response.json()
    return data


def take_google_data(google_url: str) -> dict:
    """
    get data from given url
    :param google_url: str
    :return: dict
    """
    google_data = get_data(google_url)['data']
    return google_data


def validate_score_age_rewards(google_data: dict, score=90, min_age=9,
                               max_age=18, has_rewards=True) -> list:
    """
    verifies that the student scores between 90 and 100 points, is between
    9 and 18 years old, and that the student has awards. Returns a dictionary.
    :param google_data: dict
    :param score: int (90)
    :param min_age: int (9)
    :param max_age: int (18)
    :param has_rewards: bool (True)
    :return: dict
    """
    top_score = []
    for dictionary in google_data:
        if dictionary['score'] >= score and \
                min_age < dictionary['age'] < max_age and \
                dictionary['has_rewards'] == has_rewards:
            top_score.append(dictionary)
    return top_score


def display_top_score_message(top_score: list, db: bool):
    """
    add information in string about top student score
    :param db: bool
    :param top_score: list
    :return: list
    """
    now = datetime.datetime.now().date()
    for item in top_score:
        if db is True:
            item['notes'] = f"[Запит від {now}] Учень {item['name']} " \
                          f"{SMILES.SMILE_null} є відмінником, його бал " \
                          f"{item['score']}."
        else:
            item['message'] = f"[Запит від {now}] Учень {item['name']} " \
                              f"{SMILES.SMILE_1} є відмінником, його бал " \
                              f"{item['score']}, відзначимо, що " \
                              f"{item['notes']}"
    return top_score


def validate_length_of_top_score_message(top_score: list, length: int = 150):
    """
    checks the length of a string
    :param top_score: list
    :param length: int (150)
    :return: str
    """
    message_150 = " "
    for item in top_score:
        if len(item['message']) > length:
            message_150 = item['message'][:150]
        else:
            message_150 = item['message']
    return message_150


def append_message_in_file(file_name='top_score_file.txt', message_150=''):
    """
    append message about top score in file with creating file
    :param file_name: 'top_score_file.txt'
    :param message_150: str
    :return: message about top score in file
    """
    with open(file_name, 'a+') as file:
        file.write(message_150)


# if __name__ == '__main__':
#     pprint(display_top_score_message(validate_score_age_rewards(take_google_data(task_1_url.URL)), False))

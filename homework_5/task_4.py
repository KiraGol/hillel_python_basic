from pprint import pprint
import pymongo
import config
import task_3
from homework_5 import task_1_url

# токен пропишіть як констнанту в окремому файлі конфігів,
# назву бд та колекції також тримати в файлі конфігів
#
# написати функцію, яка підєднується за токеном до бази даних, створює базу
# даних, колекцію.
#
# доробити функцію з завдання 3: якщо bd True, то ми формуємо ту ж стрічку
# (проте без смайла, можете передбачити в колекції смайлів смайл як пуста
# стрічка), і записуємо в базу даних або по одному валідні json дані, або ж
# добавляємо їх в список  і використовуємо insert_many
#
# зауважте, що ви відправляєте замість notes тест нашої стрічки до 150 символів,
# інші поля залишаються без змін
#
# id не відправляйте, нехай формується автоматично
#
#
# напишіть функцію, котра отримує всі дані з бази даних (назва бд та колекції
# у вас в конфігах)


def create_db_and_collection():
    """
    provides a connection to the database and create new db and collection
    :return: obj
    """
    db_client = pymongo.MongoClient(config.LOCALHOST)
    current_db = db_client[config.DB_CLIENT]
    collection = current_db[config.CURRENT_DB]
    return current_db, collection


def add_data_to_db(google_data: list, current_db):
    """
    add data to the collection
    :param current_db:
    :param google_data: list
    :return:
    """
    adding_to_db_data = current_db.insert_many(google_data)
    return adding_to_db_data


def add_notes_about_top_score(top_score: dict, collection):
    """
    adds one entry to the collection
    :param top_score: dict
    :param collection:
    :return:
    """
    adding_one_dict_in_db = collection.insert_one(top_score)
    return adding_one_dict_in_db


# if __name__ == '__main__':
#     pprint(task_3.display_top_score_message(task_3.validate_score_age_rewards(task_3.take_google_data(task_1_url.URL)), True))
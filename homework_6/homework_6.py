# ВСЕ РОБІТЬ ФУНКЦІЯМИ, УРЛИ ЗАДАВАЙТЕ В КОНСТАНТАХ
# створіть функцію, котра приймає по урл дані по апі
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid
# =47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv)
# по коду використовуйте метод format для підстановки в урл необхідного місця
#
# список розсилки
# https://script.google.com/macros/s/AKfycby3Fp-J3N0OM5UZhg9SHgIusHBMC2kWVXSOVsP26smPTaYS_4IiOT7sVx7ZWyC3XsVW7g/exec
# зауважте, що до вас прийдуть дані в форматі
#
# {"data":[{"name":"Kolja","e_mail":"test_hillel_api_mailing@ukr.net","city"
# :"Kyiv"},{"name":"Oleg","e_mail":"kjhgfgjg","city":"Lviv"}]}
# як ви бачите, електронна пошта не всюди валідна
#
# добавте перевірку даних електронної пошти (наявність @, є текст справа і
# зліва від @)
#
# **ЯКЩО ХОЧЕТЕ ОТРИМАТИ 5 БАЛІВ, використайте
# https://validators.readthedocs.io/en/latest/
#
# загальна система роботи
# створюєте функцію для отримання даних по апі
# отримуєте список отримувачів розсилки, дана функція повертає список діктів
# (ви вже знайомі з тим, як це працює)
#
# вищенаписану функцію декоруєте. робота декоратора заключається в тому,
# що аналізується ретурн функції, витягується з нього імейл, перевіряється на
# валідність (там точно буде імейл з лекції, доступ у вас є), і, якщо імейл
# валідний, то на нього відправляється поточна погода у вибраному місті
# (міста будуть валідними, відповідь ви точно отримаєте)
#
# **ДЛЯ ОТРИМАННЯ 5 БАЛІВ ЗАДЕКОРУЙТЕ функцію, котра у вас буде стукатися з за
# прогнозом погоди, декоратором from functools import lru_cache (гугл в
# допомогу) - лаконічний матеріал тут
# https://www.youtube.com/watch?v=K0Q5twtYxWY
#
# цей декоратор зекономить багато часу на однакових запитах до серверу, в межах
# локального запуску (буде досить багато запитів на одні й ті ж міста).
# Якщо що - я на звязку
#
# поточна погода відправляється з описом міста, дати
# (модуль datetime.datetime.now()), температури, вологості, інші дані на ваш
# вибір
#
# на основі https://openweathermap.org/weather-conditions#:~:text=Night%20icon
# -,Description,-01d.png вставте смайли з https://unicode-table.com/en/emoji/
# (в залежності від текстовки в блоці погоди можете зробити словник, де ключ -
# це текстовка, а смайл - в форматі юнікода, або ж дивитися на ID погоди
# (наприклад, коди від 500 до 531 - дощ)
#
# **ЗАВДАННЯ НА 5 БАЛІВ
# список отримувачів буде мати дублі. напишіть декоратор, котрий буде
# фільтрувати отримані дані від функції, що отримує список отримувачів
# розсилки, в результаті якого будуть відсіяні всі дублікати (тобто, всі три
# поля name e_mail city будуть ідентичні). в результаті дана функція матиме
# два декоратора, верхній відповідатиме за відправку імейлів, а нижній за
# фільтрацію отриманих даних на предмет унікальності (наприклад, завдяки
# перетворенню дікта на стрічку та використання сета для зберігання цих
# тепплейтів для порівняння))
#
# напишуть тести для функції, що перевіряє імейли (валідний- невалідний імейл,
# ретурн ф тру або фолсі), тести для функції, що робить запити в інтернет
# (формат словника, а також передачу неіснуючого міста (відповідь має бути
# {"cod":"404","message":"city not found"}, а також статус код 404
# (зверніться до відповіді
# res = requests.get('https:/.... print(res.json()) print(res.status_code))
import datetime
import functools

import requests
import validators


def check_the_weather_in_the_city() -> dict:
    """
    displays weather data for the specified city
    """
    URL_WEATHER = "https://api.openweathermap.org/data/2.5/weather?q=" \
                  "{city_name}&appid=47503e85fabbabc93cff28c52398ae97" \
                  "&units=metric".format(city_name=input("Enter the city in "
                                                         "which you want to "
                                                         "know the weather in "
                                                         "small letters, for "
                                                         "example, odesa, "
                                                         "kyiv, lviv: "))
    response = requests.get(URL_WEATHER)
    data_weather = response.json()
    return data_weather


def get_data_with_emails() -> dict:
    """
    get emails from given url
    """
    URL_EMAILS = "https://script.google.com/macros/s/AKfycby3Fp-J3N0OM5UZhg" \
                 "9SHgIusHBMC2kWVXSOVsP26smPTaYS_4IiOT7sVx7ZWyC3XsVW7g/exec"
    response = requests.get(URL_EMAILS)
    data_with_emails = response.json()
    return data_with_emails


def get_list_from_data_emails(data_with_emails: dict) -> list:
    """
    get list from data with emails
    """
    for key, value in data_with_emails.items():
        users_data = value
        return users_data


def validate_emails(users_data: list) -> list:
    real_emails = []
    for elem in users_data:
        if validators.email(elem['e_mail']) is True:
            real_emails.append(elem)
    return real_emails


def find_unique_emails(users_data):
    emails_list = []
    for elem in users_data:
        emails_list.append(elem['e_mail'])
    unique_emails = set(emails_list)
    return unique_emails


@functools.cache
def send_mail(to_sending, set_for_sending):
    def inner_(func):
        def wrapper2(*args, **kwargs):
            result = func(*args, **kwargs)
            if to_sending:
                text_to_send = f'{args}, {kwargs}'
                from homework_6 import mail
                mail.mail_sender(set_for_sending, data_to_send=text_to_send)
            data = {
                'time': datetime.datetime.now(),
                'result': result,
            }
            return data

        return wrapper2

    return inner_


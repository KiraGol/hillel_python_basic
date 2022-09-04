# 2. У додатку є json файл. Написати програму, яка прочитає його та порахує
# загальну тривалість всіх треків в альбомі.
#   Базовий кейс - поверне кількість секунд.
#   * Дод. ускладнення повернути у вигляді рядка години:хвилини:секунди,
#   прим. 0:41:39

import json
import time


def get_data_from_json_file(name_of_json_file: str) -> dict:
    """
    get data from json file
    :param name_of_json_file: str
    :return: dict
    """
    with open(name_of_json_file, 'r', encoding='utf-8') as f:
        data_from_json_file = json.load(f)
        return data_from_json_file


def get_duration_from_tracks(data_from_json_file: dict) -> int:
    """
    returns the number of seconds of all tracks.
    :param data_from_json_file: dict
    :return: int
    """
    for key, value in data_from_json_file.items():
        new_data = value
        tracks = new_data.get('tracks')
        for k, v in tracks.items():
            new_new_data = v
            duration = sum(int(n['duration']) for n in new_new_data)
            return duration


def conversion_to_time_format(duration: int) -> str:
    """
    converts the number of seconds to the time format "hours:minutes:seconds"
    :param duration: int
    :return: str
    """
    time_format = time.strftime("%H:%M:%S", time.gmtime(duration))
    return time_format


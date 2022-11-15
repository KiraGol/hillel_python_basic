import json
import time

def get_data_from_json_file(name_of_json_file: str) -> dict:
    """
    get data from json file
    """
    with open(name_of_json_file, 'r', encoding='utf-8') as f:
        data_from_json_file = json.load(f)
        return data_from_json_file


def get_duration_from_tracks(data_from_json_file: dict) -> int:
    """
    returns the number of seconds of all tracks.
    """
    for key, value in data_from_json_file.items():
        album = value
        tracks = album.get('tracks')
        for k, v in tracks.items():
            value_in_tracks = v
            duration = sum(int(n['duration']) for n in value_in_tracks)
            return duration


def conversion_to_time_format(duration: int) -> str:
    """
    converts the number of seconds to the time format "hours:minutes:seconds"
    """
    time_format = time.strftime("%H:%M:%S", time.gmtime(duration))
    return time_format

print(conversion_to_time_format(get_duration_from_tracks(get_data_from_json_file("acdc.json"))))
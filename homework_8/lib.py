import datetime
from datetime import datetime


def get_current_date() -> datetime.date:
    """Return current data"""
    date_today = datetime.now()
    return date_today


def get_current_date_str_format() -> str:
    """Return current data in '%Y-%m-%d' format"""
    date_today = datetime.now().strftime('%Y-%m-%d')
    return date_today

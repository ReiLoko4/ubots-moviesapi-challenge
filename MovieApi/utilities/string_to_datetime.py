from datetime import datetime


def string_to_datetime(datetime_str: str) -> datetime:
    return datetime.fromisoformat(datetime_str)

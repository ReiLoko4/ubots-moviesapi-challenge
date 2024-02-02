from datetime import time


def string_to_time(time_str: str) -> time:
    return time.fromisoformat(time_str)

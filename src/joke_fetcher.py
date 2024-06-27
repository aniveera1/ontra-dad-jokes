from typing import Optional

import requests

from config import HEADERS


def validate_joke_args(
    interval: int, duration: int, total: Optional[int], search: Optional[str]
) -> None:
    if interval <= 0:
        raise ValueError("Error: interval must be greater than 0")
    if duration <= 0:
        raise ValueError("Error: duration must be greater than 0")
    if total is not None and total <= 0:
        raise ValueError("Error: total must be greater than 0")
    if search is not None and search == "":
        raise ValueError("Error: search term must not be empty")


def should_fetch_joke(
    duration: int, current_time: float, start_time: float, total: Optional[int], count: int
) -> bool:
    if total is not None:
        return count < total
    return current_time - start_time < duration


def fetch_joke(url: str) -> dict:
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Error: failed to fetch joke\n{response.status_code} - {response.reason}")
    return response.json()

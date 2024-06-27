from typing import Optional

import requests

from config import HEADERS


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

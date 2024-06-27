import argparse
import time
from typing import Optional

import requests

from config import DAD_JOKE_SEARCH_URL, DAD_JOKE_URL, HEADERS


def should_fetch_joke(duration: int, start_time: float, total: Optional[int], count: int) -> bool:
    if total is not None:
        return count < total
    return time.time() - start_time < duration


def fetch_joke(url: str) -> dict:
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Error: failed to fetch joke\n{response.status_code} - {response.reason}")
    return response.json()


def main(interval: int, duration: int, total: Optional[int], search: Optional[str]):
    start_time = time.time()
    count = 0
    next_page = 1

    while should_fetch_joke(duration, start_time, total, count):
        if search is not None:
            joke = fetch_joke(DAD_JOKE_SEARCH_URL.format(page=next_page, term=search))
            print(joke["results"][0]["joke"])
        else:
            joke = fetch_joke(DAD_JOKE_URL)
            print(joke["joke"])

        next_page += 1
        count += 1
        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch random dad jokes and output them to the console."
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=15,
        help="interval in seconds between each joke (default is 15 seconds)",
    )
    parser.add_argument(
        "-d",
        "--duration",
        type=int,
        default=60,
        help="duration in seconds to fetch jokes for (default is 60 seconds)",
    )
    parser.add_argument(
        "-t",
        "--total",
        type=int,
        help="total number of jokes to fetch (overrides duration, default is None)",
    )
    parser.add_argument(
        "-s",
        "--search",
        type=str,
        help="search for jokes with the given term in them (default is None)",
    )
    args = parser.parse_args()
    main(args.interval, args.duration, args.total, args.search)

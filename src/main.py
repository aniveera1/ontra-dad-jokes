import argparse
import time
from typing import Optional

import requests

DAD_JOKE_URL = "https://icanhazdadjoke.com/"


def should_fetch_joke(duration: int, start_time: float, total: Optional[int], count: int):
    if total is not None:
        return count < total
    return time.time() - start_time < duration


def main(interval: int, duration: int, total: Optional[int]):
    start_time = time.time()
    count = 0

    while should_fetch_joke(duration, start_time, total, count):
        headers = {
            "accept": "application/json",
            "User-Agent": "dad-joke-fetcher (https://github.com/aniveera1)",
        }

        response = requests.get(DAD_JOKE_URL, headers=headers)
        if response.status_code != 200:
            print(f"Error: failed to fetch joke")
            print(f"{response.status_code} - {response.reason}")
            return

        print(response.json()["joke"])

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
    args = parser.parse_args()
    main(args.interval, args.duration, args.total)

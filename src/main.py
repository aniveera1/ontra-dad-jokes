import argparse
import time
from typing import Optional

from config import DAD_JOKE_SEARCH_URL, DAD_JOKE_URL
from joke_fetcher import fetch_joke, should_fetch_joke


def main(interval: int, duration: int, total: Optional[int], search: Optional[str]):
    start_time = time.time()
    count = 0
    next_page = 1

    while should_fetch_joke(duration, time.time(), start_time, total, count):
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

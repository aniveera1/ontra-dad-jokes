import argparse
import time
from typing import Optional

from config import DAD_JOKE_SEARCH_URL, DAD_JOKE_URL
from joke_fetcher import fetch_joke, should_fetch_joke, validate_joke_args


def main(interval: int, duration: int, total: Optional[int], search: Optional[str]):
    try:
        validate_joke_args(interval, duration, total, search)
    except ValueError as e:
        print(e)
        return

    start_time = time.time()
    count = 0
    next_page = 1

    while should_fetch_joke(duration, time.time(), start_time, total, count):
        if search is not None:
            try:
                joke = fetch_joke(DAD_JOKE_SEARCH_URL.format(page=next_page, term=search))
            except Exception as e:
                print(e)
                return

            if joke["total_jokes"] == 0:
                print(f"No jokes found for search term: {search}")
                return
            if len(joke["results"]) == 0:
                print(f"No more jokes found for search term: {search}")
                return
            print(joke["results"][0]["joke"])
        else:
            try:
                joke = fetch_joke(DAD_JOKE_URL)
            except Exception as e:
                print(e)
                return

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

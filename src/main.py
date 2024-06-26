import argparse
import time

import requests

DAD_JOKE_URL = "https://icanhazdadjoke.com/"


def main(interval: int, duration: int):
    start_time = time.time()

    while time.time() - start_time < duration:
        headers = {
            "accept": "application/json",
        }

        print(requests.get(DAD_JOKE_URL, headers=headers).json()["joke"])

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
        help="duration in seconds to fetch jokes (default is 60 seconds)",
    )
    args = parser.parse_args()
    main(args.interval, args.duration)

import argparse
import time

import requests

DAD_JOKE_URL = "https://icanhazdadjoke.com/"


def main(joke_interval):
    start_time = time.time()

    while time.time() - start_time < 60:
        headers = {
            "accept": "application/json",
        }

        print(requests.get(DAD_JOKE_URL, headers=headers).json()["joke"])

        time.sleep(joke_interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch random dad jokes and output them to the console."
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=15,
        help="Time interval in seconds between each joke (default is 15 seconds).",
    )
    args = parser.parse_args()
    main(args)

import requests
import time

DAD_JOKE_URL = "https://icanhazdadjoke.com/"


def main():
    start_time = time.time()

    while time.time() - start_time < 60:
        headers = {
            "accept": "application/json",
        }

        print(requests.get(DAD_JOKE_URL, headers=headers).json()["joke"])

        time.sleep(15)


if __name__ == "__main__":
    main()

# ontra-dad-jokes
Two fish are in a tank, one turns to the other and says, "how do you drive this thing?"

## Description
- A script that uses the [icanhazdadjoke](https://icanhazdadjoke.com/api) API to fetch random dad jokes and output them to the console. By default, jokes are fetched every 15 seconds for 1 minute.

## Installation
- Create and activate a Python virtual environment.
- `make install`

## Usage
```
python src/main.py [-h] [-i INTERVAL] [-d DURATION] [-t TOTAL]

Fetch random dad jokes and output them to the console.

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        interval in seconds between each joke (default is 15 seconds)
  -d DURATION, --duration DURATION
                        duration in seconds to fetch jokes for (default is 60 seconds)
  -t TOTAL, --total TOTAL
                        total number of jokes to fetch (overrides duration, default is
                        None)
```

## License
- [MIT](https://choosealicense.com/licenses/mit/)

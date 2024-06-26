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
optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        time interval between jokes in seconds (default: 15)
  -d DURATION, --duration DURATION
                        duration in seconds to fetch jokes (default is 60
                        seconds)
  -t TOTAL, --total TOTAL
                        total number of jokes to fetch (overrides duration,
                        default is None)
```

## Future Work
- Allow users to search for jokes based on a keyword.

## Contributing
- Pull requests are welcome. Please format all code using `make fmt`.

## License
- [MIT](https://choosealicense.com/licenses/mit/)

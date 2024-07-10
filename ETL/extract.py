import sys
import requests
import config as config
from datetime import datetime, timedelta


def extract_stock_data(symbol, start_date, end_date, interval="1min"):

    url = f"https://api.twelvedata.com/time_series"
    params = {
        "symbol": symbol,
        "interval": interval,
        "apikey": config.API_KEY,
        "start_date": start_date,
        "end_date": end_date,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"API response data: {data}")

        if "values" in data:
            return data
        else:
            raise ValueError("API response does not contain values")
    else:
        raise ConnectionError(f"failed to fetch data: {response.content}")


if len(sys.argv) < 4:
    print("Usage: python extract.py <symbol> <start_date> <end_date>")
    sys.exit(1)

stock_symbol = sys.argv[1]
start_date = sys.argv[2]
end_date = sys.argv[3]

extract_stock_data(stock_symbol, start_date, end_date)

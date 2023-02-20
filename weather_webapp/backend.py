import json

import requests
"""API Requests to fetch weather and clouds data"""

API_KEY = 'd8f709eaab7a918f99b954fe1e59335e'


def get_data(place, forecast_days=1):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


def main():
    print(json.dumps(get_data(place='London', forecast_days=1), indent=2))


if __name__ == '__main__':
    main()

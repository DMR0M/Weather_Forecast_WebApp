import requests
"""API Requests to fetch weather and clouds data"""

API_KEY = 'd8f709eaab7a918f99b954fe1e59335e'


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    url_2 = "api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={APIkey}"
    response = requests.get(url)
    content = response.json()
    return content


def main():
    print(get_data(place='Tokyo'))


if __name__ == '__main__':
    main()

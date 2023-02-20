
import requests
"""API Requests to fetch weather and clouds data"""

API_KEY = 'd8f709eaab7a918f99b954fe1e59335e'


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == 'Temperature':
        filtered_data = [w_data['main']['temp'] for w_data in filtered_data]
    if kind == 'Sky':
        filtered_data = [w_data['weather'][0]['sky'] for w_data in filtered_data]
    return filtered_data


def main():
    print(get_data(place='Pasig', forecast_days=3, kind='Temperature'))


if __name__ == '__main__':
    main()

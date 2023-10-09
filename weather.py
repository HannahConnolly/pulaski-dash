import requests
import json

use_local = True


class Weather:

    def __init__(self):
        self.weather = {
            'high': 'n.a',
            'low': 'n.a',
            'rain': 'n.a'
        }
    
    def get_weather_printout(self):
        self.get_data()
        return f"High: {self.weather['high']}°  Low: {self.weather['low']}°  Rain: {self.weather['rain']}%"

    def get_data(self):
        api = "https://api.open-meteo.com/v1/forecast?latitude=40.7143&longitude=-74.006&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max&temperature_unit=fahrenheit&precipitation_unit=inch&timezone=America%2FNew_York&forecast_days=1"
        response = requests.get(f"{api}")
        if response.status_code == 200:
            res = response.json()
            self.weather['high'] = res['daily']['temperature_2m_max'][0]
            self.weather['low'] = res['daily']['temperature_2m_min'][0]
            self.weather['rain'] = res['daily']['precipitation_probability_max'][0]
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")
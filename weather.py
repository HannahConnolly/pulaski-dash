import requests
import json

use_local = True


class Weather:
    def __init__(self):
        self.weather = {
            "high_temp": "n.a",
            "low_temp": "n.a",
            "rain_today": "n.a",
            "current_temp": "n.a",
            "hourly_rain": "n.a",
        }

    def get_weather_printout(self):
        self.get_data()
        # return f"Current: {self.weather['current_temp']}° | High: {self.weather['high_temp']}° | Low: {self.weather['low_temp']}° \nRain: {self.weather['rain_today']}%"
        return f"Current: {self.weather['current_temp']}° |  High: {self.weather['high_temp']}° |  Low: {self.weather['low_temp']}°\nRain: {self.weather['hourly_rain']}"

    def get_data(self):
        try:
            api = f"https://api.open-meteo.com/v1/forecast?latitude=40.6501&longitude=73.9496&current=temperature_2m&hourly=precipitation_probability&daily=temperature_2m_max,temperature_2m_min&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York&forecast_days=1"
            response = requests.get(f"{api}")
            if response.status_code == 200:
                res = response.json()
                self.weather["high_temp"] = int(res["daily"]["temperature_2m_max"][0])
                self.weather["low_temp"] = int(res["daily"]["temperature_2m_min"][0])
                self.weather["current_temp"] = int(res["current"]["temperature_2m"])
                self.parse_rain(res["hourly"]["precipitation_probability"])
            else:
                print(
                    f"Hello person, there's a {response.status_code} error with your request"
                )
        finally:
            return

    # rain_percent_ascii_key = ["  ", "░░", "▒▒", "▓▓"]
    rain_percent_ascii_key = ["  ", "__", "--", "^^"]

    def parse_rain(self, hourly_precipitation):
        rain = " "
        rain_count = 0
        for rain_hour in hourly_precipitation:
            if rain_hour == 0:
                rain += self.rain_percent_ascii_key[0]
            elif rain_hour < 15:
                rain += self.rain_percent_ascii_key[1]
            elif rain_hour < 50:
                rain += self.rain_percent_ascii_key[2]
            else:
                rain += self.rain_percent_ascii_key[3]
            rain_count += rain_hour

        if rain_count == 0:
            self.weather["hourly_rain"] = "no rain : ^ ) "
        else:
            self.weather["hourly_rain"] = rain

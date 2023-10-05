import requests
import json

class MtaApi:
    trainBoard = {
        'manhattan_J': [], # S
        'queens_J': [], # N
        'manhattan_M': [], # N
        'queens_M': [] # S
    }

    station_id = 0

    def __init__(self):
        print('init api')
        self.station_id = self.get_station()

    def parseTrainTime(self, train_time):
        return int(train_time / 60)

    def parseTrain(self, train):
        print(train)
        if train['route_id'] == 'J':
            if train['direction'] == 'S':
                self.trainBoard['manhattan_J'].append(self.parseTrainTime(train['time']))
            else:
                self.trainBoard['queens_J'].append(self.parseTrainTime(train['time']))
        elif train['route_id'] == 'M':
            if train['direction'] == 'N':
                self.trainBoard['manhattan_M'].append(self.parseTrainTime(train['time']))
            else:
                self.trainBoard['queens_M'].append(self.parseTrainTime(train['time']))

    def get_trains(self, use_local_data):
        print('getting train data...')

        data = None
        if not use_local_data:
            api = MtaApi()
            data = api.get_data()
            print(data)
        else:
            f = open('data/exampleFetch.json')
            data = json.load(f)

        for train in data[0]['trains']:
            self.parseTrain(train)
        print(self.trainBoard)
        return self.trainBoard

    def formatted_print(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def get_station(self):
        station_id = 0
        api = "http://localhost:5000/api/stations"
        response = requests.get(f"{api}").json()
        for station in response:
            if station["name"] == "Myrtle Av":
                return station["station_id"]

    def get_data(self):
        api = f"http://localhost:5000/api/train_times/{self.station_id}"
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            print(type(response.json()))
            return response.json()
            # formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")
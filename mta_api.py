import requests
import json

class MtaApi:
    station_id = None

    def __init__(self):
        print('init api')
        self.resetTrainBoard()
        if self.station_id == None:
            self.station_id = self.get_station()

    def resetTrainBoard(self):
        self.trainBoard = {
            'manhattan_J': [], # S
            'queens_J': [], # N
            'manhattan_M': [], # N
            'queens_M': [] # S
        }

    def parseTrainTime(self, train_time):
        return int(train_time / 60)

    def parseTrain(self, train):
        # print(train)
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

        self.resetTrainBoard()
        # print('getting train data...')

        data = None
        if not use_local_data:
            data = self.get_data()
            # print(data)
        else:
            f = open('data/exampleFetch.json')
            data = json.load(f)

        try:
            for train in data[0]['trains']: 
                self.parseTrain(train)
            # print(self.trainBoard)
        except TypeError:
            return "failed to recieve trains from API"
        finally:
            return self.trainBoard

    def formatted_print(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def get_station(self):
        api = "http://localhost:5000/api/stations"
        response = requests.get(f"{api}")
        if response.status_code == 200:
            for station in response.json():
                if station["name"] == "Myrtle Av":
                    return station["station_id"]
        else:
            return 999

    def get_data(self):
        api = f"http://localhost:5000/api/train_times/{self.station_id}"
        response = requests.get(f"{api}")
        if response.status_code == 200:
            # print("sucessfully fetched the data")
            # print(type(response.json()))
            return response.json()
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")
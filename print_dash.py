from mta_api import MtaApi
from tabulate import tabulate

use_local = True


class PrintDash:

    def __init__(self):
      print('print dash')
    
    def format_row(self, route_name, departures):
        output = [route_name]
        for departure in departures:
            output.append(departure)
        return output

    def format_trains_to_table(self, train_dict):
        table = []
        table.append(self.format_row('J -> Manhattan', train_dict['manhattan_J']))
        table.append(self.format_row('J -> Queens', train_dict['queens_J']))
        table.append([])
        table.append(self.format_row('M -> Manhattan', train_dict['manhattan_M']))
        table.append(self.format_row('M -> Queens', train_dict['queens_M']))
        return table
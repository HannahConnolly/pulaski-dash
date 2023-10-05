from mta_api import MtaApi
from print_dash import PrintDash
import json
from tabulate import tabulate
import time
from os import system

system('mode con: cols=200 lines=49')

use_local = False


class PulaskiDash:

        
    def __init__(self):
        train_getter = MtaApi()
        print_dash = PrintDash()
        while(True):
            train_board = train_getter.get_trains(use_local)
            print_dash.format_trains_to_table(train_board)
            time.sleep(60)
          
    


pulaski_dash = PulaskiDash()


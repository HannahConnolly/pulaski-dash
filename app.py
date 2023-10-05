from mta_api import MtaApi
from print_dash import PrintDash
import json
from tabulate import tabulate

use_local = True


class PulaskiDash:

        
    def __init__(self):
        train_getter = MtaApi()
        print_dash = PrintDash()
        train_board = train_getter.get_trains(use_local)
        print(train_board)
        print_dash.format_trains_to_table(train_board)
        
    


pulaski_dash = PulaskiDash()


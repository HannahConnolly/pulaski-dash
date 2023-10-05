from mta_api import MtaApi
from print_dash import PrintDash
import json
from tabulate import tabulate
import time
use_local = False


train_getter = MtaApi()
print_dash = PrintDash()
while(True):
  train_board = train_getter.get_trains(use_local)
  x = 0
  while x < 10:
    print('\n')
    x+=1
  print(tabulate(print_dash.format_trains_to_table(train_board)))
  time.sleep(60)


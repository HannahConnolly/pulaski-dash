from mta_api import MtaApi
from print_dash import PrintDash
import json
from tabulate import tabulate
import time

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

use_local = False

train_getter = MtaApi()
print_dash = PrintDash()
while(True):
  train_board = train_getter.get_trains(use_local)
  x = 0
  while x < 10:
    print(Back.WHITE + '\n')
    x+=1
  print(Fore.BLACK + Back.WHITE + tabulate(print_dash.format_trains_to_table(train_board)))
  time.sleep(60)


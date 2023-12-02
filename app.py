from mta_api import MtaApi
from print_dash import PrintDash
import json
from tabulate import tabulate
import time
import sys
import itertools
from datetime import date


from colorama import Fore, Back, Style

from weather import Weather

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

use_local = False

train_getter = MtaApi()
print_dash = PrintDash()
weather = Weather()
colors = Fore.BLACK + Back.WHITE

spinner = itertools.cycle(["-", "/", "|", "\\"])
busy = True


def sleep_spinner():
    i = 0
    while i < 60:
        sys.stdout.write(next(spinner))  # write the next character
        sys.stdout.flush()  # flush stdout buffer (actual character display)
        sys.stdout.write("\b")  # erase the last written char
        time.sleep(1)
        i += 1


while True:
    sys.stdout.flush()
    t = time.localtime()
    today = date.today()
    if t.tm_hour > 6 and t.tm_hour < 19:
        colors = Fore.BLACK + Back.WHITE
    else:
        colors = Fore.WHITE + Back.BLACK
    train_board = train_getter.get_trains(use_local)

    x = 0
    while x < 10:
        print(colors + "\n")
        x += 1
    current_time = time.strftime("%I:%M %p")
    current_date = today.strftime("%d/%m/%Y")
    # print(colors + current_time)
    # print(colors + current_date)
    print(colors + current_time + "  |  " + current_date)
    print(colors + weather.get_weather_printout())
    print(colors + tabulate(print_dash.format_trains_to_table(train_board)))
    # time.sleep(60)
    sleep_spinner()

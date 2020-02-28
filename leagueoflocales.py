# Simple LoL Locale Changer
# Created Feb 2020
# By Doomlad

from modules.os_information import os_information
from modules.autoupdate import auto_updates
from modules.prerequisites import prerequisites
from modules.initial_configuration import initial_configuration
from modules.league_directory import league_directory
from modules.client_execution import client_execution

# Try importing colorama, if it fails continue the code to handle installing it automatically
try:
    from colorama import init
    init()
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    pass


def main():

    while True:

        prerequisites()
        print(Fore.GREEN + "Satisfied!" + Style.RESET_ALL)
        auto_updates()
        os_information()
        initial_configuration()
        league_directory()
        client_execution()


if __name__ == '__main__':
    main()

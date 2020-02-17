# Simple LoL Locale Changer
# Created Feb 2020
# By Doomlad

import time
import os
import configparser
import urllib.request
from __init__ import __version__


class colors:

    # Deprecated
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def auto_updates():
    print("Checking for updates...", end="")
    update_program = urllib.request.urlopen("https://raw.githubusercontent.com/Doomlad/AutoSSH/master/__init__.py")
    read_update = update_program.read()

    def getVersion(string):
        getVersion.version = string[16:20]
    getVersion(str(read_update))

    if __version__ == getVersion.version:
        print(f"{colors.OKGREEN}Up to Date!{colors.ENDC}")

    elif __version__ < getVersion.version:
        print(f"{colors.FAIL}Out of Date!{colors.ENDC}")
        print(f"Current version: {colors.FAIL}" + __version__ + f"{colors.ENDC}\nLatest version: {colors.OKGREEN}" +
              getVersion.version + f"{colors.ENDC}")

    else:
        print(f"{colors.FAIL}Warning!{colors.ENDC} The version you are on is higher than the current latest release."
              f" This could mean you're using an illegitimate version of my software. Exercise caution!")


def main():

    print("Opening config file...", end="")
    league_config = open("testconfig.yaml").read()
    print(f"{colors.OKGREEN}Done!{colors.ENDC}")

    print("Replacing locale...", end="")
    league_config = league_config.replace('es_MX', 'en_US')
    print(f"{colors.OKGREEN}Done!{colors.ENDC}")

    file = open("testconfig.yaml", 'w')

    print("Writing changes to file...", end="")
    file.write(league_config)
    print(f"{colors.OKGREEN}Done!{colors.ENDC}\nClosing file...")

    file.close()
    print(f"Wrote changes to config 'spanish' {colors.OKGREEN}->{colors.ENDC} 'english'")

    user_input = input(f"{colors.WARNING}You must run league through the old client executable. Open now? y/n:{colors.ENDC} ")

    if user_input == "y":
        print("Opening league...")

    elif user_input == "n":
        print("Exiting...")


if __name__ == '__main__':
    main()

# Simple LoL Locale Changer
# Created Feb 2020
# By Doomlad

import time
import os
import configparser
import urllib.request
from __init__ import __version__
import platform


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


class locales:

    # Locales
    english = 'en_US'
    portuguese = 'pt_BR'
    turkish = 'tr_TR'
    # english = 'en_GB'
    dutch = 'de_DE'
    # spanish = 'es_ES'
    french = 'fr_FR'
    italian = 'it_IT'
    czech = 'cs_CZ'
    greek = 'el_GR'
    hungarian = 'hu_HU'
    polish = 'pl_PL'
    romanian = 'ro_RO'
    russian = 'ru_RU'
    spanish = 'es_MX'
    # English = 'en_AU'
    japanese = 'ja_JP'
    korean = 'ko_KR'


def os_information():

    print(f"{colors.WARNING}OS:      " + platform.system() + " " + platform.release() +
          f"\nVersion: " + platform.version() +
          f"\nMachine: " + platform.machine())


def auto_updates():
    print("Checking for updates...", end="")
    update_program = urllib.request.urlopen("https://raw.githubusercontent.com/Doomlad/LANtoENG/master/__init__.py")
    read_update = update_program.read()

    def getVersion(string):
        getVersion.version = string[17:21]
    getVersion(str(read_update))

    if __version__ == getVersion.version:
        print(f"{colors.OKGREEN}Up to Date!{colors.ENDC}")

    elif __version__ < getVersion.version:
        print(f"{colors.FAIL}Out of Date! [" + __version__ + f"]{colors.ENDC}{colors.OKGREEN} [" +
              getVersion.version + f"]{colors.ENDC}")

    else:
        print(f"{colors.FAIL}Warning!{colors.ENDC} The version you are on {colors.FAIL}[" + __version__ + f"]"
              f"{colors.ENDC} is higher than the current latest release {colors.OKGREEN}[" + getVersion.version + f"]"
              f"{colors.ENDC}. {colors.FAIL}Exercise caution!{colors.ENDC}")


def main():
    auto_updates()

    print(f"{colors.HEADER}* League of Locales *\n * Made By Doomlad *{colors.ENDC}\n")

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

    user_input = input(f"{colors.WARNING}You must run league through the old client executable. "
                       f"Open now? y/n:{colors.ENDC} ")

    if user_input == "y":
        print("Opening league...")

    elif user_input == "n":
        print("Exiting...")


if __name__ == '__main__':
    main()

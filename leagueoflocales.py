# Simple LoL Locale Changer
# Created Feb 2020
# By Doomlad

import time
import os
import configparser
import urllib.request
import subprocess
import platform
from setuptools.command.easy_install import main as install
from __init__ import __version__

try:
    from colorama import init
    init()
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    pass


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
    BRIGHT_RED = '1;31;40m'


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


def prerequisites():

    package = 'colorama'
    try:
        return __import__(package)

    except ImportError:
        print("Not Satisfied!\n")

        while True:
            print("You are missing the module " + package + "\n(Install once and forget about it)")
            user_input = input("\nWould you like to install it? y/n: ")

            if user_input == 'y':
                print("Installing " + package + " via pip...", end="")
                install([package])
                print("Done!\nPlease restart the program.")
                counter = 4
                for count in range(3):
                    counter -= 1
                    print("Exiting in..." + str(counter), end="\r")
                    time.sleep(1)
                exit()

            elif user_input == 'n':
                print("\nThis program cannot function without colorama, please consider installing to continue.\n")
                counter = 4
                for count in range(3):
                    counter -= 1
                    print("Exiting in..." + str(counter), end="\r")
                    time.sleep(1)
                exit()

            else:
                continue


def os_information():

    print(Fore.MAGENTA + "OS:      " + platform.system() + " " + platform.release() +
          f"\nVersion: " + platform.version() +
          f"\nMachine: " + platform.machine() + Style.RESET_ALL + "\n")


def auto_updates():
    print("Checking for updates...", end="")
    update_program = urllib.request.urlopen("https://raw.githubusercontent.com/Doomlad/LANtoENG/master/__init__.py")
    read_update = update_program.read()

    def getVersion(string):
        getVersion.version = string[17:21]
    getVersion(str(read_update))

    if __version__ == getVersion.version:
        print(Fore.GREEN + "Up to Date!\n" + Style.RESET_ALL)

    elif __version__ < getVersion.version:
        print(Fore.RED + "Out of Date! \n\nCurrent...[" + __version__ + "] \n" + Fore.GREEN + "Latest..." + Fore.GREEN +
              "[" + getVersion.version + "]\n")

    else:
        print(Fore.RED + "Warning! " + Style.RESET_ALL + "Your version " + Fore.RED + "[" + __version__ + f"]"
              + Style.RESET_ALL + " is greater than current latest release " + Fore.GREEN + "[" + getVersion.version
              + f"]" + Style.RESET_ALL + ". " + Fore.RED + "\nExercise caution!\n" + Style.RESET_ALL)


def languages_banner():

    print("\n[1] English\n"
          "[2] Portuguese\n"
          "[3] Turkish\n"
          "[4] Dutch\n"
          "[5] Spanish\n"
          "[6] French\n"
          "[7] Italian\n"
          "[8] Czech\n"
          "[9] Greek\n"
          "[10] Hungarian\n"
          "[11] Polish\n"
          "[12] Romanian\n"
          "[13] Russian\n"
          "[14] Japanese\n"
          "[15] Korean\n")


def initial_configuration():

    while True:
        config = configparser.ConfigParser()
        try:
            print("Opening config file...", end="")
            if len(config.read('user_config.ini')) == 0:
                print(Fore.RED + "Not found!" + Style.RESET_ALL + "\nGenerating first time configuration...")
                configfile = open("user_config.ini", "w+")
                config.add_section('Locale')
                config.set('Locale', 'Current', 'default')
                config.set('Locale', 'Desired', 'default')
                config.set('Locale', 'IsKorean', 'no')
                languages_banner()

                user_input = input("Choose your clients current language: ")

                if user_input == '1':
                    print("English selected.")
                    initial_configuration.current = locales.english
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '2':
                    print("Portuguese selected.")
                    initial_configuration.current = locales.portuguese
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '3':
                    print("Turkish selected.")
                    initial_configuration.current = locales.turkish
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '4':
                    print("Dutch selected.")
                    initial_configuration.current = locales.dutch
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '5':
                    print("Spanish selected.")
                    initial_configuration.current = locales.spanish
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '6':
                    print("French selected.")
                    initial_configuration.current = locales.french
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '7':
                    print("Italian selected.")
                    initial_configuration.current = locales.italian
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '8':
                    print("Czech selected.")
                    initial_configuration.current = locales.czech
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '9':
                    print("Greek selected.")
                    initial_configuration.current = locales.greek
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '10':
                    print("Hungarian selected.")
                    initial_configuration.current = locales.hungarian
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '11':
                    print("Polish selected.")
                    initial_configuration.current = locales.polish
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '12':
                    print("Romanian selected.")
                    initial_configuration.current = locales.romanian
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '13':
                    print("Russian selected.")
                    initial_configuration.current = locales.russian
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '14':
                    print("Japanese selected.")
                    initial_configuration.current = locales.japanese
                    config['Locale']['Current'] = initial_configuration.current

                elif user_input == '15':
                    print("Korean selected.")
                    initial_configuration.current = locales.korean

                else:
                    print(Fore.RED + "Invalid Entry!" + Style.RESET_ALL)
                    initial_configuration()

                user_input = input("Choose your desired client language: ")

                if user_input == '1':
                    print("English selected.")
                    initial_configuration.desired = locales.english
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '2':
                    print("Portuguese selected.")
                    initial_configuration.desired = locales.portuguese
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '3':
                    print("Turkish selected.")
                    initial_configuration.desired = locales.turkish
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '4':
                    print("Dutch selected.")
                    initial_configuration.desired = locales.dutch
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '5':
                    print("Spanish selected.")
                    initial_configuration.desired = locales.spanish
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '6':
                    print("French selected.")
                    initial_configuration.desired = locales.french
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '7':
                    print("Italian selected.")
                    initial_configuration.desired = locales.italian
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '8':
                    print("Czech selected.")
                    initial_configuration.desired = locales.czech
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '9':
                    print("Greek selected.")
                    initial_configuration.desired = locales.greek
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '10':
                    print("Hungarian selected.")
                    initial_configuration.desired = locales.hungarian
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '11':
                    print("Polish selected.")
                    initial_configuration.desired = locales.polish
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '12':
                    print("Romanian selected.")
                    initial_configuration.desired = locales.romanian
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '13':
                    print("Russian selected.")
                    initial_configuration.desired = locales.russian
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '14':
                    print("Japanese selected.")
                    initial_configuration.desired = locales.japanese
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '15':
                    print("Korean selected.")
                    initial_configuration.desired = locales.korean
                    config['Locale']['Desired'] = initial_configuration.desired

                else:
                    print(Fore.RED + "Invalid Entry!" + Style.RESET_ALL)
                    initial_configuration()

                print("\nReview your selection... \nCurrent Locale: " + initial_configuration.current +
                      "\nDesired Locale: " + initial_configuration.desired)
                user_input = input("\nConfirm? y/n: ")

                if user_input == 'y':
                    print("Writing changes to config file...", end="")

                    config.write(configfile)
                    configfile.close()
                    print(Fore.GREEN + "Done!" + Style.RESET_ALL)
                    break

                elif user_input == 'n':
                    print("Restarting...")
                    configfile.close()
                    continue

                else:
                    pass

            else:
                try:
                    print(Fore.GREEN + "Found!" + Style.RESET_ALL)

                    initial_configuration.current = config['Locale']['Current']
                    print("Current Locale..." + Fore.GREEN + initial_configuration.current + Style.RESET_ALL)

                    initial_configuration.desired = config['Locale']['Desired']
                    print("Desired Locale..." + Fore.GREEN + initial_configuration.desired + Style.RESET_ALL)

                    break

                except KeyError:
                    print(Fore.RED + "[KeyError]" + Style.RESET_ALL + " Could not grab configuration from file. "
                          f"Deleting broken config...", end="")
                    os.remove("user_config.ini")
                    print(Fore.GREEN + "Done!" + Style.RESET_ALL)

                except KeyboardInterrupt:
                    print(Fore.RED + "CTRL + C pressed!" + Style.RESET_ALL)

        except KeyError:
            print("[KeyError] Could not grab configuration from file. "
                  "Deleting broken config...", end="")
            os.remove("config.ini")
            print(Fore.GREEN + "Done!" + Style.RESET_ALL)
            counter = 6
            for count in range(5):
                counter -= 1
                print("Restarting in..." + str(counter), end="\r")
                time.sleep(1)


def league_directory():
    league_directory.directory_c = "C:\\Riot Games"
    league_directory.directory_d = "D:\\Riot Games"
    league_directory.directory_e = "E:\\Riot Games"

    dir_counter = 0
    league_directory.counter_c = 0
    for root, dirs, files in os.walk(league_directory.directory_c):
        for file in files:
            league_directory.counter_c += 1

    if league_directory.counter_c > 1:
        # print("There are files present, therefore this is the proper directory. C")
        dir_counter += 1

        try:
            league_config = open("C:\\Riot Games\\League of Legends\\Config\\LeagueClientSettings.yaml")

            print("Replacing locale...", end="")
            league_config = league_config.read().replace(initial_configuration.current, initial_configuration.desired)
            print(Fore.GREEN + "Done! " + Style.RESET_ALL)

            file = open("C:\\Riot Games\\League of Legends\\Config\\LeagueClientSettings.yaml", 'w')
            print("Writing changes to file...", end="")
            file.write(league_config)
            print(Fore.GREEN + "Done!" + Style.RESET_ALL + "\nClosing file...", end="")

            file.close()
            print(Fore.GREEN + "Done! " + Style.RESET_ALL)

        except FileNotFoundError:
            league_directory.counter_c = 0
            pass

    else:
        pass

    league_directory.counter_d = 0
    for root, dirs, files in os.walk(league_directory.directory_d):
        for file in files:
            league_directory.counter_d += 1

    if league_directory.counter_d > 1:
        # print("There are files present, therefore this is the proper directory. D")
        dir_counter += 1

        try:
            league_config = open("D:\\Riot Games\\League of Legends\\Config\\LeagueClientSettings.yaml")

            print("Replacing locale...", end="")
            league_config = league_config.read().replace(initial_configuration.current, initial_configuration.desired)
            print(Fore.GREEN + "Done! " + Style.RESET_ALL)

            file = open("D:\\Riot Games\\League of Legends\\Config\\LeagueClientSettings.yaml", 'w')
            print("Writing changes to file...", end="")
            file.write(league_config)
            print(Fore.GREEN + "Done!" + Style.RESET_ALL + "\nClosing file...", end="")

            file.close()
            print(Fore.GREEN + "Done! " + Style.RESET_ALL)

        except FileNotFoundError:
            league_directory.counter_d = 0
            pass

    else:
        pass

    league_directory.counter_e = 0
    for root, dirs, files in os.walk(league_directory.directory_e):
        for file in files:
            league_directory.counter_e += 1

    if league_directory.counter_e > 1:
        # print("There are files present, therefore this is the proper directory. E")
        dir_counter += 1

        try:
            league_config = open("E:\\Riot Games\\League of Legends\\Config\\LeagueClientSettings.yaml")

            print("Replacing locale...", end="")
            league_config = league_config.read().replace(initial_configuration.current, initial_configuration.desired)
            print(Fore.GREEN + "Done! " + Style.RESET_ALL)

            file = open("E:\\Riot Games\\League of Legends\\Config\\LeagueClientSettings.yaml", 'w')
            print("Writing changes to file...", end="")
            file.write(league_config)
            print(Fore.GREEN + "Done!" + Style.RESET_ALL + "\nClosing file...", end="")

            file.close()
            print(Fore.GREEN + "Done! " + Style.RESET_ALL)

        except FileNotFoundError:
            league_directory.counter_e = 0
            pass

    else:
        pass

    # More than 1 folder flagged with a Riot Games folder
    if dir_counter >= 2:
        print(Fore.RED + "Notice! " + Style.RESET_ALL + "Two or more 'Riot Games' folders found!")


def main():
    while True:
        os.system("cls")
        print("Checking for prerequisite...", end="")
        prerequisites()
        print(Fore.GREEN + "Satisfied!" + Style.RESET_ALL)
        
        auto_updates()

        print(Fore.YELLOW + "* League of Locales *\n " + Fore.CYAN + "* Made By Doomlad *\n" + Style.RESET_ALL)
        
        os_information()

        initial_configuration()
        
        league_directory()

        print(Fore.YELLOW + "\n[Wrote] " + Style.RESET_ALL + "changes to config locale " + Fore.GREEN + "->" +
              Style.RESET_ALL + " '" + initial_configuration.desired + "'\n")

        user_input = input("You must run league through the old client executable. Open now? y/n: ")

        if user_input == "y":
            print("Opening league...", end="")

            league_client_dir = "C:\\Riot Games\\League of Legends\\"

            if league_directory.counter_c > 1:
                print(Fore.YELLOW + "Directory: C:\\Riot Games\\League of Legends\\LeagueClient.exe")
                os.chdir(league_client_dir)
                print("Injecting locale...", end="")
                subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            elif league_directory.counter_d > 1:
                print(Fore.YELLOW + "Directory: D:\\Riot Games\\League of Legends\\LeagueClient.exe")
                os.chdir(league_client_dir)
                print("Injecting locale...", end="")
                subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            elif league_directory.counter_e > 1:
                print(Fore.YELLOW + "Directory: E:\\Riot Games\\League of Legends\\LeagueClient.exe")
                os.chdir(league_client_dir)
                print("Injecting locale...", end="")
                subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            break

        elif user_input == "n":
            print("Exiting...")
            break

        else:
            print("Opening league...", end="")

            if league_directory.counter_c > 1:
                print(Fore.YELLOW + "Directory: C:\\Riot Games\\League of Legends\\LeagueClient.exe")
                subprocess.call(['C:\\Riot Games\\League of Legends\\LeagueClient.exe'])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            elif league_directory.counter_d > 1:
                print(Fore.YELLOW + "Directory: D:\\Riot Games\\League of Legends\\LeagueClient.exe")
                subprocess.call(['D:\\Riot Games\\League of Legends\\LeagueClient.exe'])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            elif league_directory.counter_e > 1:
                print(Fore.YELLOW + "Directory: E:\\Riot Games\\League of Legends\\LeagueClient.exe")
                subprocess.call(['E:\\Riot Games\\League of Legends\\LeagueClient.exe'])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            break


if __name__ == '__main__':
    main()

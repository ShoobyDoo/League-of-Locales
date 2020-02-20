from modules.initial_configuration import initial_configuration
import os
try:
    from colorama import init

    init()
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    pass


def league_directory():
    if initial_configuration.is_garena == 'yes':

        league_directory.directory_c = "C:\\Garena\\Games\\32771"
        league_directory.directory_d = "D:\\Garena\\Games\\32771"
        league_directory.directory_e = "F:\\Garena\\Games\\32771"

    else:

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
        print(Fore.RED + "Notice: " + Style.RESET_ALL + "Two or more 'Riot Games' folders found!")

    print(Fore.YELLOW + "\n[Wrote] " + Style.RESET_ALL + "changes to config locale " + Fore.GREEN + "->" +
          Style.RESET_ALL + " '" + initial_configuration.desired + "'\n")

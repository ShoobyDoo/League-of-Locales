import os
import subprocess
from modules.initial_configuration import initial_configuration
from modules.league_directory import league_directory
try:
    from colorama import init
    init()
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    pass


def client_execution():
    
    print(Fore.YELLOW + "To reset your configuration, type 'delete config' instead of y/n below." + Style.RESET_ALL)
    user_input = input("You must run league through the old client executable. Open now? y/n: ")

    if user_input == "y":

        print("Opening league..." + Fore.GREEN + "Done!" + Style.RESET_ALL)
        if initial_configuration.is_garena == 'yes':
            league_client_dir_c = "C:\\Garena\Games\\32771\\LeagueClient"
            league_client_dir_d = "D:\\Garena\Games\\32771\\LeagueClient"
            league_client_dir_e = "F:\\Garena\Games\\32771\\LeagueClient"
            print("Injecting locale...", end="")
            try:

                os.chdir(league_client_dir_c)
                subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            except FileNotFoundError:

                try:
                    os.chdir(league_client_dir_d)
                    subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])

                except FileNotFoundError:
                    pass

                    try:
                        os.chdir(league_client_dir_e)
                        subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])

                    except FileNotFoundError:
                        pass

            print(Fore.GREEN + "Done!" + Style.RESET_ALL)
            exit()

        else:
            league_client_dir_c = "C:\\Riot Games\\League of Legends\\"
            league_client_dir_d = "D:\\Riot Games\\League of Legends\\"
            league_client_dir_e = "E:\\Riot Games\\League of Legends\\"

            if league_directory.counter_c > 1:
                print(Fore.YELLOW + "Directory: C:\\Riot Games\\League of Legends\\LeagueClient.exe")
                os.chdir(league_client_dir_c)
                print("Injecting locale...", end="")
                subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            elif league_directory.counter_d > 1:
                print(Fore.YELLOW + "Directory: D:\\Riot Games\\League of Legends\\LeagueClient.exe")
                os.chdir(league_client_dir_d)
                print("Injecting locale...", end="")
                subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            elif league_directory.counter_e > 1:
                print(Fore.YELLOW + "Directory: E:\\Riot Games\\League of Legends\\LeagueClient.exe")
                os.chdir(league_client_dir_e)
                print("Injecting locale...", end="")
                subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            exit()

    elif user_input == "n":
        print(Fore.RED + "Exiting..." + Style.RESET_ALL)
        exit()

    elif user_input.lower() == "delete config":
        os.remove("user_config.ini")
        print(Fore.RED + "\n[V] Config deleted." + Style.RESET_ALL)
        initial_configuration()

    else:

        if initial_configuration.is_garena == 'yes':
            league_client_dir_c = "C:\\Garena\Games\\32771\\LeagueClient"
            league_client_dir_d = "D:\\Garena\Games\\32771\\LeagueClient"
            league_client_dir_e = "F:\\Garena\Games\\32771\\LeagueClient"
            print("Injecting locale...", end="")
            try:

                os.chdir(league_client_dir_c)
                subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

            except FileNotFoundError:

                try:
                    os.chdir(league_client_dir_d)
                    subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])

                except FileNotFoundError:
                    pass

                    try:
                        os.chdir(league_client_dir_e)
                        subprocess.Popen(['LeagueClient.exe', "--locale=" + initial_configuration.desired])

                    except FileNotFoundError:
                        pass

            print(Fore.GREEN + "Done!" + Style.RESET_ALL)
            exit()

    print(Fore.GREEN + "Done!" + Style.RESET_ALL)

import configparser
import os
import time
from modules.locales import locales
from modules.languages import languages_banner
try:
    from colorama import init
    init()
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    pass


# Initial configurations set by user
def initial_configuration():

    while True:
        # Instantiate config
        config = configparser.ConfigParser()
        try:
            # Search for config and if not found, prompt generation of first time configuration
            print("Opening config file...", end="")
            if len(config.read('user_config.ini')) == 0:
                print(Fore.RED + "Not found!" + Style.RESET_ALL + "\nGenerating first time configuration...")
                configfile = open("user_config.ini", "w+")
                config.add_section('Locale')
                config.set('Locale', 'Current', 'en_US')
                config.set('Locale', 'Desired', 'en_US')
                config.set('Locale', 'IsGarena', 'No')
                config.set('Locale', 'lolDir', '')
                
                initial_configuration.lolDir_user = input("\nEnter your LoL Directory "
                                                          r"(Default: C:\Riot Games\League of Legends): ")
                if initial_configuration.lolDir_user == "":
                    initial_configuration.lolDir_user = r"C:\Riot Games\League of Legends"

                config['Locale']['lolDir'] = initial_configuration.lolDir_user
                languages_banner()

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
                    print("French selected.")
                    initial_configuration.desired = locales.french
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '6':
                    print("Italian selected.")
                    initial_configuration.desired = locales.italian
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '7':
                    print("Czech selected.")
                    initial_configuration.desired = locales.czech
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '8':
                    print("Greek selected.")
                    initial_configuration.desired = locales.greek
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '9':
                    print("Hungarian selected.")
                    initial_configuration.desired = locales.hungarian
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '10':
                    print("Polish selected.")
                    initial_configuration.desired = locales.polish
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '11':
                    print("Romanian selected.")
                    initial_configuration.desired = locales.romanian
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '12':
                    print("Russian selected.")
                    initial_configuration.desired = locales.russian
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '13':
                    print("Spanish selected.")
                    initial_configuration.desired = locales.spanish
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '14':
                    print("Japanese selected.")
                    initial_configuration.desired = locales.japanese
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '15':
                    print("Korean selected.")
                    initial_configuration.desired = locales.korean
                    config['Locale']['Desired'] = initial_configuration.desired

                # Newer Locales
                elif user_input == '16':
                    print("Indonesian selected.")
                    initial_configuration.desired = locales.indonesian
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '17':
                    print("Chinese selected.")
                    initial_configuration.desired = locales.chinese
                    config['Locale']['Desired'] = initial_configuration.desired

                else:
                    print(Fore.RED + "Invalid Entry!" + Style.RESET_ALL)
                    initial_configuration()

                initial_configuration.is_garena = 'no'
                config['Locale']['IsGarena'] = initial_configuration.is_garena

                print(Fore.YELLOW + "\nReview your selection..." + Fore.CYAN + " \nDesired Locale: " +
                      initial_configuration.desired + "\nPath to LoL: " + initial_configuration.lolDir_user +
                      Style.RESET_ALL)
                user_input = input("\nConfirm? y/n: ")

                if user_input == 'y':
                    print("Writing changes to config file...", end="")
                    config.write(configfile)
                    configfile.close()
                    print(Fore.GREEN + "Done!" + Style.RESET_ALL)
                    time.sleep(0.75)
                    continue

                elif user_input == 'n':
                    configfile.close()
                    print(Fore.RED + "Restarting..." + Style.RESET_ALL)
                    time.sleep(0.75)
                    continue
                
                elif user_input == "":
                    print("Writing changes to config file...", end="")
                    config.write(configfile)
                    configfile.close()
                    print(Fore.GREEN + "Done!" + Style.RESET_ALL)
                    time.sleep(0.75)
                    continue
                
                else:
                    pass

            else:
                try:
                    print(Fore.GREEN + "Found!" + Style.RESET_ALL)

                    initial_configuration.current = config['Locale']['Current']

                    initial_configuration.desired = config['Locale']['Desired']
                    print("Desired Locale..." + Fore.GREEN + initial_configuration.desired + Style.RESET_ALL)

                    initial_configuration.is_garena = config['Locale']['IsGarena']
                    
                    initial_configuration.lolDir_user = config['Locale']['lolDir']
                    print("LoL Directory..." + Fore.GREEN + initial_configuration.lolDir_user + Style.RESET_ALL)

                    break

                except KeyError:
                    print(Fore.RED + "[KeyError]" + Style.RESET_ALL + " Could not grab configuration from file. "
                          f"Deleting broken config...", end="")
                    os.remove("user_config.ini")
                    print(Fore.GREEN + "Done!" + Style.RESET_ALL + "\n")

                except KeyboardInterrupt:
                    print(Fore.RED + "CTRL + C pressed!" + Style.RESET_ALL)

        except KeyError:
            print(Fore.RED + "[KeyError]" + Style.RESET_ALL + " Could not grab configuration from file. "
                                                              f"Deleting broken config...", end="")
            os.remove("user_config.ini")
            print(Fore.GREEN + "Done!" + Style.RESET_ALL + "\n")

        except KeyboardInterrupt:
            print(Fore.RED + "CTRL + C pressed!" + Style.RESET_ALL)

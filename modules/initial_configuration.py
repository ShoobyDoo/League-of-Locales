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
                languages_banner()

                # user_input = input("Choose your clients current language: ")
                #
                # if user_input == '1':
                #     print("English selected.")
                #     initial_configuration.current = locales.english
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '2':
                #     print("Portuguese selected.")
                #     initial_configuration.current = locales.portuguese
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '3':
                #     print("Turkish selected.")
                #     initial_configuration.current = locales.turkish
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '4':
                #     print("Dutch selected.")
                #     initial_configuration.current = locales.dutch
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '5':
                #     print("Spanish selected.")
                #     initial_configuration.current = locales.spanish
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '6':
                #     print("French selected.")
                #     initial_configuration.current = locales.french
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '7':
                #     print("Italian selected.")
                #     initial_configuration.current = locales.italian
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '8':
                #     print("Czech selected.")
                #     initial_configuration.current = locales.czech
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '9':
                #     print("Greek selected.")
                #     initial_configuration.current = locales.greek
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '10':
                #     print("Hungarian selected.")
                #     initial_configuration.current = locales.hungarian
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '11':
                #     print("Polish selected.")
                #     initial_configuration.current = locales.polish
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '12':
                #     print("Romanian selected.")
                #     initial_configuration.current = locales.romanian
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '13':
                #     print("Russian selected.")
                #     initial_configuration.current = locales.russian
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '14':
                #     print("Japanese selected.")
                #     initial_configuration.current = locales.japanese
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '15':
                #     print("Korean selected.")
                #     initial_configuration.current = locales.korean
                #
                # # Newer Locales
                # elif user_input == '16':
                #     print("Indonesian selected.")
                #     initial_configuration.current = locales.indonesian
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '17':
                #     print("Tagalog selected.")
                #     initial_configuration.current = locales.tagalog
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '18':
                #     print("Chinese selected.")
                #     initial_configuration.current = locales.chinese
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # elif user_input == '19':
                #     print("Vietnamese selected.")
                #     initial_configuration.current = locales.vietnamese
                #     config['Locale']['Current'] = initial_configuration.current
                #
                # else:
                #     print(Fore.RED + "Invalid Entry!" + Style.RESET_ALL)
                #     initial_configuration()

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

                # Newer Locales
                elif user_input == '16':
                    print("Indonesian selected.")
                    initial_configuration.desired = locales.indonesian
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '17':
                    print("Tagalog selected.")
                    initial_configuration.desired = locales.tagalog
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '18':
                    print("Chinese selected.")
                    initial_configuration.desired = locales.chinese
                    config['Locale']['Desired'] = initial_configuration.desired

                elif user_input == '19':
                    print("Vietnamese selected.")
                    initial_configuration.desired = locales.vietnamese
                    config['Locale']['Desired'] = initial_configuration.desired

                else:
                    print(Fore.RED + "Invalid Entry!" + Style.RESET_ALL)
                    initial_configuration()

                # user_input = input("Using Garena client? y/n: ")
                # if user_input == "y":
                #     print("Using Garena client.")
                #     initial_configuration.is_garena = 'yes'
                #     config['Locale']['IsGarena'] = initial_configuration.is_garena
                #
                # if user_input == "n":
                #     print("Not using Garena client.")
                initial_configuration.is_garena = 'no'
                config['Locale']['IsGarena'] = initial_configuration.is_garena

                print("\nReview your selection... \nDesired Locale: " + initial_configuration.desired)
                # '\nCurrent Locale: " + initial_configuration.current +'
                user_input = input("\nConfirm? y/n: ")

                if user_input == 'y':
                    print("Writing changes to config file...", end="")

                    config.write(configfile)
                    configfile.close()
                    print(Fore.GREEN + "Done!" + Style.RESET_ALL)
                    break

                elif user_input == 'n':
                    print(Fore.RED + "Restarting..." + Style.RESET_ALL)
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

                    initial_configuration.is_garena = config['Locale']['IsGarena']
                    print("Is garena..." + Fore.GREEN + initial_configuration.is_garena + Style.RESET_ALL)

                    break

                except KeyError:
                    print(Fore.RED + "[KeyError]" + Style.RESET_ALL + " Could not grab configuration from file. "
                          f"Deleting broken config...", end="")
                    os.remove("user_config.ini")
                    print(Fore.GREEN + "Done!" + Style.RESET_ALL)

                except KeyboardInterrupt:
                    print(Fore.RED + "CTRL + C pressed!" + Style.RESET_ALL)

        except KeyError:
            print(Fore.RED + "[KeyError]" + Style.RESET_ALL + " Could not grab configuration from file. "
                  "Deleting broken config...", end="")
            os.remove("config.ini")
            print(Fore.GREEN + "Done!" + Style.RESET_ALL)
            counter = 6
            for count in range(5):
                counter -= 1
                print("Restarting in..." + str(counter), end="\r")
                time.sleep(1)

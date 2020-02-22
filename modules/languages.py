# Simple print of available banners
try:
    from colorama import init

    init()
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    pass


def languages_banner():
    locale_list = ['English', 'Portuguese', 'Turkish', 'Dutch', 'French', 'Italian', 'Czech', 'Greek',
                   'Hungarian', 'Polish', 'Romanian', 'Russian', 'Spanish', 'Japanese', 'Korean',
                   'Indonesian', Fore.RED + 'Tagalog (DOES NOT WORK)' + Style.RESET_ALL, 'Chinese', Fore.RED +
                   'Vietnamese (DOES NOT WORK)' + Style.RESET_ALL]
    print()
    counter = 0
    for locale in locale_list:
        counter += 1
        print("[" + str(counter) + "] " + locale)
    print()

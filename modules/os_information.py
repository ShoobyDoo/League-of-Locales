import platform
from .__init__ import __version__
try:
    from colorama import init
    init()
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    pass


# Prints Title and OS information
def os_information():
    print(Fore.YELLOW + "* League of Locales *\n " + Fore.CYAN + "* Made By Doomlad *\n" + Style.RESET_ALL)
    if platform.system().lower() == "windows":
        print(Fore.MAGENTA + "OS:      " + platform.system() + " " + platform.release() +
                             "\nVersion: " + platform.version() +
                             "\nMachine: " + platform.machine() +
                             "\nLoLoc:   " + __version__ + Style.RESET_ALL + "\n")
    else:
        print(Fore.RED + "Unsupported Operating System! This program has only been tested on Windows. " +
              Style.RESET_ALL)

import urllib.request
import os
import subprocess
from zipfile import ZipFile
from .__init__ import __version__
try:
    from colorama import init
    init()
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    pass


def auto_updates():
    print("Checking for updates...", end="")
    update_program = urllib.request.urlopen\
        ("https://raw.githubusercontent.com/Doomlad/League-of-Locales/master/__init__.py")
    read_update = update_program.read().decode('utf-8')

    def getVersion(string):
        getVersion.version = string[15:19]
    getVersion(str(read_update))

    if __version__ == getVersion.version:
        print(Fore.GREEN + "Up to Date!\n" + Style.RESET_ALL)

    elif __version__ < getVersion.version:

        print(Fore.RED + "Out of Date! \n\nCurrent...[" + __version__ + "] \n" + Fore.GREEN + "Latest..." + Fore.GREEN +
              "[" + getVersion.version + "]\n" + Style.RESET_ALL + Fore.YELLOW)

        release_information = urllib.request.urlopen\
            ("https://raw.githubusercontent.com/Doomlad/League-of-Locales/master/latestrelease.txt")
        read_release = release_information.read().decode('utf-8')

        def getRelease(string):
            getRelease.release = string
        getRelease(str(read_release))
        print(getRelease.release)

        user_input = input(Style.RESET_ALL + "Would you like to download and install the latest version? y/n: ")

        if user_input == 'y':

            if not os.path.exists('League-of-Locales-master.zip'):
                print(Fore.YELLOW + "\nDownloading to local folder...\n" + Style.RESET_ALL)
                subprocess.call("curl -LJO https://github.com/Doomlad/League-of-Locales/archive/master.zip")
                print(Fore.GREEN + "\nDone!" + Style.RESET_ALL)

                print(Fore.YELLOW + "Extracting..." + Style.RESET_ALL, end="")
                with ZipFile('League-of-Locales-master.zip', 'r') as LoLocales:
                    LoLocales.extractall()
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)
                print(Fore.YELLOW + "Removing Zip File..." + Style.RESET_ALL, end="")
                os.remove('League-of-Locales-master.zip')
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)
                
                os.chdir("./modules")
                os.system("start /B start cmd.exe @cmd /k py autoreplacefiles.py")
                os.chdir("..")

                # print(Fore.CYAN + "\nPlease look inside your League of Locales folder. You will now find a 'League-of-"
                #                   "Locales-master' folder inside. This is the latest release, you can safely delete the"
                #                   " old one, or just copy over the files and overwrite. I will figure out a "
                #                   "way to automate this in later releases. Thank you.\n")
                print(Fore.RED + "Exiting..." + Style.RESET_ALL)
                exit()

            else:
                print("League-of-Locales-master.zip exists!")
                print(Fore.YELLOW + "Removing Zip File..." + Style.RESET_ALL, end="")
                os.remove('League-of-Locales-master.zip')
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

        elif user_input == 'n':
            print(Fore.YELLOW + "\nIt is recommended to be on the latest release for up to date features, bug fixes and "
                                "general optimizations!\n" + Style.RESET_ALL)
            pass

        elif user_input == "":

            if not os.path.exists('League-of-Locales-master.zip'):
                print(Fore.YELLOW + "\nDownloading to local folder...\n" + Style.RESET_ALL)
                subprocess.call("curl -LJO https://github.com/Doomlad/League-of-Locales/archive/master.zip")
                print(Fore.GREEN + "\nDone!" + Style.RESET_ALL)

                print(Fore.YELLOW + "Extracting..." + Style.RESET_ALL, end="")
                with ZipFile('League-of-Locales-master.zip', 'r') as LoLocales:
                    LoLocales.extractall()
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)
                print(Fore.YELLOW + "Removing Zip File..." + Style.RESET_ALL, end="")
                os.remove('League-of-Locales-master.zip')
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

                os.chdir("./modules")
                os.system("start /B start cmd.exe @cmd /k py autoreplacefiles.py")
                os.chdir("..")

                # print(Fore.CYAN + "\nPlease look inside your League of Locales folder. You will now find a 'League-of-"
                #                   "Locales-master' folder inside. This is the latest release, you can safely delete the"
                #                   " old one, or just copy over the files and overwrite. I will figure out a "
                #                   "way to automate this in later releases. Thank you.\n")
                print(Fore.RED + "Exiting..." + Style.RESET_ALL)
                exit()

            else:
                print("League-of-Locales-master.zip exists!")
                print(Fore.YELLOW + "Removing Zip File..." + Style.RESET_ALL, end="")
                os.remove('League-of-Locales-master.zip')
                print(Fore.GREEN + "Done!" + Style.RESET_ALL)

        else:
            print(Fore.RED + "\nUh-oh, Stinky! You didn't enter y/n! Continuing...\n" + Style.RESET_ALL)
            pass

    else:
        print(Fore.RED + "Warning! " + Style.RESET_ALL + "Your version " + Fore.RED + "[" + __version__ + f"]"
              + Style.RESET_ALL + " is greater than current latest release " + Fore.GREEN + "[" + getVersion.version
              + f"]" + Style.RESET_ALL + " " + Fore.RED + "\nExercise caution!\n" + Style.RESET_ALL)

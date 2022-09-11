# Title:        League of Locales
# File:         leagueoflocales.py
# Created:      Feb / 2020
# Modified:     Sept / 09 / 2022
# Author:       ShoobyDoo
# Description:  An easy to use League of Legends language/locale modifier.

# Imports
import configparser
import os
import platform
import subprocess
import time
import urllib.request
import shutil
from os import path

# Local imports
from modules.__init__ import __version__
from modules.colors import Colors
from modules.helpers import Helpers



class LeagueOfLocales:
    def __init__(
        self,
        github_version_url = "https://raw.githubusercontent.com/ShoobyDoo/League-of-Locales/master/modules/__init__.py"
        ) -> None:
        self.github_version_url = github_version_url
        self.config_filename = "lol.ini"
        self.update_available = False
        self.all_locales = {
            'English': 'en_US', 
            'Portuguese': 'pt_BR', 
            'Turkish': 'tr_TR', 
            'Dutch': 'de_DE', 
            'French': 'fr_FR', 
            'Italian': 'it_IT', 
            'Czech': 'cs_CZ', 
            'Greek': 'el_GR',
            'Hungarian': 'hu_HU', 
            'Polish': 'pl_PL', 
            'Romanian': 'ro_RO', 
            'Russian': 'ru_RU', 
            'Spanish': 'es_MX', 
            'Japanese': 'ja_JP', 
            'Korean': 'ko_KR', 
            'Indonesian': 'id_ID', 
            'Chinese': 'zh_CN',
            'Tagalog': 'tl_PH',
            'Vietnamese': 'vi_VN'
        }
        self.language = None
        self.lol_path = None


    def print_banner(self):
        """
        ### Prints the program banner.
        """
        print(Colors.infoize(f"[League of Locales {__version__} by Doomlad] (Python {platform.python_version()})\n"))


    def startup(self) -> None:
        """
        ### Perform several startup functions, essentially initialize the program.
        """
        Helpers.clear_screen()
        self.print_banner()
        self.check_update()
        self.check_config()
        self.get_menu()


    def check_update(self) -> None:
        """
        ### Check and perform an automatic update.
        ---

        Checks GitHub repo for the latest release, and if an update is available, then perform do_update().
        """

        print("Checking for updates...", end='')
        latest_version = str(
            urllib.request.urlopen(self.github_version_url).read().decode('utf-8')
        ).strip().split('=')[-1].replace('\'', '')

        if Helpers.compare_versions(latest_version, __version__):
            # Update available
            print(Colors.colorize(Colors.LIGHT_GREEN, f" done.{Colors.YELLOW} (Update available)"))
            self.update_available = True
        else:
            print(Colors.affirmize(f" done."))
            self.update_available = False


    def do_update(self) -> None:
        if self.update_available:
            # TODO: do the auto update logic. (download release, if no exe, then get zip)
            pass

    
    def write_to_config(self, key: str, value: str) -> None:
        """
        ### Write passed parameters to the config file.
        ---

        Args:
            key (str): Key to modify
            value (str): Value to pass
        """

        config = configparser.ConfigParser()
        config.read(self.config_filename)
        config['League of Locales'][key] = value

        print("Writing changes to config...", end='')
        with open(self.config_filename, "w+") as configfile:
            config.write(configfile)
        print(Colors.affirmize(" done."))
        time.sleep(1)


    def select_locale(self) -> None:
        """
        ### Initiates prompt to get users desired locale
        """

        for idx, language in enumerate(self.all_locales.keys()):
            line = f"[{Colors.errorize(str(idx+1).zfill(2)):<2}] {Colors.colorize(Colors.LIGHT_CYAN, language):<23}"
            if idx % 5 == 4:
                print(line)
            else:
                print(line, end='') if language != list(self.all_locales.keys())[-1] else print(f"{line}\n")
            
        while True:
            desired_locale = input(
                f"Please enter the {Colors.colorize(Colors.LIGHT_CYAN, 'language')} you would like " \
                f"{Colors.colorize(Colors.LIGHT_WHITE + Colors.BOLD, 'OR')} the cooresponding {Colors.colorize(Colors.LIGHT_RED, 'number')}.\n" \
                "Locale: "
            )
            
            if desired_locale.capitalize() in self.all_locales.keys():
                self.language = desired_locale.capitalize()
                self.write_to_config('locale', self.language) # TODO: FIX THIS, CANT WRITE TO FILE THAT DOESNT EXIST
                break
            elif desired_locale == '':
                break
            elif 1 <= int(desired_locale) <= len(self.all_locales):
                self.language = list(self.all_locales.keys())[int(desired_locale) - 1]
                try:
                    self.write_to_config('locale', self.language)
                except KeyError:
                    # tripped likely because its the first run and the config file doesnt exist yet, just ignore.
                    pass
                break
            else:
                print(Colors.colorize(Colors.YELLOW, f'{desired_locale} is not a valid locale, try again.'))


    def check_config(self) -> None:
        """
        ### Check for configuration.
        ---
        Checks to see if a configuration file exists, if it does read the keys otherwise prompt initial setup.
        """

        print("Checking for config...", end='')
        config = configparser.ConfigParser()
        
        if path.exists(self.config_filename):
            config.read(self.config_filename)
            self.language = config['League of Locales']['locale']
            self.lol_path = config['League of Locales']['league_directory']
            print(Colors.colorize(Colors.LIGHT_GREEN, " done.\n"))

        else:
            print(f"{Colors.colorize(Colors.LIGHT_GREEN, f' done. {Colors.YELLOW}(Initiating first time setup...)')}\n")

            print(Colors.infoize("Setting up configuration...\n"))
            config.add_section('League of Locales')

            self.select_locale()

            print(Colors.colorize(Colors.LIGHT_CYAN, f"-> Locale: {self.language}"))
            config.set('League of Locales', 'locale', self.language)
            self.language = config['League of Locales']['locale']

            print(Colors.infoize("\nAttempting to locate your League of Legends installation automatically, please wait...\n"))
            time.sleep(1)

            lol_installs_found = []
            for drive_letter in Helpers.get_drives():
                total, used, free = shutil.disk_usage(f"{drive_letter}:/")

                total_fmtd = Colors.colorize(Colors.BOLD, f"Total: {(total // (2**30))} GiB")
                used_fmtd = Colors.colorize(Colors.YELLOW, f"Used: {(used // (2**30))} GiB")
                free_fmtd = Colors.colorize(Colors.LIGHT_GREEN, f"Free: {(free // (2**30))} GiB")

                print(f"Scanning drive [{drive_letter}] ... {total_fmtd} | {used_fmtd} | {free_fmtd}")

                lol_directory = f"{drive_letter}:/Riot Games/League of Legends"
                if path.exists(lol_directory):
                    print(Colors.colorize(Colors.LIGHT_GREEN, f"    -> Found @ {lol_directory}"))
                    lol_installs_found.append(lol_directory)
            
            if len(lol_installs_found) > 1:
                print(Colors.colorize(Colors.YELLOW, "* Multiple League of Legends installations found, please specify desired install."))
                for lol_install in lol_installs_found:
                    answer = Helpers.yes_no_prompt(f"Use {lol_install}?")
                    if answer == 'Yes':
                        lol_directory = lol_install
                        break
            elif len(lol_installs_found) == 1:
                lol_directory = lol_installs_found[0]
            else:
                print(Colors.colorize(Colors.YELLOW, "* Could not find your League of Legends installation automatically."))
                lol_directory = input("Please enter the FULL path to your League folder. (Ex. C:/Games/Riot Games/League of Legends)\nPath: ")
            
            # TODO: Check to see if the path given contains LeagueClient.exe, if not prompt user to double check.
            print(Colors.colorize(Colors.LIGHT_CYAN, f"-> League Directory: {lol_directory}"))
            config.set('League of Locales', 'league_directory', lol_directory)
            self.lol_path = config['League of Locales']['league_directory']
            
            print("Writing configuration to file...", end='')
            with open(self.config_filename, "w+") as configfile:
                config.write(configfile)
            print(Colors.affirmize(" done."))

            print(Colors.infoize(f"\nInitial configuration is complete. Loading menu...\n"))
            time.sleep(1)


    def execute_client(self):
        """
        ### Force the client to set its locale to the users desired one; irrespective of region.
        """

        os.chdir(self.lol_path)
        print(f"Injecting locale {self.all_locales[self.language]}...", end='')
        subprocess.Popen(['LeagueClient.exe', f"--locale={self.all_locales[self.language]}"])
        print(Colors.affirmize(" done."))


    def get_menu(self):
        """
        ### Prints out the main menu
        """

        menu_items = [
            f"Start client",
            f"Change locale [{Colors.colorize(Colors.LIGHT_CYAN, self.language)}]",
            f"Updater       [{Colors.affirmize('Up to Date') if not self.update_available else Colors.warnize('Update available')}]",
            f"League Folder [{Colors.colorize(Colors.LIGHT_CYAN, self.lol_path)}]",
            f"About",
            f"Quit"
        ]
        for idx, item in enumerate(menu_items):
            print(f"[{Colors.errorize(idx + 1 if item != menu_items[-1] else 'Q')}] {item}")


    def locale_submenu(self):
        """
        ### Handles functionality of the locale selector sub-menu
        """

        Helpers.clear_screen()
        print(Colors.infoize("[Change Locale]\n"))
        print(f"Current: {Colors.colorize(Colors.LIGHT_CYAN, self.language)}\n")
        self.select_locale()
    

    def updater_submenu(self):
        """
        ### Handles functionality of the updater sub-menu
        """

        while True:
            Helpers.clear_screen()
            print(Colors.infoize("[Updater - Work in Progress]\n"))
            print(f"Status: {Colors.affirmize('Up to Date') if self.update_available == False else Colors.warnize('Update available')}\n")

            print(f"[{Colors.errorize('1')}] Check now\n[{Colors.errorize('B')}] Go back\n")
            entry = input("Entry: ").lower()

            if entry == '1':
                self.check_update()
            elif entry == 'b':
                break
    

    def league_folder_submenu(self):
        """
        ### Handles functionality of the league folder sub-menu
        """

        while True:
            Helpers.clear_screen()
            print(Colors.infoize("[League Folder]\n"))
            print(f"Current: {Colors.colorize(Colors.LIGHT_CYAN, self.lol_path)}\n")

            print(f"[{Colors.errorize('1')}] Change folder\n[{Colors.errorize('B')}] Go back\n")
            entry = input("Entry: ").lower()

            if entry == '1':
                self.lol_path = input("Please enter the FULL path to your League folder. (Ex. C:/Games/Riot Games/League of Legends)\nPath: ")
                self.write_to_config('league_directory', self.lol_path)
                break
            elif entry == 'b':
                break

    
    def about_submenu(self):
        """
        ### Prints a bit of information about league of locales.
        """

        while True:
            Helpers.clear_screen()
            print(Colors.infoize("[About]\n"))
            print(
                f"League of Locales is a simple program that allows you to force your client to use\n" \
                "any locale you desire. It bypasses the limited locales set by your game region\n" \
                "and works in a way that DOES NOT modify any original game files.\n\nDisclaimer:\n" \
                "The very first public version of League of Locales came out nearly 3 years ago\n" \
                "and in all that time, there have been no reports of users getting banned for using it.\n" \
                "That being said, I am NOT responsible for any actions that may be taken against your\n" \
                "account for using this software or otherwise. By using this software, you understand\n" \
                "and accept these terms.\n"
            )

            print(f"[{Colors.errorize('B')}] Go back\n")
            entry = input("Entry: ").lower()

            if entry == 'b':
                break


def main():
    lol = LeagueOfLocales()
    
    while True:
        lol.startup()
        entry = input("\nInput (Default=1): ").lower()

        if entry == '1' or entry == '':
            lol.execute_client()
            print()
            for i in range(5, 0, -1):
                print(Colors.infoize(f"Program will now exit in {i} seconds, thank you for using League of Locales."), end='\r')
                time.sleep(1)
            break
        elif entry == '2':
            lol.locale_submenu()
        elif entry == '3':
            lol.updater_submenu()
        elif entry == '4':
            lol.league_folder_submenu()
        elif entry == '5':
            lol.about_submenu()
        elif entry == 'q':
            break


if __name__ == '__main__':
    main()

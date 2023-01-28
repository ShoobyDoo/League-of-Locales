# Title:        League of Locales
# File:         leagueoflocales.py
# Created:      Feb / 2020
# Modified:     Jan / 25 / 2023
# Author:       ShoobyDoo
# Description:  An easy-to-use League of Legends language/locale modifier.

# Imports
import os
import sys
import time
import shutil
import traceback
import platform
import subprocess
import configparser
import urllib.request
from io import TextIOWrapper
from zipfile import ZipFile

# Local imports
from modules.__init__ import __version__
from modules.colors import Colors
from modules.helpers import Helpers


class LeagueOfLocales(Helpers, Colors):
    def __init__(
        self,
        github_version_url="https://raw.githubusercontent.com/ShoobyDoo/League-of-Locales/master/modules/__init__.py"
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
        self.patch_method = None
        self.riot_client = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        self.latest_version = None
        self.set_window_title(f"League of Locales {__version__}")

    def print_banner(self) -> None:
        """
        ### Prints the program banner.
        """
        print(self.infoize(f"[League of Locales {__version__} by Doomlad] (Python {platform.python_version()})\n"))

    def startup(self) -> None:
        """
        ### Perform several startup functions, essentially initialize the program.
        """
        self.clear_screen()
        self.print_banner()
        self.check_update()
        self.check_config()
        self.get_menu()

    def get_latest_version(self) -> str:
        """
        ### Get the latest version from GitHub.
        """

        latest_version = str(
            urllib.request.urlopen(self.github_version_url).read().decode('utf-8')
        ).strip().split('=')[-1].replace('\'', '')

        return latest_version.strip()

    def check_update(self) -> None:
        """
        ### Check and perform an automatic update.
        ---

        Checks GitHub repo for the latest release, and if an update is available, set update_available instance variable.
        """

        print("Checking for updates...", end='')
        self.latest_version = self.get_latest_version()

        if self.compare_versions(self.latest_version, __version__):
            # Update available
            print(f"{self.affirmize(' done.')} {self.warnize('(Update available)')}")
            self.update_available = True
        else:
            print(self.affirmize(f" done."))
            self.update_available = False

    def do_update(self) -> None:
        self.check_update()
        filename = None
        if self.update_available:
            print(self.warnize("-> Update available."))
            print(self.infoize(f"-> Current version: {self.warnize(__version__)}{self.infoize(' | Latest version: ')}{self.affirmize(self.latest_version)}."))
            src_link = f"https://github.com/ShoobyDoo/League-of-Locales/releases/download/{self.latest_version}/leagueoflocales{self.latest_version}-src.zip"
            exe_link = f"https://github.com/ShoobyDoo/League-of-Locales/releases/download/{self.latest_version}/leagueoflocales{self.latest_version}.exe"
            
            time.sleep(0.5)

            print(self.infoize("-> Determining download method..."), end='')
            for entry in os.scandir():
                if entry.name.endswith(".pys"):
                    print(self.affirmize(" src."))
                    filename = f"leagueoflocales{self.latest_version}-src.zip"
                    print(self.infoize(f"-> Downloading to ./{filename}...\n{'-' * 80}"))
                    subprocess.call(f"curl -LJO {src_link}")
                    print(self.infoize('-' * 80))
                    break
                elif entry.name.endswith(".exe"):
                    print(self.affirmize(" exe."))
                    filename = f"leagueoflocales{self.latest_version}.exe"
                    print(self.infoize(f"-> Downloading to ./{filename}...\n{'-' * 80}"))
                    subprocess.call(f"curl -LJO {exe_link}")
                    print(self.infoize('-' * 80))
                    break
            print(self.affirmize(f"Download complete."))

            if filename.endswith(".zip"):
                time.sleep(0.5)

                print(self.infoize(f"-> Extracting {filename}..."), end='')
                with ZipFile(filename, 'r') as LoLocales:
                    LoLocales.extractall(filename.replace(".zip", ""))
                print(self.affirmize(" done."))

                time.sleep(0.5)

                print(self.infoize("-> Cleaning up..."), end='')
                os.remove(filename)
                print(self.affirmize(" done."))

            time.sleep(0.5)

            print(self.infoize(f"-> Update complete. Please find update \"./{filename.replace('.zip', '')}\" within your League of Locales folder ..."))
            input(self.warnize("\nPress ENTER to return to updater menu. It is recommended that you close out and launch the new version."))

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
        print(self.affirmize(" done."))
        time.sleep(1)

    def select_locale(self) -> None:
        """
        ### Initiates prompt to get users desired locale.
        """

        for idx, language in enumerate(self.all_locales.keys()):
            line = f"[{self.errorize(str(idx + 1).zfill(2)):<2}] {self.colorize(self.LIGHT_CYAN, language):<23}"
            if idx % 5 == 4:
                print(line)
            else:
                print(line, end='') if language != list(self.all_locales.keys())[-1] else print(f"{line}")

        print(f"\n[{self.errorize('B')}] Go back\n") if self.language != None else print()
        while True:
            desired_locale = input(
                f"Please ENTER the {self.colorize(self.LIGHT_CYAN, 'language')} you would like " \
                f"{self.colorize(self.LIGHT_WHITE + self.BOLD, 'OR')} the cooresponding {self.errorize('number')}.\n" \
                "Locale: "
            )

            if desired_locale.capitalize() in self.all_locales.keys():
                self.language = desired_locale.capitalize()
                try:
                    self.write_to_config('locale', self.language)
                except KeyError:
                    pass
                break

            elif str(desired_locale).isnumeric() and 1 <= int(desired_locale) <= len(self.all_locales):
                self.language = list(self.all_locales.keys())[int(desired_locale) - 1]
                try:
                    self.write_to_config('locale', self.language)
                except KeyError:
                    pass
                break

            elif desired_locale.lower() == 'b':
                if self.language == None:
                    print(self.warnize("Can't go back, this is the setup environment. Please enter a locale!"))
                else:
                    break

            else:
                print(self.warnize(
                    f"{desired_locale if desired_locale != '' else '{empty}'} is not a valid locale, try again."))

    def ensure_client_path(self, lol_directory: str) -> str:
        """
        ### Ensures the path to the client file is correct.
        ---
        Args:
            path (str): Path to the client file.

        Returns:
            str: Corrected path to the client file.
        """
        
        while True:
            if os.path.isfile(f"{lol_directory}/LeagueClient.exe"):
                print(self.affirmize("Found LeagueClient.exe! OK."))
                time.sleep(0.5)
                break
            else:
                print(self.warnize("Could not find LeagueClient.exe in given path, please try again."))
                lol_directory = input("Please enter the FULL path to your League folder. (Ex. C:/Riot Games/League of Legends)\nPath: ")
        
        return lol_directory

    def check_config(self) -> None:
        """
        ### Check for configuration.
        ---
        Checks to see if a configuration file exists, if it does read the keys otherwise prompt initial setup.
        """

        print("Checking for config...", end='')
        config = configparser.ConfigParser()

        if os.path.exists(self.config_filename):
            config.read(self.config_filename)
            try:
                self.language = config['League of Locales']['locale']
                self.lol_path = config['League of Locales']['league_directory']
                self.riot_client = config['League of Locales']['riot_client_directory']
                self.patch_method = config['League of Locales']['patch_method']
                print(self.affirmize(" done.\n"))
            except KeyError as e:
                print(self.warnize(" error."))
                print(self.warnize(f"Config file is missing key(s) {e}, please re-run setup.\n(Delete or rename lol.ini to re-run setup)\n"))

        else:
            print(f"{self.affirmize(f' done.')} {self.warnize('(Initiating first time setup...)')}\n")

            print(self.infoize("Setting up configuration...\n"))
            config.add_section('League of Locales')

            self.select_locale()

            print(self.colorize(self.LIGHT_CYAN, f"-> Locale: {self.language}"))
            config.set('League of Locales', 'locale', self.language)
            self.language = config['League of Locales']['locale']

            print(self.infoize("\nAttempting to locate your League of Legends installation automatically, please wait...\n"))
            time.sleep(1)

            riot_client_directory = self.find_directory("/Riot Games/Riot Client", suppress_drive_info=True)

            print(self.colorize(self.LIGHT_CYAN, f"-> Riot Client Directory: {riot_client_directory}"))
            config.set('League of Locales', 'riot_client_directory', riot_client_directory)
            self.riot_client = config['League of Locales']['riot_client_directory']

            lol_directory = self.find_directory("/Riot Games/League of Legends")
            lol_directory = self.ensure_client_path(lol_directory)

            print(self.colorize(self.LIGHT_CYAN, f"-> League Directory: {lol_directory}"))
            config.set('League of Locales', 'league_directory', lol_directory)
            self.lol_path = config['League of Locales']['league_directory']

            print(self.infoize("\nDetermining locale patch method..."))
            if self.get_game_region() == "garena":
                print(self.colorize(self.LIGHT_CYAN, f"-> Patch Method: sys file"))
                config.set('League of Locales', 'patch_method', 'file')
            else:
                print(self.colorize(self.LIGHT_CYAN, f"-> Patch Method: param"))
                config.set('League of Locales', 'patch_method', 'param')

            print("\nWriting configuration to file...", end='')
            with open(self.config_filename, "w+") as configfile:
                config.write(configfile)
            print(self.affirmize(" done."))

            print(self.infoize(f"\nInitial configuration is complete. Loading menu...\n"))
            time.sleep(1)

    def find_directory(self, directory: str = "/Riot Games/League of Legends", suppress_drive_info = False) -> str:
        """
        ### Finds the directory of the League of Legends installation.
        ---
        Args:
            directory (str): Path to the League of Legends installation.

        Returns:
            str: Path to the League of Legends installation.
        """

        lol_installs_found = []
        for drive_letter in self.get_drives():
            total, used, free = shutil.disk_usage(f"{drive_letter}:/")

            total_fmtd = self.colorize(self.BOLD, f"Total: {(total // (2 ** 30))} GiB")
            used_fmtd = self.warnize(f"Used: {(used // (2 ** 30))} GiB")
            free_fmtd = self.infoize(f"Free: {(free // (2 ** 30))} GiB")

            if not suppress_drive_info: print(f"Scanning drive [{drive_letter}] ... {total_fmtd:<24} | {used_fmtd:<26} | {free_fmtd:<28}")

            lol_directory = f"{drive_letter}:{directory}"
            if os.path.exists(lol_directory):
                print(self.affirmize(f"    -> Found installation @ {lol_directory}"))
                lol_installs_found.append(lol_directory)

        if len(lol_installs_found) > 1:
            print(self.warnize("Multiple installations found, please specify correct path."))
            for lol_install in lol_installs_found:
                answer = self.yes_no_prompt(f"Use {lol_install}?")
                if answer == 'Yes':
                    lol_directory = lol_install
                    break
        elif len(lol_installs_found) == 1:
            lol_directory = lol_installs_found[0]
        else:
            print(self.warnize("Could not find your installation automatically."))
        
        return lol_directory
        
    def get_game_region(self):
        file_data = self.get_sys_file()
        if "default_region: SG2" in file_data:
            return "garena"
        else:
            return "other"

    def get_sys_file(self, returns = 'raw') -> (TextIOWrapper | str | None):
        """
        ### Returns the contents of the system.yaml file.
        """

        if returns == 'raw':
            with open(f"{self.lol_path}/system.yaml", "r") as system_file:
                return system_file.read()
        elif returns == 'obj':
            return open(f"{self.lol_path}/system.yaml", "r+")

    def execute_client(self) -> None:
        """
        ### Force the client to set its locale to the users desired one; irrespective of region.
        """

        print(self.infoize(f"\n[Execute Client]\n----------------\n\nSwapping to League of Legends directory: ") + self.boldize(f"{self.lol_path}..."), end='')
        os.chdir(self.lol_path)
        print(self.affirmize(" done."))

        print(self.infoize(f"Determining patch method..."), end='')
        if self.patch_method == 'file':
            print(self.affirmize(" sysfile."))
            
            sysfile = self.get_sys_file('obj')
            file_data = sysfile.read()
            region = 'SG2'
            
            for line in file_data.splitlines():
                if line.startswith("default_region:"):
                    print(self.infoize(f"-> Found region: {self.colorize(self.LIGHT_CYAN, region)}"))
                    region = line.split(": ")[-1]

                elif line.strip() == f"{region}:":
                    print(self.infoize(f"-> Writing locale: {self.colorize(self.LIGHT_CYAN, region)} to region... "), end='')
                    file_data = file_data.replace(
                        file_data.splitlines()[file_data.splitlines().index(line) + 1], 
                        f"    available_locales:\n    - {self.all_locales[self.language]}"
                    )
                    print(self.affirmize(" done."))

                elif "default_locale:" in line:
                    file_data = file_data.replace(line, f"    default_locale: {self.all_locales[self.language]}")

            sysfile.write(file_data)
            sysfile.close()

        else:
            print(self.affirmize(" param."))

        print(self.infoize(f"Sending locale {self.language} ({self.all_locales[self.language]}) to LEAGUE client..."), end='')
        subprocess.Popen(['LeagueClient.exe', f"--locale={self.all_locales[self.language]}"])
        print(self.affirmize(" done."))

        if self.is_client_running('LeagueClient.exe'):
            print(self.affirmize(f"Client is running, client execution sucessful!"))
            return
        
        print(self.warnize("-> Using experimental Riot Client Services method (Experimental)..."))
        print(self.infoize(f"Sending locale {self.language} ({self.all_locales[self.language]}) to RIOT client..."), end='')
        subprocess.Popen(
            [
            f'{self.riot_client}\\RiotClientServices.exe', 
            "--launch-product=league_of_legends", 
            "--launch-patchline=live", 
            f"--locale={self.all_locales[self.language]}"
            ]
        )
        print(self.affirmize(" done."))
        
    def is_client_running(self, client_process: str = "LeagueClient.exe") -> bool:
        """
        ### Checks if the league client is running.
        """

        counter = 0
        while True:
            print(self.infoize(f"\rVerifying if {client_process} is running [{counter + 1}/10]..."), end='')
            if self.is_process_running(client_process):
                print(self.affirmize(" done."))
                break
            elif counter == 10:
                print(self.warnize(f"\rLeague of Locales was not able to determine if the client '{client_process}' was running within 10 seconds..."))
                break
            else:
                counter += 1
                time.sleep(1)

    def is_process_running(self, process_name: str) -> bool:
        """
        ### Checks if a process is running.
        """

        tasks = subprocess.check_output('tasklist', shell=False).decode('utf-8')
        if process_name in tasks:
            return True
        else:
            return False
    
    def get_menu(self):
        """
        ### Prints out the main menu.
        """

        self.set_window_title(f"League of Locales {__version__}")

        menu_items = [
            f"{self.boldize('Start client')}",
            f"{self.boldize('Change locale')} [{self.colorize(self.LIGHT_CYAN, self.language)}]",
            f"{self.boldize('Updater')}       [{self.affirmize('Up to Date') if not self.update_available else self.warnize('Update available')}]",
            f"{self.boldize('League Folder')} [{self.colorize(self.LIGHT_CYAN, self.lol_path)}]",
            f"{self.boldize('Client Folder')} [{self.colorize(self.LIGHT_CYAN, self.riot_client)}]",
            f"{self.boldize('About')}",
            f"{self.boldize('Quit')}"
        ]
        for idx, item in enumerate(menu_items):
            print(f"[{self.errorize(idx + 1 if item != menu_items[-1] else 'Q')}] {item}")

    def locale_submenu(self):
        """
        ### Handles functionality of the locale selector sub-menu.
        """

        self.clear_screen()
        print(self.infoize("[Change Locale]\n"))
        print(f"Current: {self.colorize(self.LIGHT_CYAN, self.language)}\n")
        self.select_locale()

    def updater_submenu(self):
        """
        ### Handles functionality of the updater sub-menu.
        """

        while True:
            self.clear_screen()
            print(self.infoize("[Updater - Experimental]\n"))
            print(f"Status: {self.affirmize('Up to Date') if self.update_available == False else self.warnize('Update available')}\n")

            print(f"[{self.errorize('1')}] Check now\n[{self.errorize('B')}] Go back\n")
            entry = input("Entry: ").lower()

            if entry == '1':
                self.do_update()
            elif entry == 'b':
                break

    def league_folder_submenu(self):
        """
        ### Handles functionality of the league folder sub-menu.
        """

        while True:
            self.clear_screen()
            print(self.infoize("[League Folder]\n"))
            print(f"Current: {self.colorize(self.LIGHT_CYAN, self.lol_path)}\n")

            print(f"[{self.errorize('1')}] Change folder\n[{self.errorize('B')}] Go back\n")
            entry = input("Entry: ").lower()

            if entry == '1':
                self.lol_path = self.ensure_client_path(self.lol_path)
                self.write_to_config('league_directory', self.lol_path)
                break
            elif entry == 'b':
                break
    
    def client_folder_submenu(self):
        """
        ### Handles functionality of the client folder sub-menu.
        """

        while True:
            self.clear_screen()
            print(self.infoize("[Client Folder]\n"))
            print(f"Current: {self.colorize(self.LIGHT_CYAN, self.riot_client)}\n")

            print(f"[{self.errorize('1')}] Change folder\n[{self.errorize('B')}] Go back\n")
            entry = input("Entry: ").lower()

            if entry == '1':
                self.riot_client = input("Please enter the FULL path to your Riot Client folder. (Ex. C:/Riot Games/Riot Client)\nPath: ")
                self.write_to_config('riot_client_directory', self.riot_client)
                break
            elif entry == 'b':
                break

    def about_submenu(self):
        """
        ### Prints a bit of information about league of locales.
        """

        while True:
            self.clear_screen()
            print(self.infoize("[About]\n"))
            print(
                f"League of Locales is a simple program that allows you to force your client to use\n" \
                "any locale you desire. It bypasses the limited locales set by your game region\n" \
                "and works in a way that DOES NOT modify any original game files.\n"
            )

            print(f"[{self.errorize('B')}] Go back\n")
            entry = input("Entry: ").lower()

            if entry == 'b': break


def main():
    while True:
        try:
            lol = LeagueOfLocales()
            lol.startup()
            entry = input("\nInput (Default=1): ").lower()

            if entry == '1' or entry == '':
                lol.execute_client()
                for i in range(15, 0, -1):
                    if i == 0: print(lol.infoize(f"Times up! Thank you for using League of Locales.                            "), end='\r')
                    print(lol.infoize(f"Program will now exit in {i} seconds, thank you for using League of Locales."), end='\r')
                    time.sleep(1)
                break
            elif entry == '2':
                lol.locale_submenu()
            elif entry == '3':
                lol.updater_submenu()
            elif entry == '4':
                lol.league_folder_submenu()
            elif entry == '5':
                lol.client_folder_submenu()
            elif entry == '6':
                lol.about_submenu()
            elif entry == 'q':
                break

        except FileNotFoundError:
            input(
                f"\n\n{LeagueOfLocales.errorize(f'League of Locales could not find your League of Legends folder. Please try again.')}\n\n" \
                f"{lol.infoize('Press ENTER to attempt a restart. (Could break the config file. If you have issues, delete lol.ini and try again.)')}"
            )
            continue

        except Exception:
            input(
                f"\n\n{LeagueOfLocales.errorize(f'A fatal error has occurred with League of Locales, copy and paste this into Doomlads Github support server.')}\n{LeagueOfLocales.errorize('Please see below for details:')}\n\n"
                f"{traceback.format_exc()}\n\n{lol.infoize('Press ENTER to attempt a restart. (Could break the config file. If you have issues, delete lol.ini and try again.)')}"
            )
            continue


if __name__ == '__main__':
    main()

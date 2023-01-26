# Title:        Helpers Class
# File:         helpers.py
# Created:      Feb / 2020
# Modified:     Sept / 11 / 2022
# Author:       ShoobyDoo
# Description:  A helper class that contains various functions.

import os
import string
from ctypes import windll
from pkg_resources import packaging


class Helpers:
    """
    A helper class that contains various different functions.
    """

    @staticmethod
    def set_window_title(new_title: str) -> None:
        """
        ### Sets the window title.
        """
        os.system(f"title {new_title}")


    @staticmethod
    def compare_versions(v1, v2) -> bool:
        """
        ### Compare two different version strings.
        ---

        Args:
            v1 (str): First version string (ex. 1.0.0-pre1)
            v2 (str): Second version string (ex. 1.2.0-pre2)

        Returns:
            bool: True if v1 > v2, False otherwise.
        """

        return packaging.version.parse(v1) > packaging.version.parse(v2)


    @staticmethod
    def yes_no_prompt(prompt: str) -> str:
        """
        ### Prompts the user for a yes or no answer.
        ---

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            str: The user's answer.
        """
        while True:
            response = input(f"{prompt}\n(Y)es/(N)o: ")
            if response.lower() in ['y', 'yes', 'n', 'no']:
                response = "Yes" if response.lower().startswith('y') else "No"
                break
        return response


    @staticmethod
    def clear_screen() -> None:
        """
        ### Clears the screen.
        """
        os.system('cls')


    @staticmethod
    def get_drives() -> list:
        """
        ### Gets all the drives on the system.

        Returns:
            list: A list of all the drives on the system.
        """
        drives = []
        bm = windll.kernel32.GetLogicalDrives() # bitmap
        for letter in string.ascii_uppercase:
            if bm & 1:
                drives.append(letter)
            bm >>= 1
        return drives
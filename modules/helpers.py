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
    def yes_no_prompt(prompt: str):
        while True:
            response = input(f"{prompt}\n(Y)es/(N)o: ")
            if response.lower() in ['y', 'yes', 'n', 'no']:
                response = "Yes" if response.lower().startswith('y') else "No"
                break
        return response


    @staticmethod
    def clear_screen():
        os.system('cls')


    @staticmethod
    def get_drives():
        drives = []
        bm = windll.kernel32.GetLogicalDrives() # bitmap
        for letter in string.ascii_uppercase:
            if bm & 1:
                drives.append(letter)
            bm >>= 1
        return drives
# Title:        Colors Helper Class
# File:         colors.py
# Created:      Feb / 2020
# Modified:     Sept / 11 / 2022
# Author:       ShoobyDoo
# Description:  A helper class to color console outputs.


class Colors:
    """ 
    ANSI color codes and related helper functions
    """

    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    RESET = "\033[0m"


    @staticmethod
    def colorize(color: str, string: str):
        """
        ### Color the given input string as the passed color parameter.
        ---

        Args:
            string (str): Input string to color

        Returns:
            str: Input string with the ANSI color code appended
        """
        return f"{color}{string}{Colors.RESET}"
    
    @staticmethod
    def boldize(string: str):
        """
        ### Shorthand for colorize bold.
        ---

        Args:
            string (str): Input string to color

        Returns:
            str: Input string colored bold
        """
        return Colors.colorize(Colors.BOLD, string)

    @staticmethod
    def infoize(string: str):
        """
        ### Shorthand for colorize purple.
        ---

        Args:
            string (str): Input string to color

        Returns:
            str: Input string colored purple
        """
        return Colors.colorize(Colors.LIGHT_PURPLE, string)
    

    @staticmethod
    def affirmize(string: str):
        """
        ### Shorthand for colorize green.
        ---

        Args:
            string (str): Input string to color

        Returns:
            str: Input string colored green
        """
        return Colors.colorize(Colors.LIGHT_GREEN, string)
    
    
    @staticmethod
    def errorize(string: str):
        """
        ### Shorthand for colorize red.
        ---

        Args:
            string (str): Input string to color

        Returns:
            str: Input string colored red
        """
        return Colors.colorize(Colors.LIGHT_RED, string)
    

    @staticmethod
    def warnize(string: str):
        """
        ### Shorthand for colorize yellow.
        ---

        Args:
            string (str): Input string to color

        Returns:
            str: Input string colored yellow
        """
        return Colors.colorize(Colors.YELLOW, string)

# from setuptools.command.easy_install import main as install
import time
import os


def prerequisites():

    os.system("cls")
    print("Checking for prerequisite...", end="")

    package = 'colorama'
    try:
        return __import__(package)

    except ImportError:
        print("Not Satisfied!\n")

        while True:
            print("You are missing the module " + package + "\n(Install once and forget about it)")
            user_input = input("\nWould you like to install it? y/n: ")

            if user_input == 'y':
                print("Installing " + package + " via pip...", end="")
                os.system("pip install " + package)
                print("Done!\nPlease restart the program.")
                counter = 4
                for count in range(3):
                    counter -= 1
                    print("Exiting in..." + str(counter), end="\r")
                    time.sleep(1)
                exit()

            elif user_input == 'n':
                print("\nThis program cannot function without colorama, please consider installing to continue.\n")
                counter = 4
                for count in range(3):
                    counter -= 1
                    print("Exiting in..." + str(counter), end="\r")
                    time.sleep(1)
                exit()

            else:
                continue

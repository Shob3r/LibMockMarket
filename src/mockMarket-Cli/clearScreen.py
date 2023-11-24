import platform
import os


# Only works in the Os console (Command prompt, Unix Terminal). displays as an error character on PyCharm
def clearScreen():
    if platform.system() != 'Windows':
        os.system('clear')
    else:
        os.system('cls')

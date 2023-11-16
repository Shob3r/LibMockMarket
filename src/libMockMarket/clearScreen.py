import platform
import os
def clearScreen():
    if platform.system() != 'Windows':
        os.system('clear')
    else:
        os.system('cls')

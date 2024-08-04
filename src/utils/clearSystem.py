import os
from platform import system
def clear_system():
    if system() == 'Windows':
        os.system('cls')

    else:
        os.system('clear')
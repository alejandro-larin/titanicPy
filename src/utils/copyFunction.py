import pyperclip
from time import sleep
from os import system
def copy_to_clipboard(text):
    pyperclip.copy(text)
    system('cls')
    sleep(1)
    print('Text copy to Clipboard')


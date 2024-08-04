import os
from time import sleep
from utils.translator import translatorHTML
from utils.copyFunction import copy_to_clipboard
from utils.clearSystem import clear_system
from utils.readHtml import read_arch_html
try:
    clear_system()

    html_content= read_arch_html()

    while True:
        clear_system()
        print('Welcome to Titanic! \n------------------------------------- \n1.FR \n2.EN \n3.PT \n')

        menu_select= int(input('Please select one option of the menu: '))

        if menu_select==1:
            clear_system()
            frHtml = translatorHTML(html_content,'fr')
            copy_to_clipboard(frHtml)

        elif menu_select==2:
            clear_system()
            enHtml = translatorHTML(html_content,'en')
            copy_to_clipboard(enHtml)
        elif menu_select==3:
            clear_system()
            ptHtml = translatorHTML(html_content,'pt')
            copy_to_clipboard(ptHtml)

        else:
            clear_system()
            print('Error of select menu')
            sleep(1)

except KeyboardInterrupt:
    clear_system()
    print('Good bye!')
    sleep(1)
    clear_system()
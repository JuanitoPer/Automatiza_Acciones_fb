import time
import pyautogui
import os
import webbrowser


time.sleep(3)

link = "https://www.google.com"

webbrowser.open_new_tab(link)

time.sleep(3)

pyautogui.hotkey('alt','tab')

time.sleep(3)

pyautogui.hotkey('alt','tab')


time.sleep(3)

for i in range(2):
    pyautogui.keyDown("alt")
    time.sleep(.3)
    pyautogui.hotkey('tab')
pyautogui.keyUp("alt")




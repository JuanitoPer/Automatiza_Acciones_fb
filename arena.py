import pyautogui
import time

#esto ejecuta algo simple
caja = (500, 500)
barra = (500, 500)

#desde aqui comienza la automatizacion
time.sleep(1)

pyautogui.click(caja)
#luego hacemos algun scroll
pyautogui.scroll(-500)
time.sleep(1)
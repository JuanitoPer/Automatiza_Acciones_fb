import pyautogui
import time as t

recorrido_grupos = 5
recorrido_gral = 15



acepta_cookie = (1651, 883)

cierra_grupo = (126, 249)
abre_grupo = (100, 296)

t.sleep(3)

#recorre para aceptar
t.sleep(.5)
for i in range(recorrido_grupos):

    for i in range(recorrido_gral):
        t.sleep(5)
        pyautogui.click(acepta_cookie)
        t.sleep(1)
        pyautogui.press("esc")
        pyautogui.hotkey('ctrl', 'pagedown')
        t.sleep(.5)

    pyautogui.click(cierra_grupo)
    t.sleep(5)
    pyautogui.click(abre_grupo)
    t.sleep(1)



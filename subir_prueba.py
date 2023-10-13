import pyautogui
import time
import tkinter as tk
from tkinter import filedialog
import pyperclip
import csv


#Coordenadas 

carita = (1732, 67)
create_identity= (1292, 725)
custom = (1546, 291)
click_color = (1361, 346)
color = ("#92B57A","#12541s")
id = (1374, 346)
password = (1401, 429)
barra = (1007, 73)
caja_Equis = (608, 259)

#para los proxys se agrega un numero para definir cual es el que se necesita
proxy = (1370, 560)
proxys_consecutivo = ("75")
#pendiente ponerlo correcto 
save = (1351, 704)

#Parte2 del login
link_face = ("https://es-la.facebook.com/")



nombres = ["nombre1:nombre2:nombre3:nombre4:nombre5:nombre6:nombre7"]

# Leer las credenciales desde el archivo CSV
credenciales = []
with open("C:\\Users\\alber\\Documents\\CLOUD\\Automatizaciones\\data.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        credenciales.append(fila)






#Comienza la automatizacion
time.sleep(3)
# Inicializar el contador
contador = 0


# Iterar sobre cada nombre en la lista "nombres"
for nombre in nombres:
    valores = nombre.split(":")
    
    # Ejecutar las acciones para cada conjunto de valores
    for valor in valores:
        time.sleep(3)
        pyautogui.click(carita)
        time.sleep(3)
        pyautogui.click(create_identity)
        time.sleep(3)
        
        pyperclip.copy(valor.strip())
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Agregar proxyvalor2
        pyautogui.click(proxy)
        time.sleep(1)
        pyautogui.write(proxys_consecutivo)
        time.sleep(1)
        pyautogui.press('enter')

        
        # Definir color
        time.sleep(1)
        pyautogui.click(custom)
        time.sleep(1)
        pyautogui.click(click_color)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.2)
        pyautogui.press('delete')
        pyautogui.write(color)
        time.sleep(1)
        pyautogui.click(save)
        time.sleep(1)

        # Hacer otras acciones...

        pyautogui.click(barra)
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.2)
        pyautogui.press('delete')
        time.sleep(.2)
        pyautogui.typewrite(link_face)
        time.sleep(.1)
        pyautogui.press('enter')
        time.sleep(2)

        # Si ya se han realizado las acciones de pegado en esta vuelta, incrementar el contador y avanzar
        if contador < len(credenciales):
            usuario, contraseña, twofa = credenciales[contador]

            pyautogui.click(id)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            pyperclip.copy(usuario.strip())
            pyautogui.hotkey("ctrl", "v")
            time.sleep(2)

            pyautogui.click(password)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            pyperclip.copy(contraseña.strip())
            pyautogui.hotkey("ctrl", "v")
            time.sleep(2)

            # Aquí podrías continuar con las acciones para el 2FA y otros pasos...

            # Esperar después de cada iteración
            time.sleep(1)

            # Incrementar el contador
            contador += 1






        #esperar el resultado del 2FA

            

            

        # Esperar después de cada iteración
    time.sleep(1)  # Ajusta el tiempo según tu necesidad
    


            







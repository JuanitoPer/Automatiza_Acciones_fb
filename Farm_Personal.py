from tkinter import filedialog
import pyautogui
import time
import pyperclip
import os
import csv



# barra = (646, 52)
barra = (674, 235)
caja_Equis = (245, 319)
caja_coments = (816, 198)



usuarios_url = [

    
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    
    # Agrega más URLs de usuarios aquí
]


# Función para abrir la página de usuarios
def abrir_pagina_usuarios(usuarios_url):
    pyautogui.click(barra)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.typewrite(usuarios_url)
    pyautogui.press('enter')
    time.sleep(3)




time.sleep(5)   



# Leer el archivo CSV y almacenar las líneas en una lista
ruta_archivo = "C:\\Users\\alber\\Documents\\CLOUD\\Automatizaciones\\Farm\\farms1.csv"
with open(ruta_archivo, "r") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    lineas_csv = list(lector)


# Initialize a dictionary to keep track of the last processed line for each user URL
# Abrir la página con los usuarios
last_processed_line = {}


# Ciclo para cada conjunto de usuarios (3 usuarios)
for index, usuarios_url in enumerate(usuarios_url):
    # Check if we have a record of the last processed line for this user URL
    if usuarios_url in last_processed_line:
        ultima_linea_usuario = last_processed_line[usuarios_url]
    else:
        ultima_linea_usuario = index * 3  # Initialize based on index

    abrir_pagina_usuarios(usuarios_url)
    time.sleep(5)  # Esperar a que la página cargue

    # Contador para llevar el registro de comentarios hechos
    comentarios_hechos = 0

    # Ciclo para repetir el proceso 3 veces
    for _ in range(3):  # Iterate 3 times
        if ultima_linea_usuario >= len(lineas_csv):  # Break the loop if there are no more lines
            break

        # Get the current line
        linea = lineas_csv[ultima_linea_usuario]
        comentario = linea[0].strip()
        ruta_archivo = linea[1].strip()

        pyautogui.click(caja_coments)
        time.sleep(.2)

        # Escribir el comentario
        pyperclip.copy(comentario)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)

        # Ciclo para acceder a los archivos
        for i in range(4):
            pyautogui.hotkey('tab')
            time.sleep(1)
        pyautogui.press('enter')

        # Segunda parte de archivos
        time.sleep(2)
        pyautogui.click(caja_Equis)
        for i in range(3):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        pyautogui.press('enter')

        # Escribir la ruta del archivo
        time.sleep(2)
        pyperclip.copy(ruta_archivo)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        time.sleep(10)

        # Ciclo para acceder a previsualización
        pyautogui.click(caja_Equis)
        for i in range(6):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        pyautogui.press('enter')

        time.sleep(8)
        pyautogui.click(caja_Equis)

        # Ciclo para presionar el botón de comentar
        for i in range(11):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        #pyautogui.press('enter')

        # Esperar antes de repetir para el mismo usuario pero diferente comentario
        time.sleep(5)

        # Incrementar el contador de comentarios hechos
        comentarios_hechos += 1
        url_actual = usuarios_url
        abrir_pagina_usuarios(url_actual)

        # Incrementar el contador de comentarios hechos
        ultima_linea_usuario += 1  # Update the last processed line

    # Update the last processed line for this user URL
    last_processed_line[usuarios_url] = ultima_linea_usuario

    # After completing a user URL, switch to the next USER
    pyautogui.hotkey('ctrl', 'pagedown')
import pyautogui
import time
import pyperclip
import csv
import random

# Define las coordenadas de los elementos en la pantalla
Primer_Elemento = (334, 306)

# Función para pegar comentario y ruta de archivo
def pegar_comentario_y_ruta(comentarios):
    # Selecciona uno de los comentarios aleatoriamente
    comentario_aleatorio = random.choice(comentarios[0:3])

    time.sleep(5)
    # Pulsar tabulaciones para llegar a la ubicación adecuada
    # Modificar secuencia del primer al segundo elemento
    pyautogui.click(Primer_Elemento)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.3)
    pyautogui.hotkey('alt', 'tab')

    # Pendiente cambiar tiempo
    time.sleep(10)
    # Pegar el comentario aleatorio
    pyperclip.copy(comentario_aleatorio)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.3)
    pyautogui.hotkey("enter")

# Procesar usuarios desde un archivo CSV
ruta_archivo = "C:\\Users\\alber\\Documents\\CLOUD\\Automatizaciones\\Farm\\Pega_Ima_Coment.csv"
with open(ruta_archivo, "r", encoding="utf-8-sig") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    lineas_csv = list(lector)

# Realizar acciones para cada usuario
for linea in lineas_csv:
    comentarios = linea[1:]  # Obtén los comentarios de la segunda columna en adelante
    pegar_comentario_y_ruta(comentarios)

    ruta = linea[0].strip()
    comentario_aleatorio = random.choice(comentarios[0:3])
   
    print("Comentario: '{}'".format(comentario_aleatorio))

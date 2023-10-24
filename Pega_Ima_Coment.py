import tkinter as tk
import pyautogui
import time
import pyperclip
import csv
import random


#barra = (1302, 291)

#barra = (1302, 291)

# Define las coordenadas de los elementos en la pantalla
barra = (1230, 403)
caja_Equis = (156, 320)


# Función para abrir la página de usuarios
def abrir_pagina_usuarios(url):
    pyautogui.click(barra)
    time.sleep(.3)
    #pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    time.sleep(.3)
    pyautogui.typewrite(url)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(.3)
    pyautogui.hotkey('ctrl', 'pagedown')
    time.sleep(1)




# Función para pegar comentario y ruta de archivo
def pegar_comentario_y_ruta(comentarios, ruta):
    tab_interval = .3  # Intervalo entre pulsaciones de tabulación

    # Seleccionar un comentario aleatorio de la fila
    # Selecciona uno de los comentarios 
    comentario_aleatorio = random.choice(comentarios[0:3])  
    

    pyautogui.click(caja_Equis)

    time.sleep(tab_interval)
    # Pulsar tabulaciones para llegar a la ubicación adecuada
    for _ in range(3):
        pyautogui.hotkey('tab')
        time.sleep(tab_interval)

    # Pegar el comentario aleatorio
    pyperclip.copy(comentario_aleatorio)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.3)

    # Acceder para seleccionar el archivo
    for _ in range(2):
        pyautogui.hotkey('tab')
        time.sleep(tab_interval)
    pyautogui.press('enter')

    # Pegar la ruta
    time.sleep(2)
    pyperclip.copy(ruta)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.3)

    # Presionar Enter para enviar el comentario
    pyautogui.hotkey('tab')
    pyautogui.press('enter')
    time.sleep(1)
    
    pyautogui.hotkey('ctrl', 'pagedown')

# Función para procesar un usuario y su información desde el archivo CSV
def procesar_usuario(lineas_csv):
    for linea in lineas_csv:
        ruta = linea[0].strip()  # Obtén la ruta de la primera columna
        comentarios = linea[1:]  # Obtén los comentarios de la segunda columna en adelante
        pegar_comentario_y_ruta(comentarios, ruta)

# Función para iniciar la ejecución
def start_execution():
    url = url_entry.get()
    ruta_archivo = "C:\\Users\\alber\\Documents\\CLOUD\\Automatizaciones\\Farm\\Pega_Ima_Coment.csv"
    with open(ruta_archivo, "r", encoding="utf-8-sig") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        lineas_csv = list(lector)

    num_repeticiones = len(lineas_csv)

    for _ in range(num_repeticiones):
        time.sleep(1)
        abrir_pagina_usuarios(url)

            
        # Imprime la ruta y el comentario que se utilizó
    for linea in lineas_csv:
        ruta = linea[0].strip()
        comentarios = linea[1:]
        comentario_aleatorio = random.choice(comentarios[0:3])

        print("Ruta: '{}'" .format(ruta))
        print("Comentario: '{}'".format(comentario_aleatorio))





    reinicio = False

    # Ciclo para acceder a la posición inicial
    for _ in range(num_repeticiones):
        # Activa el atajo para copiar la URL actual en la barra de direcciones (Ctrl + L y luego Ctrl + C)
        pyautogui.hotkey('ctrl', 'shift', 'pageup')
        time.sleep(.1)
        pyautogui.click(barra)
        time.sleep(.1)
        #pyautogui.hotkey('ctrl', 'l')
        time.sleep(.1)
        #pyautogui.hotkey('ctrl', 'c')
        time.sleep(.1)

        # Obtén la URL copiada del portapapeles utilizando Pyperclip
        copied_url = pyperclip.paste()

        # Realiza acciones con la URL copiada
        # Por ejemplo, compara la URL con otra y toma acciones en consecuencia
        if url in copied_url:
            # La URL coincide con lo que buscas, establece la etiqueta 'reinicio' en True
            reinicio = True
            continue
        else:
            print("----Se eliminó " + copied_url + "----")
            # La URL no coincide, cierra la pestaña actual (Ctrl + W)
            #pyautogui.hotkey('ctrl', 'w')
            num_repeticiones -= 1
            time.sleep(1)

        # Si la etiqueta 'reinicio' es True, continúa con la siguiente repetición
        if reinicio:
            reinicio = False
            continue

    

    






    # Procesar a los usuarios
    procesar_usuario(lineas_csv)

    #Hay que revisar este print
    



# Crear la ventana tkinter
root = tk.Tk()
root.title("Automatización de Comentarios")
root.geometry("600x250")

# Crear una entrada para la URL
url_label = tk.Label(root, text="Ingresa la URL:", font=("Helvetica", 12))
url_label.pack()
url_entry = tk.Entry(root, font=("Helvetica", 12))
url_entry.pack()

# Crear un botón para iniciar la ejecución
start_button = tk.Button(root, text="Iniciar Ejecución", command=start_execution, font=("Helvetica", 12))
start_button.pack()

root.mainloop()

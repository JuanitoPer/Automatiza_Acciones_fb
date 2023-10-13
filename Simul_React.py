import csv
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
import pyperclip
import datetime




barra = (1007, 73)
caja_Equis = (236, 424)


# Función para ejecutar las acciones de las reacciones
def execute_reactions(link, like, love, importa, asombra):
    repetitions = int(like) + int(love) + int(importa) + int(asombra)

    # Ciclo para pegar las ligas en la barra de URLs
    for _ in range(repetitions):
        time.sleep(1)
        pyautogui.click(barra)
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.2)
        pyautogui.press('delete')
        time.sleep(.2)
        pyautogui.typewrite(link)
        time.sleep(10)
        pyautogui.press('enter')
        time.sleep(.3)
        pyautogui.hotkey('ctrl', 'pagedown')
        time.sleep(1)  # Wait between iterations

    reinicio = False

    # Ciclo para acceder a la posición inicial
    for _ in range(repetitions):
        # Activa el atajo para copiar la URL actual en la barra de direcciones (Ctrl + L y luego Ctrl + C)
        pyautogui.hotkey('ctrl', 'shift', 'pageup')
        time.sleep(.2)
        pyautogui.click(barra)
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(.2)

        # Obtén la URL copiada del portapapeles utilizando Pyperclip
        copied_url = pyperclip.paste()

        # Realiza acciones con la URL copiada
        # Por ejemplo, compara la URL con otra y toma acciones en consecuencia
        if link in copied_url:
            # La URL coincide con lo que buscas, establece la etiqueta 'reinicio' en True
            reinicio = True
            continue
        else:
            print("----Se eliminó " + copied_url + "----")
            # La URL no coincide, cierra la pestaña actual (Ctrl + W)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(.2)

        # Si la etiqueta 'reinicio' es True, continúa con la siguiente repetición
        if reinicio:
            reinicio = False
            continue

    #para hacer la reaccion para cada reaccion hay que hacer una condicional que verifique el numero de reacciones en cada input y lo ejecute y si no que avance a la siguiente reaccion

    
    
        # Obtén la hora actual
        hora_actual = datetime.datetime.now()

        # Formatea la hora actual como una cadena de texto
        hora_formateada = hora_actual.strftime("%H:%M:%S")
        print("LINK: " + link + " SOLO_LIKES: " + str(repetitions) + " Hora: " + hora_formateada)

    time.sleep(.2)
    # Bucle para el "like"
    for _ in range(int(like)):
        time.sleep(.2)
        pyautogui.click(caja_Equis)
        time.sleep(.2)
        # Accediendo a la reacción
        for i in range(2):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'pagedown')


    time.sleep(.2)
    # Bucle para el "love"
    for _ in range(int(love)):
        time.sleep(.2)
        pyautogui.click(caja_Equis)
        time.sleep(.2)
        # Accediendo a la reacción
        for i in range(3):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'pagedown')



    time.sleep(.2)
    # Bucle para el "me importa"
    for _ in range(int(importa)):
        time.sleep(.2)
        pyautogui.click(caja_Equis)
        time.sleep(.2)
        # Accediendo a la reacción
        for i in range(4):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'pagedown')

    # Bucle para el "me asombra"
    for _ in range(int(asombra)):
        time.sleep(.2)
        pyautogui.click(caja_Equis)
        time.sleep(.2)
        # Accediendo a la reacción
        for i in range(6):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'pagedown')            


    
# Función para mostrar un cuadro de diálogo de confirmación
def confirm_execution():
    result = messagebox.askyesno("Confirmación", "¿Deseas ejecutar las acciones?")
    if result:
        archivo_csv = 'C:\\Users\\alber\\Documents\\CLOUD\\Script\\acciones.csv'  # Reemplaza con la ubicación de tu archivo CSV

        with open(archivo_csv, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Saltar la primera fila con encabezados
            for row in reader:
                link, like, love, importa, asombra = row
                execute_reactions(link, like, love, importa, asombra)
                # Imprimir el número de fila consecutiva y el número total de acciones
                
    
    else:
        messagebox.showinfo("Información", "Ejecución cancelada")

# Crear una ventana de tkinter
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Mostrar el cuadro de diálogo de confirmación
confirm_execution()

# Salir de la aplicación
root.destroy()


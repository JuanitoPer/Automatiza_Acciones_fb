import csv
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
import pyperclip
import datetime

barra = (1213, 68)
caja_Equis = (236, 424)


time.sleep(5)



def execute_reactions(rows):
    for row in rows:
        link = row[0]
        comments = [comment for comment in row[1:] if comment.strip()]  # Filtrar comentarios vacíos
        comment_count = len(comments)  # Contar la cantidad de comentarios en esta fila

        # Ciclo para pegar el mismo enlace el número de veces correspondiente
        for _ in range(comment_count):
            # Pegar el enlace de la fila actual
            time.sleep(1)
            pyautogui.click(barra)
            time.sleep(.2)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(.2)
            pyautogui.press('delete')
            time.sleep(.2)
            pyautogui.typewrite(link)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(.1)
            pyautogui.hotkey('ctrl', 'pagedown')
            time.sleep(2)  # Espera entre iteraciones

        # Ciclo para acceder a la posición inicial
        for _ in range(comment_count):
            pyautogui.hotkey('ctrl', 'shift', 'pageup')
            time.sleep(.2)

        # Pegar todos los comentarios de la fila actual
        for comment in comments:
            pyautogui.click(caja_Equis)
            time.sleep(.2)
            # Acceder a la caja de comentarios
            for i in range(3):
                pyautogui.hotkey('tab')
                time.sleep(.2)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(.2)
            pyautogui.press('delete')
            time.sleep(.2)

            # Copiar el contenido del comentario al portapapeles
            pyperclip.copy(comment.strip())
            time.sleep(.2)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(.2)

            # Comentar
            for i in range(3):
                pyautogui.hotkey('tab')
                time.sleep(.2)
            pyautogui.press('enter')
            time.sleep(.2)
            pyautogui.hotkey('ctrl', 'pagedown')
            time.sleep(2)

        pyautogui.hotkey('ctrl', 'pagedown')


        
        # Obtén la hora actual
        hora_actual = datetime.datetime.now()

        # Formatea la hora actual como una cadena de texto
        hora_formateada = hora_actual.strftime("%H:%M:%S")
        print("LINK: " + link + " SOLO_LIKES: " + str(comment_count) + " Hora: " + hora_formateada)
# Función para mostrar un cuadro de diálogo de confirmación
def confirm_execution():
    result = messagebox.askyesno("Confirmación", "¿Deseas ejecutar las acciones?")
    if result:  
        archivo_csv = 'C:\\Users\\alber\\Documents\\CLOUD\\Script\\coments_simul.csv'  
        
        # Reemplaza con la ubicación de tu archivo CSV

        with open(archivo_csv, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Saltar la  primera fila con encabezados

            rows = list(reader)  # Leer todas las filas del CSV
            execute_reactions(rows)
    else:
        messagebox.showinfo("Información", "Ejecución cancelada")

# Crear una ventana de tkinter
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Mostrar el cuadro de diálogo de confirmación
confirm_execution()

# Salir de la aplicación
root.destroy()

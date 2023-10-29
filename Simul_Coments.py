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
            pyperclip.copy(link)
            time.sleep(.1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(.1)
            pyautogui.press('enter')
            time.sleep(.1)
            pyautogui.hotkey('ctrl', 'pagedown')
            time.sleep(1)  # Espera entre iteraciones

        
        # Etiqueta para el bucle exterior
        reinicio = False

        # Ciclo para acceder a la posición inicial
        for _ in range(comment_count):
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
                comment_count -= 1
                time.sleep(.2)

            # Si la etiqueta 'reinicio' es True, continúa con la siguiente repetición
            if reinicio:
                reinicio = False
                continue

                #para hacer la reaccion para cada reaccion hay que hacer una condicional que verifique el numero de reacciones en cada input y lo ejecute y si no que avance a la siguiente reaccion


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

        print("--- " + str(comment_count)+ " Comentarios---")



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

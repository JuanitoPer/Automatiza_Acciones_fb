import pyautogui
import time
import tkinter as tk
from tkinter import filedialog





# Coordenadas de las cajas en la interfaz gráfica
caja = (990, 65)          # Coordenadas para pegar la un comentario
caja_equis = (307, 425)   # Coordenadas para hacer un clic antes de hacer un ciclo







# Función para obtener la ruta del archivo de texto/csv
def obtener_ruta():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    caja_ruta.delete(0, tk.END)
    caja_ruta.insert(tk.END, ruta_archivo)

# Función para ejecutar el script
def ejecutar_script():
    try:
        # Ruta del archivo de texto con las URLs
        archivo_urls = caja_ruta.get()

        # Leer los comentarios desde el archivo de texto
        with open(archivo_urls, 'r', encoding='utf-8') as file:
            urls = [url.strip() for url in file.readlines()]

        # Obtener el número de repeticiones y de links desde la GUI
        try:
            numero_repeticiones = int(caja_repeticiones.get())
        except ValueError:
            print("Ingrese un número entero válido en Repeticiones.")
            return

        numero_links = caja_links.get()  # No necesita validación aquí, ya que se espera un valor de texto
    




        #PRIMERO ESCRIBE LA RUTA Y LUEGO ACCEDE PARA PONER VALORES Y LUEGO ACCIONAR
        # Bucle para escribir un comentario
        for url in urls:
            time.sleep(3)

            # Bucle para pegar las URLs y cambiar de pestaña
            for _ in range(numero_repeticiones):
                # Obtener la URL de la caja "Número de Links" en la GUI
                url = caja_links.get()

                # Pegar la URL en la barra de direcciones
                pyautogui.click(caja)  # Hacer clic en la barra de direcciones
                pyautogui.hotkey("ctrl", "a")  # Seleccionar todo en la barra de direcciones
                time.sleep(.5)
                pyautogui.press("delete")  # Borrar la URL actual
                time.sleep(.5)
                pyautogui.write(url)  # Escribir la URL
                pyautogui.press('enter')  # Presionar Enter
                time.sleep(.5)  # Esperar a que cargue la página
                pyautogui.hotkey('ctrl', 'tab')  # Cambiar de pestaña
                time.sleep(.2)

                #Esto es para regresar al punto inicial de las pestañas
                time.sleep(.2)
                for i in range(numero_repeticiones):
                    time.sleep(.2)
                    pyautogui.hotkey('ctrl', 'shift', 'tab')  
                    time.sleep(.2)


            time.sleep(.5)
            # Simular clic en la "X" para borrar el texto existente
            pyautogui.click(caja_equis)
            time.sleep(.2)
            # Simular el proceso de escribir y enviar comentario
            for i in range(5):
                time.sleep(.3)
                pyautogui.hotkey('tab')
                
            
            time.sleep(.2)
            

            #Escribe el comentario del txt1
            pyautogui.write("MUY BUEN TRABAJO EL QUE HAY EN VALLARTA")
            
            time.sleep(.2)
            
            for i in range(4):
                pyautogui.hotkey('tab')
                time.sleep(0.2)
            
            time.sleep(0.2)
            pyautogui.hotkey('enter')
            time.sleep(0.2)
            pyautogui.click(caja_equis)
            time.sleep(.5)

            #Seleccionar archivo
            for i in range(4):
                pyautogui.hotkey('tab')
                time.sleep(0.2)

            pyautogui.hotkey('enter')

            
            #Escribir la ruta del txt2
            pyautogui.write("C:\\Users\\alber\\Desktop\\MUCHO TRABAJO.png")
            time.sleep(1)
            pyautogui.hotkey('enter')
            time.sleep(3)


            #accede a previsualizar
            pyautogui.click(caja_equis)
            for i in range(6):
                pyautogui.hotkey('tab')
                time.sleep(0.2)

            pyautogui.hotkey('enter')

            time.sleep(3)
            #Publicar
            pyautogui.click(caja_equis)
            for i in range(11):
                pyautogui.hotkey('tab')
                time.sleep(0.2)
            #pyautogui.hotkey('enter')

            time.sleep(30)
            

    except Exception as e:
        print("Error:", str(e))

# Crear la ventana de la interfaz de usuario
ventana = tk.Tk()
ventana.title("Comentar")
ventana.geometry("1000x400")

# Etiqueta y caja de entrada para la ruta del archivo
etiqueta_ruta = tk.Label(ventana, text="Ruta del archivo", fg="blue", font=("Helvetica", 16, "bold"))
etiqueta_ruta.pack()

caja_ruta = tk.Entry(ventana, width=50)
caja_ruta.pack()
caja_ruta.config(font=("Helvetica", 15))
# Botón para seleccionar el archivo
boton_ruta = tk.Button(ventana, text="Seleccionar archivo", command=obtener_ruta, fg="brown", font=("Helvetica", 16, "bold"))
boton_ruta.pack()

# Etiqueta y caja de entrada para el número de repeticiones
etiqueta_repeticiones = tk.Label(ventana, text="Repeticiones", fg="blue", font=("Helvetica", 16, "bold"))
etiqueta_repeticiones.pack()

caja_repeticiones = tk.Entry(ventana, width=40)
caja_repeticiones.pack()
caja_repeticiones.config(font=("Helvetica", 30))

# Etiqueta y caja de entrada para el número de links
etiqueta_links = tk.Label(ventana, text="Link", fg="blue", font=("Helvetica", 16, "bold"))
etiqueta_links.pack()

caja_links = tk.Entry(ventana, width=110)
caja_links.pack()
caja_links.config(font=("Helvetica", 20))

# Botón para ejecutar el script
boton_ejecutar = tk.Button(ventana, text="Ejecutar", command=ejecutar_script, fg="red", font=("Helvetica", 16, "bold"))
boton_ejecutar.pack()

# Ejecutar el bucle principal de la interfaz de usuario
ventana.mainloop()
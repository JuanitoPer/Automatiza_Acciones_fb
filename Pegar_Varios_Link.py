import pyautogui
import time
import tkinter as tk
from tkinter import filedialog
import pyperclip


caja = (990, 65)





def obtener_ruta():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    caja_ruta.delete(0, tk.END)
    caja_ruta.insert(tk.END, ruta_archivo)
    return ruta_archivo


# Función para ejecutar el script
def ejecutar_script():
    # Ruta del archivo de texto
    archivo_urls = caja_ruta.get()
    start_line = int(start_line_entry.get())
    end_line = int(end_line_entry.get())

    # Abrir el archivo de texto y leer las URLs con codificación UTF-8
    with open(archivo_urls, 'r', encoding='utf-8') as file:
        urls = file.readlines()

    # Eliminar los caracteres de nueva línea ('\n') al final de cada línea
    urls = [url.strip() for url in urls]

    #Empezar script

    time.sleep(3)
    for url in urls[start_line-1:end_line]:
        # Click en la barra de direcciones y pegar la URL
        pyautogui.click(caja)
        time.sleep(.1) 
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.2) 
        pyautogui.press("delete")
        time.sleep(.2)  
        pyperclip.copy(url)
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.1)
        # Cambiar de pestaña
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(1)
        

# Crear la ventana de la interfaz de usuario
ventana = tk.Tk()
ventana.title("Pega_URLS")
ventana.geometry("800x400")
# Colores personalizados
bg_color = "#F0F0F0"
button_color = "#4CAF50"
text_color = "#333333"

# Etiqueta y caja de entrada para la ruta del archivo
etiqueta_ruta = tk.Label(ventana, text="Ruta del archivo:")
etiqueta_ruta.pack()

caja_ruta = tk.Entry(ventana, width=40)
caja_ruta.pack()




# Botón para seleccionar el archivo
boton_ruta = tk.Button(ventana, text="Seleccionar archivo", command=obtener_ruta)
boton_ruta.pack()





# Agregar entradas para las líneas de inicio y fin
start_line_label = tk.Label(ventana, text="Línea de inicio:", bg=bg_color, fg="blue", font=("Helvetica", 16, "bold"))
start_line_label.pack()

start_line_entry = tk.Entry(ventana, width=10, font=("Helvetica", 16, "bold"))
start_line_entry.pack()

end_line_label = tk.Label(ventana, text="Línea de fin:", bg=bg_color, fg="blue", font=("Helvetica", 16, "bold"))
end_line_label.pack()

end_line_entry = tk.Entry(ventana, width=10, font=("Helvetica", 16, "bold"))
end_line_entry.pack()

# Botón para ejecutar el script
boton_ejecutar = tk.Button(ventana, text="Ejecutar", command=ejecutar_script)
boton_ejecutar.pack()


# Ejecutar el bucle principal de la interfaz de usuario
ventana.mainloop()

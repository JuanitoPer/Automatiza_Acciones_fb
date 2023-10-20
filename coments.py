import tkinter as tk
from tkinter import filedialog
import pyautogui
import time
import pyperclip
import datetime


barra = (1007, 73)
caja_Equis = (156, 320)




def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def start_execution():
    start_line = int(start_line_entry.get())
    end_line = int(end_line_entry.get())
    repetitions = (end_line - start_line)+1
    
    
    link = link_entry.get()
    
    with open(file_entry.get(), 'r', encoding='utf-8') as file:
        content = file.readlines()

    content = content[start_line-1:end_line]  # Leer solo las líneas especificadas


    
    #Ciclo para pegar las ligas en la barra de urls
    time.sleep(2)  
    for _ in range(repetitions):
        time.sleep(.1)
        pyautogui.click(barra)
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.2)
        pyautogui.press('delete')
        time.sleep(.2)  
        pyperclip.copy(link)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.1)
        pyautogui.hotkey('ctrl', 'pagedown')
        time.sleep(1)  


    reinicio = False
    # ... Tu código previo ...

    # Ciclo para acceder a la posición inicial
    for _ in range(repetitions):
        # Activa el atajo para copiar la URL actual en la barra de direcciones (Ctrl + L y luego Ctrl + C)
        pyautogui.hotkey('ctrl', 'shift', 'pageup')
        time.sleep(.2)
        pyautogui.click(barra)
        pyautogui.hotkey('ctrl', 'l')
        
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

            print("---- Se eliminó " + copied_url + "----")
            
            # La URL no coincide, cierra la pestaña actual (Ctrl + W)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)
            repetitions -= 1  # Resta 1 a la variable 'repetitions'

        # Si la etiqueta 'reinicio' es True, continúa con la siguiente repetición
        if reinicio:
            reinicio = False
            continue


    time.sleep(1)
    #ciclo para aceder al comentario

    for comment in content:
        pyautogui.click(caja_Equis)
        time.sleep(.2)
        
        #Accede a caja comentario
        for i in range(3):  
            pyautogui.hotkey('tab')
            time.sleep(.2)
        

        # Copia el contenido del comentario al portapapeles
        pyperclip.copy(comment.strip())
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(.2)





        #REVISAR LOS TABS EN WEB
        #REVISAR LAS MAYUSCULAS YA QUE NO TOMA EL MBASIC
        #Comentar 
        for i in range(3):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.2)

        pyautogui.hotkey('ctrl', 'pagedown')
        time.sleep(2)




# Create the main window
root = tk.Tk()
root.title("Comentar")
root.geometry("600x500+500+400")

# Colores personalizados
bg_color = "#F0F0F0"
button_color = "#4CAF50"
text_color = "#333333"

# Estilos
root.configure(bg=bg_color)
file_label = tk.Label(root, text="Selecciona Archivo:", bg=bg_color, fg="blue", font=("Helvetica", 16, "bold"))
file_label.pack()

file_entry = tk.Entry(root, width=100, font=("Helvetica", 16, "bold"))
file_entry.pack()

file_button = tk.Button(root, text="Abrir", command=open_file, bg=button_color, fg="white", font=("Helvetica", 16, "bold"))
file_button.pack()





link_label = tk.Label(root, text="Link:", bg=bg_color, fg="blue", font=("Helvetica", 18, "bold"))
link_label.pack()

link_entry = tk.Entry(root, width=100, font=("Helvetica", 16, "bold"))
link_entry.pack()



# Agregar entradas para las líneas de inicio y fin
start_line_label = tk.Label(root, text="Línea de inicio:", bg=bg_color, fg="blue", font=("Helvetica", 16, "bold"))
start_line_label.pack()

start_line_entry = tk.Entry(root, width=10, font=("Helvetica", 16, "bold"))
start_line_entry.pack()

end_line_label = tk.Label(root, text="Línea de fin:", bg=bg_color, fg="blue", font=("Helvetica", 16, "bold"))
end_line_label.pack()

end_line_entry = tk.Entry(root, width=10, font=("Helvetica", 16, "bold"))
end_line_entry.pack()


# Agregar un espaciador en blanco
blank_space_label = tk.Label(root, text="", bg=bg_color)
blank_space_label.pack()
# Agregar un espaciador en blanco
blank_space_label = tk.Label(root, text="", bg=bg_color)
blank_space_label.pack()



# Run the main loop
start_button = tk.Button(root, text="Ejecutar", command=start_execution, bg=button_color, fg="white", font=("Helvetica", 12, "bold"))
start_button.pack()


root.mainloop() 
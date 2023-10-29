import tkinter as tk
from tkinter import filedialog
import pyautogui
import time
import pyperclip
import datetime




#Esta accion pega comentarios de volada
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def start_execution():
    start_line = int(start_line_entry.get())
    end_line = int(end_line_entry.get())
    speed = int(speed_entry.get())  # Obtén la velocidad de ejecución
    
    
    with open(file_entry.get(), 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    # Asegurémonos de que las líneas estén dentro de los límites del archivo
    start_line = max(1, start_line)
    end_line = min(end_line, len(content))

    
    time.sleep(5)
    for line_num in range(start_line -1 , end_line +1):
        line = content[line_num]
        
        # Copia el contenido de la línea al portapapeles
        pyperclip.copy(line.strip())
        
        # Pega el contenido en la barra de direcciones (u otro lugar según tu necesidad)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey("enter")
        
        time.sleep(speed)  
        # Convierte la velocidad a segundos



# Create the main window
root = tk.Tk()
root.title("Comentarios_Rapidos")
root.geometry("600x500+500+400")

# Colores personalizados
bg_color = "#F0F0F0"
button_color = "#4CAF50"
text_color = "#333333"

# Estilos
root.configure(bg=bg_color)
file_label = tk.Label(root, text="Selecciona Archivo:", bg=bg_color, fg="red", font=("Helvetica", 16, "bold"))
file_label.pack()

file_entry = tk.Entry(root, width=100, font=("Helvetica", 16, "bold"))
file_entry.pack()

file_button = tk.Button(root, text="Abrir", command=open_file, bg=button_color, fg="white", font=("Helvetica", 16, "bold"))
file_button.pack()



# Agregar un espaciador en blanco
blank_space_label = tk.Label(root, text="", bg=bg_color)
blank_space_label.pack()
# Agregar un espaciador en blanco
blank_space_label = tk.Label(root, text="", bg=bg_color)
blank_space_label.pack()



# Agregar un campo de entrada para controlar la velocidad de ejecución
speed_label = tk.Label(root, text="Velocidad de ejecución:", bg=bg_color, fg="blue", font=("Helvetica", 16, "bold"))
speed_label.pack()

speed_entry = tk.Entry(root, width=10, font=("Helvetica", 16, "bold"))
speed_entry.insert(0, "")  # Valor por defecto
speed_entry.pack()



# Agregar un espaciador en blanco
blank_space_label = tk.Label(root, text="", bg=bg_color)
blank_space_label.pack()





# Agregar entradas para las líneas de inicio y fin
start_line_label = tk.Label(root, text="Línea de inicio:", bg=bg_color, fg="red", font=("Helvetica", 16, "bold"))
start_line_label.pack()

start_line_entry = tk.Entry(root, width=10, font=("Helvetica", 16, "bold"))
start_line_entry.pack()

end_line_label = tk.Label(root, text="Línea de fin:", bg=bg_color, fg="red", font=("Helvetica", 16, "bold"))
end_line_label.pack()

end_line_entry = tk.Entry(root, width=10, font=("Helvetica", 16, "bold"))
end_line_entry.pack()

# Run the main loop
start_button = tk.Button(root, text="Ejecutar", command=start_execution, bg=button_color, fg="white", font=("Helvetica", 12, "bold"))
start_button.pack()

# Agregar un espaciador en blanco
blank_space_label = tk.Label(root, text="", bg=bg_color)
blank_space_label.pack()
# Agregar un espaciador en blanco
blank_space_label = tk.Label(root, text="", bg=bg_color)
blank_space_label.pack()






root.mainloop() 
import tkinter as tk
import pyautogui
import time
import pyperclip
import datetime

barra = (1007, 73)
caja_Equis = (156, 320)



# Función para ejecutar las acciones de las reacciones
def execute_reactions(link, like, love, importa):
    repetitions = int(like) + int(love) + int(importa)
    

    #Repeticiones es la suma de los enteros inputs de las reacciones "like", "love", "me importa"
    #Ciclo para pegar las ligas en la barra de urls
    time.sleep(2)  
    for _ in range(repetitions):
        time.sleep(1)
        pyautogui.click(barra)
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.2)
        pyautogui.press('delete')
        time.sleep(.2)
        pyperclip.copy(link)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(.3)
        pyautogui.press('enter')
        time.sleep(.1)
        pyautogui.hotkey('ctrl', 'pagedown')
        time.sleep(1)  # Wait between iterations





    time.sleep(1)
        # Etiqueta para el bucle exterior
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
            repetitions -= 1
            time.sleep(.2)

        # Si la etiqueta 'reinicio' es True, continúa con la siguiente repetición
        if reinicio:
            reinicio = False
            continue

        #para hacer la reaccion para cada reaccion hay que hacer una condicional que verifique el numero de reacciones en cada input y lo ejecute y si no que avance a la siguiente reaccion

    
    
       




    #Aqui inician las acciones

   
    time.sleep(.2)
    # Bucle para el "like"
    for _ in range(int(like)):
        time.sleep(.2)
        pyautogui.click(caja_Equis)
        time.sleep(.2)
        #Accediendo a la reaccion
        for i in range(2):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'pagedown')





        pass  # Reemplaza "pass" con las acciones que deseas hacer



    time.sleep(.2)
    # Bucle para el "love"
    for _ in range(int(love)):
        time.sleep(.2)
        pyautogui.click(caja_Equis)
        time.sleep(.2)
        #Accediendi a la reaccion
        for i in range(3):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'pagedown')




        pass  # Reemplaza "pass" con las acciones que deseas hacer



    time.sleep(.2)
    # Bucle para el "me importa"
    for _ in range(int(importa)):
        time.sleep(.2)
        pyautogui.click(caja_Equis)
        time.sleep(.2)
        #Accediendi a la reaccion
        for i in range(4):
            pyautogui.hotkey('tab')
            time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.2)
        pyautogui.hotkey('ctrl', 'pagedown')



        pass  # Reemplaza "pass" con las acciones que deseas hacer





    print("--- " + str(repetitions)+ " Reacciones---")


def submit_values():
    link = link_entry.get()
    like = like_entry.get()
    love = love_entry.get()
    importa = importa_entry.get()


    execute_reactions(link, like, love, importa)
# Aquí podrías realizar acciones con los valores ingresados, como imprimirlos en la consola

# Crear la ventana principal
root = tk.Tk()
root.title("Reacciones")
root.geometry("600x500+500+400")


# Colores personalizados
bg_color = "#FF0000"
button_color = "#4CAF50"
text_color = "#333333"
label_bg_color = "#DADADA"
  # Código hexadecimal para el color rojo


# Estilos
root.configure(bg=bg_color)


# Elementos de entrada
link_frame = tk.Frame(root, bg=bg_color)
link_frame.pack(pady=10)

link_label = tk.Label(link_frame, text="Link:", width=10, font=("Helvetica", 16, "bold"), bg=label_bg_color, fg=text_color)
link_label.pack(side=tk.LEFT)

link_entry = tk.Entry(link_frame, width=50, font=("Helvetica", 16))
link_entry.pack(side=tk.LEFT)

like_frame = tk.Frame(root, bg=bg_color)
like_frame.pack(pady=10)

like_label = tk.Label(like_frame, text="Like:", width=10, font=("Helvetica", 16, "bold"), bg=label_bg_color, fg=text_color)
like_label.pack(side=tk.LEFT)

like_entry = tk.Entry(like_frame, width=50, font=("Helvetica", 16))
like_entry.pack(side=tk.LEFT)

love_frame = tk.Frame(root, bg=bg_color)
love_frame.pack(pady=10)

love_label = tk.Label(love_frame, text="Love:", width=10, font=("Helvetica", 16, "bold"), bg=label_bg_color, fg=text_color)
love_label.pack(side=tk.LEFT)

love_entry = tk.Entry(love_frame, width=50, font=("Helvetica", 16))
love_entry.pack(side=tk.LEFT)

importa_frame = tk.Frame(root, bg=bg_color)
importa_frame.pack(pady=10)

importa_label = tk.Label(importa_frame, text="Importa:", width=10, font=("Helvetica", 16, "bold"), bg=label_bg_color, fg=text_color)
importa_label.pack(side=tk.LEFT)

importa_entry = tk.Entry(importa_frame, width=50, font=("Helvetica", 16))
importa_entry.pack(side=tk.LEFT)


# Botón de envío
submit_button = tk.Button(root, text="Enviar", command=submit_values, bg=button_color, fg="white", font=("Helvetica", 12, "bold"))
submit_button.pack()

# Ejecutar el bucle principal
root.mainloop()

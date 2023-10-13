import tkinter as tk
import pyautogui
import time
import pyperclip
import datetime


#Esta es la variable que hay que configurar con CDM en mi caso es:
caja = (990, 65)




#TKinter

class PopupWindow:
    def __init__(self, master):
        self.master = master
        master.title("SOLO_LIKE")
        master.geometry("400x400+100+100")

        self.url_label = tk.Label(master, text="URL", fg="blue", font=("Helvetica", 16, "bold"))
        self.url_label.pack()
        self.url_entry = tk.Entry(master)
        self.url_entry.pack()
        
        

        self.rep_label = tk.Label(master, text="Repeticiones", fg="blue", font=("Helvetica", 16, "bold"))
        self.rep_label.pack()
        

        self.rep_entry = tk.Entry(master)
        self.rep_entry.pack()

        self.ok_button = tk.Button(master, text="OK", command=self.ok_callback)
        self.ok_button.pack()

    def ok_callback(self):
        link = self.url_entry.get()
        n_repeticiones = int(self.rep_entry.get())
        self.master.destroy()

        # Esperar 3 segundos antes de iniciar
        time.sleep(2)

        # Iterar n_repeticiones veces
        for i in range(n_repeticiones):
            
            # Click en la barra de direcciones y pegar la URL
            pyautogui.click(caja)
            time.sleep(.2)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(.2)
            pyautogui.press("delete")
            time.sleep(.2)
            pyautogui.write(link)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(.2)
            # Cambiar de pestaña
            pyautogui.hotkey('ctrl', 'pagedown')
            time.sleep(1)


        #Regresa al punto inicial

        reinicio = False

        # Ciclo para acceder a la posición inicial
        for _ in range(n_repeticiones):
            # Activa el atajo para copiar la URL actual en la barra de direcciones (Ctrl + L y luego Ctrl + C)
            pyautogui.hotkey('ctrl', 'shift', 'pageup')
            time.sleep(.2)
            pyautogui.click(caja)
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
        print("LINK: " + link + " SOLO_LIKES: " + str(n_repeticiones) + " Hora: " + hora_formateada)




        

            
            
            
            
            
            
        time.sleep(.2)
        for i in range(n_repeticiones):
             #Click de espera a la accion   
            pyautogui.click(233, 333) 
            time.sleep(.2)
 

            for i in range(3):
                pyautogui.hotkey('tab')
                time.sleep(.2)

            
            pyautogui.hotkey('enter')
            time.sleep(.2)
            
            pyautogui.hotkey('ctrl', 'pagedown')
            time.sleep(.2)
            # Esperar 1 segundo antes de la siguiente iteración

def main():
    root = tk.Tk()
    PopupWindow(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()

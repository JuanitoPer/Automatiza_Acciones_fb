import tkinter as tk
import pyautogui
import time



#Esta es la variable que hay que configurar con CDM en mi caso es:
caja = (990, 65)




#TKinter

class PopupWindow:
    def __init__(self, master):
        self.master = master
        master.title("ME ENCANTA")
        master.geometry("400x400+100+100")

        self.url_label = tk.Label(master, text="URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        self.rep_label = tk.Label(master, text="Cantidad de repeticiones:")
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
        time.sleep(3)

        # Iterar n_repeticiones veces
        for i in range(n_repeticiones):
            
            # Click en la barra de direcciones y pegar la URL
            pyautogui.click(caja)
            time.sleep(2)
            pyautogui.press("delete")
            time.sleep(1)
            pyautogui.write(link)
            time.sleep(1)
            pyautogui.press('enter')
            # Esperar 1 segundo para que cargue la página
            time.sleep(1)
            
            # Cambiar de pestaña
            pyautogui.hotkey('ctrl', 'pagedown')


        #Regresa al punto inicial

        for i in range(n_repeticiones):
            pyautogui.hotkey('ctrl', 'shift', 'pageup')
            time.sleep(1)


    

            
            
            
            
            
            
            
        for i in range(n_repeticiones):
            time.sleep(.2) 
            pyautogui.click(228, 421) 
            time.sleep(.2)  
            pyautogui.hotkey('tab')
            time.sleep(.2)
            pyautogui.hotkey('tab')
            time.sleep(.2)
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

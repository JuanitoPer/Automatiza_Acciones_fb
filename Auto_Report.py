import tkinter as tk
import pyautogui
import time



# Coordenadas de la caja para pegar la URL en la barra de direcciones
caja = (1007, 73)
caja_equis = ((156, 320))

class PopupWindow:
    def __init__(self, master):
        self.master = master
        master.title("Auto_Report")
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
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("delete")
            time.sleep(1)
            pyautogui.write(link)
            time.sleep(5)
            pyautogui.press('enter')
            # Esperar 1 segundo para que cargue la página
            time.sleep(1)
            # Cambiar de pestaña
            pyautogui.hotkey('ctrl', 'tab')




        time.sleep(3)
        # Regresa al punto inicial de las pestañas
        for i in range(n_repeticiones):
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'shift', 'tab')  
            
        time.sleep(2)
        # Realizar la acción deseada después cada que se cambia de pestaña
        for i in range(n_repeticiones):
            time.sleep(1)
            pyautogui.click(caja_equis) 
            time.sleep(1)  
            
            #Accediendo al PRIMER cuadro de dialogo
            pyautogui.hotkey('tab')
            time.sleep(3)  
            for i in range(3):
                time.sleep(.2)
                pyautogui.press('down')
            pyautogui.press('enter')



            #Accediendo al SEGUNDO cuadro de dialogo
            time.sleep(3)  
            pyautogui.click(caja_equis) 
            pyautogui.hotkey('tab')

            #Selecciona un problema:

            # Desnudos
            #Violencia  
            #Acoso  
            #Suicidio o autolesión  
            #Información falsa
            #Spam  
            #Ventas no autorizadas  
            #Lenguaje que incita al odio  
            #Terrorismo 


            #Estamos accediendo a VIOLENCIA
            
            time.sleep(2)
            pyautogui.press('down')
            time.sleep(.2)
            pyautogui.press('enter')
            time.sleep(2)


            #Accediendo al TERCER cuadro de dialogo
            #Violencia gráfica
            pyautogui.click(caja_equis) 
            time.sleep(1)  
            pyautogui.hotkey('tab')
            time.sleep(.2)
            pyautogui.press('down')
            time.sleep(.2)
            pyautogui.press('up')
            pyautogui.press('enter')
            time.sleep(.2)


            #Click Caja_equis
            pyautogui.click(caja_equis)
            time.sleep(1)  

            #Click checkbox
            pyautogui.click(712, 512)

            time.sleep(1)
            
            pyautogui.hotkey('tab')
            time.sleep(1)
            pyautogui.press('enter')

            #En este puno ya se envio el reporte y se puede ocultar o bloquear al usuario

            time.sleep(3)
            pyautogui.hotkey('ctrl', 'tab') 

            #En este puno ya se envio el reporte y se puede ocultar o bloquear al usuario




def main():
    root = tk.Tk()
    PopupWindow(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()

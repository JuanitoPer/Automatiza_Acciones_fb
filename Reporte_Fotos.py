import tkinter as tk
import pyautogui
import time

# Coordenadas de los elementos en la pantalla
barra = (1007, 73)
caja_Equis = (156, 320)

# TKinter
class PopupWindow:
    def __init__(self, master):
        self.master = master
        master.title("REPORTE_FOTOS")
        master.geometry("400x500+100+100")

        self.url_label = tk.Label(master, text="URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        self.rep_label = tk.Label(master, text="Cantidad de repeticiones:")
        self.rep_label.pack()
        self.rep_entry = tk.Entry(master)
        self.rep_entry.pack()

        self.path_label = tk.Label(master, text="Ruta de almacenamiento:")
        self.path_label.pack()
        self.path_entry = tk.Entry(master)
        self.path_entry.pack()

        self.ok_button = tk.Button(master, text="OK", command=self.ok_callback)
        self.ok_button.pack()

    def ok_callback(self):
        link = self.url_entry.get()
        n_repeticiones = int(self.rep_entry.get())
        save_path = self.path_entry.get()
        self.master.destroy()

        # Esperar 3 segundos antes de iniciar
        time.sleep(3)

        # Iterar n_repeticiones veces
        for i in range(n_repeticiones):
            time.sleep(3)
            pyautogui.click(barra)
            time.sleep(.2)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(.2)
            pyautogui.press('delete')
            time.sleep(.2)
            pyautogui.typewrite(link)
            time.sleep(.1)
            pyautogui.press('enter')
            time.sleep(.1)
           



            # Realizar acción después de pegar link
            time.sleep(5)
            pyautogui.click(caja_Equis)
            time.sleep(1)
            pyautogui.press('esc')


            # Ajusta el valor según lo necesario
            pyautogui.click(caja_Equis)
            pyautogui.scroll(-500)  
            time.sleep(.2)



            pyautogui.press('esc')
            screenshot = pyautogui.screenshot(region=(509, 211, 900, 300))  # Cambiar las dimensiones según tu pantalla
            screenshot.save(f"{save_path}/pic_{i + 1}.png")  # Guardar con nombres ascendentes
            time.sleep(.2)
            pyautogui.hotkey('ctrl', 'pagedown')
            time.sleep(.2)

           

def main():
    root = tk.Tk()
    PopupWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()

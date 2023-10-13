import tkinter as tk
import pyautogui
import time
import threading

# Coordenadas de la caja en la interfaz gráfica para pegar la URL
caja = (990, 65)

class PopupWindow:
    def __init__(self, master):
        self.master = master
        master.title("Reacciones Automáticas")
        master.geometry("400x400+100+100")

        self.url_label = tk.Label(master, text="URLs (separadas por coma):")
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
        links = self.url_entry.get().split(',')
        n_repeticiones = int(self.rep_entry.get())
        self.master.destroy()

        def process_link(link):
            for _ in range(n_repeticiones):
                pyautogui.click(caja)
                pyautogui.press("delete")
                time.sleep(1)
                pyautogui.write(link)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'tab')
                time.sleep(2)  # Ajusta este tiempo según sea necesario
                # Agregar aquí las acciones que deseas realizar en cada pestaña
                pyautogui.hotkey('ctrl', 'tab')
                time.sleep(1)

        threads = []
        for link in links:
            thread = threading.Thread(target=process_link, args=(link.strip(),))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        print("Todas las tareas completadas.")

def main():
    root = tk.Tk()
    PopupWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()

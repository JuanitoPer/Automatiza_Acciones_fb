import pyautogui
import time

# Coordenadas de los elementos en la pantalla
caja_Equis = (156, 320)
barra = (1908, 990)

# Tiempo de espera inicial
time.sleep(5)

# Número de repeticiones
n_repeticiones = 1

# Ruta donde se guardarán las fotos
save_path = "C:\\Users\\alber\\Documents\\CLOUD\\PNG"



# Función para guardar las fotos
def guardar_fotos(n_repeticiones, save_path):
    for num in range(1, n_repeticiones + 1):
        time.sleep(1)
        pyautogui.click(caja_Equis)
        time.sleep(1)
        #Hay que definir el tamaño de la pagina para poder tomar la captura
        pyautogui.scroll(-2500)
        pyautogui.tripleClick(barra)
        #pyautogui.click(caja_Equis)
        time.sleep(1)


        # Cambiar las dimensiones según tu pantalla
        screenshot = pyautogui.screenshot(region=(509, 211, 900, 700)) 
        time.sleep(.2) 
        screenshot.save(f"{save_path}/1_{num}.png")
        time.sleep(.2)
            


# Llamar a la función para guardar las fotos
guardar_fotos(n_repeticiones, save_path)

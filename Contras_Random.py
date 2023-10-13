import random
import string
import pandas as pd

# Cargar los datos desde un archivo CSV (suponiendo que tienes un archivo CSV)
# Asegúrate de tener una columna con nombres para hombres y otra para mujeres
# En este ejemplo, usaremos un DataFrame de ejemplo con columnas "Hombres" y "Mujeres"
# Reemplaza esto con la carga de tu propio archivo CSV

data = {
    "Hombres": ["Juan", "Pedro", "Carlos", "Luis", "Miguel"],
    "Mujeres": ["Ana", "María", "Sofía", "Laura", "Isabella"]
}

df = pd.DataFrame(data)

# Número de nombres a generar e imprimir
nombres_a_generar = int(input("Cuántos nombres aleatorios deseas generar: "))

# Sexo: "h" para hombres, "m" para mujeres
sexo = input("Ingresa el sexo (h para hombres, m para mujeres): ")

# Función para generar nombres aleatorios
def generar_nombres_aleatorios(dataframe, sexo, cantidad):
    if sexo == "h":
        columna = "Hombres"
    elif sexo == "m":
        columna = "Mujeres"
    else:
        print("Sexo no válido.")
        return

    nombres = dataframe[columna].sample(n=cantidad)
    return nombres

# Generar e imprimir nombres aleatorios
nombres_generados = generar_nombres_aleatorios(df, sexo, nombres_a_generar)
   
print(nombres_generados)

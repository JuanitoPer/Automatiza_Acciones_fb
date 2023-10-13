import datetime

# Obtén la hora actual
hora_actual = datetime.datetime.now()

# Formatea la hora actual como una cadena de texto
hora_formateada = hora_actual.strftime("%H:%M:%S")

# Imprime la hora formateada
print("La hora actual es:", hora_formateada)

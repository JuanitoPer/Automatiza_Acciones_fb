# Revisa el estado del sistema
import psutil

# Obtén la cantidad de memoria disponible
memory_available = psutil.virtual_memory().available

# Obtén la cantidad de espacio en disco disponible
disk_available = psutil.disk_usage("/").free

# Obtén la temperatura del procesador
cpu_temperature = psutil.sensors_temperatures()["cpu_thermal_zone0"].current

# Imprime la información
print("Memoria disponible:", memory_available)
print("Espacio en disco disponible:", disk_available)
print("Temperatura del procesador:", cpu_temperature)

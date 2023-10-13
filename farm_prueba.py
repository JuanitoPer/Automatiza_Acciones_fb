import psutil

# Obtener estadísticas de red
net_stats = psutil.net_io_counters()
print(f"Bytes enviados: {net_stats.bytes_sent}")
print(f"Bytes recibidos: {net_stats.bytes_recv}")

# Listar conexiones de red activas
connections = psutil.net_connections(kind='inet')
for conn in connections:
    print(f"Local Address: {conn.laddr}")
    print(f"Remote Address: {conn.raddr}")
    print(f"Status: {conn.status}")

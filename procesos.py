import os
import sys
import psutil

def obtener_informacion_proceso(pid):
    try:
        proceso = psutil.Process(pid)
        nombre = proceso.name()
        pid = proceso.pid
        pid_padre = proceso.ppid()
        usuario_propietario = proceso.username()
        uso_cpu = proceso.cpu_percent()
        consumo_memoria = proceso.memory_info().rss
        estado = proceso.status()
        path_ejecutable = proceso.exe()

        print(f"Nombre del proceso: {nombre}")
        print(f"ID del proceso: {pid}")
        print(f"Parent process ID: {pid_padre}")
        print(f"Usuario propietario: {usuario_propietario}")
        print(f"Porcentaje de uso de CPU: {uso_cpu}%")
        print(f"Consumo de memoria: {consumo_memoria} bytes")
        print(f"Estado: {estado}")
        print(f"Path del ejecutable: {path_ejecutable}")

    except psutil.NoSuchProcess:
        print("El ID del proceso proporcionado no es válido.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <ID_del_proceso>")
    else:
        pid_proceso = int(sys.argv[1])
        obtener_informacion_proceso(pid_proceso)

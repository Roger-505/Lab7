import os
import sys
import time
import subprocess

def monitorear_proceso(nombre_proceso, comando):
    while True:
        # Verificar si el proceso está en ejecución
        proceso_encontrado = False
        for proc in os.popen('tasklist').readlines():
            if nombre_proceso in proc:
                proceso_encontrado = True
                break

        if not proceso_encontrado:
            print(f"El proceso '{nombre_proceso}' no está en ejecución. Iniciando...")
            subprocess.Popen(comando, shell=True)  # Iniciar el proceso

        time.sleep(5)  # Esperar 5 segundos antes de volver a revisar

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <nombre_proceso> <comando>")
    else:
        nombre_proceso = sys.argv[1]
        comando = sys.argv[2]
        monitorear_proceso(nombre_proceso, comando)

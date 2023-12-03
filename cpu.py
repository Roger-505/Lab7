import psutil
import subprocess
import time
import matplotlib.pyplot as plt

def monitorear_proceso(ejecutable):
    try:
        proceso = subprocess.Popen(ejecutable)
        pid = proceso.pid
        print(f"Proceso iniciado con PID: {pid}")

        cpu_uso = []
        memoria_uso = []

        while proceso.poll() is None:
            uso_cpu = psutil.Process(pid).cpu_percent()
            uso_memoria = psutil.Process(pid).memory_percent()
            
            cpu_uso.append(uso_cpu)
            memoria_uso.append(uso_memoria)
            
            time.sleep(1)  # Esperar 1 segundo antes de volver a medir
            
        # Graficar los valores recopilados sobre el tiempo
        plt.figure(figsize=(10, 5))
        plt.subplot(2, 1, 1)
        plt.plot(cpu_uso, label='Uso de CPU')
        plt.xlabel('Tiempo')
        plt.ylabel('Uso de CPU (%)')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(memoria_uso, label='Uso de Memoria')
        plt.xlabel('Tiempo')
        plt.ylabel('Uso de Memoria (%)')
        plt.legend()

        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("El ejecutable proporcionado no existe.")
    except psutil.NoSuchProcess:
        print("El proceso finalizó inesperadamente.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python script.py <ejecutable>")
    else:
        ejecutable = sys.argv[1]
        monitorear_proceso(ejecutable)

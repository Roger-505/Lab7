# Reporte de Monitoreo de Procesos

## Script 1: Obtener Información de un Proceso

El primer script tenía como objetivo obtener información relevante de un proceso en ejecución. Utilizamos el módulo `os` y `psutil` en Python para recopilar datos como el nombre del proceso, ID, ID del proceso padre, usuario propietario, porcentaje de uso de CPU, consumo de memoria, estado y la ruta del ejecutable.

El script proporcionó una manera rápida y eficiente de obtener información detallada sobre un proceso específico. Al ejecutar el script con el ID de un proceso como argumento, pudimos obtener datos relevantes que son útiles para el monitoreo y diagnóstico de procesos en un sistema.

## Script 2: Automatizar el Monitoreo de un Proceso

El segundo script fue diseñado para monitorear un proceso de forma automática. Recibió el nombre del proceso y el comando para ejecutarlo, luego verificó periódicamente si el proceso estaba en ejecución. Si el proceso se cerraba, el script lo reiniciaba.

Este script permitió automatizar la supervisión de un proceso en particular. Si el proceso terminaba por alguna razón, el script lo reiniciaba automáticamente. Esto es útil en situaciones donde es crucial mantener un proceso en ejecución constante.

## Script 3: Monitorear Consumo de CPU y Memoria de un Proceso

El tercer script se enfocó en monitorear el consumo de CPU y memoria de un proceso específico. Ejecutó el binario proporcionado como argumento y registró periódicamente el uso de CPU y memoria en un archivo de registro. Al finalizar el proceso, generó gráficos utilizando `matplotlib` para visualizar estos datos a lo largo del tiempo.

El script pudo recopilar datos de uso de CPU y memoria a lo largo del tiempo mientras el proceso estaba en ejecución. La visualización de estos datos en forma de gráficos proporcionó una representación clara del comportamiento del proceso en términos de consumo de recursos.
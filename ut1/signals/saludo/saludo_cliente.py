import os
import sys
import signal

if len(sys.argv) != 2: # mal número de parámetros de ejecución
    print("Número incorrecto de parámetros, se espera un PID")
    os._exit(-1)

numero = int(sys.argv[1])
os.kill(numero, signal.SIGUSR1)
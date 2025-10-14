import signal
import os
import sys


if len(sys.argv) != 2:
    print("falta el pid del secundario")
    os._exit(-1)

pid = int(sys.argv[1])

while True:
    command = input("Ingrese señal:\t")
    match command:
        case "empezar":
            os.kill(pid, signal.SIGUSR1)
        case "parar":
            os.kill(pid, signal.SIGUSR2)
        case "continuar":
            os.kill(pid, signal.SIGINT)
        case _:
            print("ese comando no existe, ingresa (empezar|parar)")
        



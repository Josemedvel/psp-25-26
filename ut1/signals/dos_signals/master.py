import signal
import os
import sys

print(sys.argv)

if len(sys.argv) != 2:
    sys.exit(-1)

pid_esclavo = int(sys.argv[1])

while True:
    comando = input("Ingrese comando:")
    match comando.lower().strip():
        case "ping":
            os.kill(pid_esclavo, signal.SIGUSR1)
        case "pong":
            os.kill(pid_esclavo, signal.SIGUSR2)
        case _:
            print("oye, pon un comando válido (ping|pong)")
            continue





import os
import signal
import sys

if len(sys.argv) != 3:
    print("Faltan parámetros:")
    print("dromedario.py [num_dromedario] [pid_gestor]")
    sys.exit(-1)

pid_gestor = int(sys.argv[2])
num_dromedario = sys.argv[1]
os.kill(pid_gestor, signal.SIGINT) # cuando el gestor reciba 2, empieza la partida
signal_drom = None

if num_dromedario == "1":
    signal_drom = signal.SIGUSR1
else:
    signal_drom = signal.SIGUSR2

while True:
    input("Pulsa Enter para avanzar")
    os.kill(pid_gestor, signal_drom)
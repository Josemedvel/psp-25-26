import signal
import os

print(f"Hola, el pid del servidor es: {os.getpid()}")

def saludo(signum, frame):
    print("se ha recibido la señal de saludo")

signal.signal(signal.SIGUSR1, saludo)

while True:
    signal.pause()

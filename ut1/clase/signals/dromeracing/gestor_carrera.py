import signal
import os
import random

print(os.getpid())

num_usuarios = 0
posiciones_dromedarios = [0,0]
meta = 20
prob_tropiezo = 0.2

def avanzar_dromedario(signum, frame, num_drom):
    global prob_tropiezo, posiciones_dromedarios
    if random.random() > prob_tropiezo: # no hay tropiezo
        posiciones_dromedarios[num_drom] += 1
    print((posiciones_dromedarios[0] - 1) * "_" + "🐪" + (meta-posiciones_dromedarios[0]-1)*"_"+"|")
    print((posiciones_dromedarios[1] - 1) * "_" + "🐪" + (meta-posiciones_dromedarios[1]-1)*"_"+"|")
    for i in range(len(posiciones_dromedarios)):
        if posiciones_dromedarios[i] == meta:
            print(f"Ha ganado el dromedario {i}")

def empezar():
    print("La carrera ha empezado")
    signal.signal(signal.SIGUSR1, lambda signum, frame: avanzar_dromedario(signum, frame, 0))
    signal.signal(signal.SIGUSR2, lambda signum, frame: avanzar_dromedario(signum, frame, 1))

def usuario_conectado(signum, frame):
    global num_usuarios
    print("Se ha conectado un usuario")
    num_usuarios += 1
    if num_usuarios == 2:
        empezar()






signal.signal(signal.SIGINT, usuario_conectado)
while True:
    signal.pause()
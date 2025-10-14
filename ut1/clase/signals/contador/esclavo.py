import os
import signal

def empezar(signum, frame): #sigusr1
    global contando, contador
    contando = True
    contador = 0
    while contando:
        contador += 1
        print(contador)

def parar(signum, frame): #sigusr2
    global contando
    contando = False

def continuar(signum, frame):
    global contando, contador
    contando = True
    while contando:
        contador += 1
        print(contador)


contador = 0
contando = False

print(os.getpid())

signal.signal(signal.SIGUSR1, empezar)
signal.signal(signal.SIGUSR2, parar)
signal.signal(signal.SIGINT, continuar)
signal.SIG

while True:
    signal.pause()
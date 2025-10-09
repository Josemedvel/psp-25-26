import time
import subprocess


def limpiar():
    subprocess.run(args=["clear"])

def derecha():
    for j in range(20):
        print(j * " " + "#")
        time.sleep(0.005)
        limpiar()

def izquierda():
    for j in range(20, -1, -1):
        print(j * " " + "#")
        time.sleep(0.005)
        limpiar()

if __name__ == "__main__":
    while True:
        derecha()
        izquierda()
        
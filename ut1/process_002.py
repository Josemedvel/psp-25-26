from multiprocessing import Process
import os

def saludo():
    print("Hola")


proceso_nuevo = Process(target=saludo)
print("Proceso nuevo", proceso_nuevo.pid)
proceso_nuevo.start()
proceso_nuevo.join()
print("Proceso lanzador",os.getpid())

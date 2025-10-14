from multiprocessing import Process
import os

def saludo(persona,edad):
    print(f"Hola {persona},{edad}")

proceso_1 = Process(target=saludo, args=("Pedro",56))
proceso_2 = Process(target=saludo, args=("Salma",22))
proceso_1.start()
proceso_2.start()
proceso_1.join()
proceso_2.join()
print("adios desde el principal")



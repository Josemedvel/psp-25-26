import os
from multiprocessing import Value

espera  = Value("b", True)


print("Inicio")

print(f"hola, soy el padre, con PID {os.getpid()}")
pid_hijo = os.fork()
if pid_hijo == 0: # hijo
    print(f"Hola, soy el hijo, con PID {os.getpid()}")
    pid_nieto = os.fork()
    if pid_nieto == 0: # nieto
        print(f"Hola, soy el nieto, con PID {os.getpid()}")
        pid_bisnieto = os.fork()
        if pid_bisnieto == 0: # bisnieto
            print(f"Hola, soy el bisnieto, con PID {os.getpid()}")
            espera.value = False
            os._exit(0)
        else: # nieto
            os._exit(0)
    else: # hijo
        os._exit(0)
while espera.value:
    pass
print("Final")

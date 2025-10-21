import os

print("Inicio")

pid_hijo = os.fork()
if pid_hijo != 0: # padre
    print(f"hola, soy el padre, con PID {os.getpid()}, mi proceso clon(hijo) tiene PID {pid_hijo}")
else: # hijo
    pid_nieto = os.fork()
    if pid_nieto != 0: # hijo
        print(f"Hola, soy el hijo, con PID {os.getpid()}, mi hijo tiene PID {pid_nieto}, mi padre es {os.getppid()}")
        os._exit(0)
    else: # nieto
        pid_bisnieto = os.fork()
        if pid_bisnieto != 0: # nieto
            print(f"Hola, soy el nieto, con PID {os.getpid()}, mi hijo tiene PID {pid_bisnieto}, mi padre es {os.getppid()}")
            os._exit(0)
        else: # bisnieto
            print(f"Hola, soy el bisnieto, con PID {os.getpid()}, mi padre es {os.getppid()}")
            os._exit(0)

print("Final")
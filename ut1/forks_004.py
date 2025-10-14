import os
import sys

print("INICIO")
pid = os.fork()
if pid != 0: # Somos el proceso padre
    os.wait() # esperamos a que muera el proceso hijo
    print(f"Hola, soy el padre, con PID {os.getpid()}")
else: # Somos el hijo
    print(f"Hola, soy el proceso hijo, con PID {os.getpid()}, mi padre es {os.getppid()}")
    # os._exit(0)
    sys.exit(0)
print("FINAL")
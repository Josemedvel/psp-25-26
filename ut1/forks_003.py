import os

print("INICIO")
pid = os.fork()
pid_2 = os.fork()
if pid != 0 and pid_2 != 0: # padre
    print(f"Hola desde el padre, mi PID es: {os.getpid()}")
elif pid != 0 and pid_2 == 0: # 2º hijo del padre
    print(f"Hola desde el segundo hijo: {os.getpid()}, mi padre es el: {os.getppid()}")
elif pid == 0 and pid_2 != 0: # 1er hijo del padre
    print(f"Hola desde el primer hijo: {os.getpid()}, mi padre es el: {os.getppid()}")
else:
    print(f"Hola desde el nieto: {os.getpid()}, mi padre es el: {os.getppid()}")
print("FINAL")
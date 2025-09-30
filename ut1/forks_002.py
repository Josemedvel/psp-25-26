import os

print("INICIO")
pid = os.fork()
if pid != 0: # estoy ejecutando en el proceso padre
    print("hola, soy el padre", os.getpid(), "mi hijo tiene pid:" ,pid)
else:
    print("hola, soy el hijo", os.getpid(), "mi padre tiene pid:", os.getppid())
print("FINAL")
import sys
from multiprocessing import Process, Value

valor = Value("i", 0)

def suma_par(lista, valor):
    res = 0
    for i in lista:
        res += i
    with valor:
        valor.value += res

if len(sys.argv) != 2:
    num_proc = 4
else:
    num_proc = int(sys.argv[1]) # numero elegido

lista = [x for x in range(1,101)]

'''print(lista[2*3:])#ultimo
print(lista[0*3:0*3 + 3])#primero
print(lista[1*3:1*3 + 3])#segundo
'''
lista_proc = []

num_ventana = len(lista) // num_proc

for i in range(num_proc):
    if i == num_proc - 1: # último
        p = Process(target=suma_par, args=(lista[i*num_ventana:],valor))
    else: # cualquier otro proceso
        p = Process(target=suma_par, args=(lista[i*num_ventana: i*num_ventana + num_ventana],valor))
    lista_proc.append(p)

for p in lista_proc:
    p.start()

for p in lista_proc:
    p.join()

print(valor.value)
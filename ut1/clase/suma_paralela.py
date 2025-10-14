from multiprocessing import Process, Value

lista_numeros = [x for x in range(1,101)] #5050
valor = Value("i", 0)

print(lista_numeros[:len(lista_numeros) // 2])
print(lista_numeros[len(lista_numeros) // 2:])


def suma_par(lista, valor):
    res = 0
    for i in lista:
        res += i
    with valor:
        valor.value += res
    

p_1 = Process(target=suma_par, args=(lista_numeros[:len(lista_numeros)//2], valor))
p_2 = Process(target=suma_par, args=(lista_numeros[len(lista_numeros)//2:], valor))

p_1.start()
p_2.start()

p_1.join()
p_2.join()

print(valor.value) # resultado completo
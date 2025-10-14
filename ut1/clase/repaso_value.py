from multiprocessing import Value, Process
valor = Value("i", 5)
variable = 5

def suma(valor):
    with valor:
        for i in range(1000):
            valor.value += 1
def resta(valor):
    with valor:
        for i in range(1000):
            valor.value -= 1


p_suma = Process(target=suma, args=(valor,))
p_resta = Process(target=resta, args=(valor,))

p_suma.start()
p_resta.start()

p_suma.join()
p_resta.join()

print(valor.value)
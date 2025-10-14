from multiprocessing import Process, Value

variable = Value("i", 0)

def sumar(variable):
    for x in range(100):
        with variable:
            variable.value += 1

def restar(variable):
    for x in range(100):
        with variable:
            variable.value -= 1

proc_suma = Process(target=sumar, args=(variable,))
proc_resta = Process(target=restar, args=(variable,))

proc_suma.start()
proc_resta.start()

proc_suma.join()
proc_resta.join()

print(variable.value)
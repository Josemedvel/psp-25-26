edad = 16

def sumar(a, b):
    return a + b
'''
print(sumar(1, 4))
print("la edad de la persona es " + str(edad))

print(1 + 2) # 3
print(2 - 2) # 0
print(4 * 2) # 8
print(7 / 2) # 3.5
print(7 // 2) # 3
print(3 ** 2) # 9
print(2 ** 0.5) # 1.41
print(15 % 12) # 3
'''
cadena = "hola\t 'javier'" \
"mundo"
cadena_2 = 'hola\t"javier"' + str(edad)
cadena_3 = '''hola
mundo'''

cadena_4 = f"La edad de la persona es de {edad} años"
cadena_5 = "~"
'''
print(cadena)
print(cadena_2)
print(cadena_3)
print(cadena_4)

print(cadena_5*20, end="\t")
print(cadena_5*20)
'''
def imprimir_edad():
    global edad
    print(edad)

imprimir_edad()

if edad >= 18:
    print("Puede entrar a la discoteca")
elif edad >= 16:
    print("Puedes entrar a la discoteca de zumitos") 
else:
    print("No puedes entrar, eres menor de edad")

estado_pedido = 4# input("Introduce el estado del pedido:")

match estado_pedido:
    case "preparado":
        print("tu pedido está preparado")
    case "enviado" | "en camino":
        print("tu pedido está en camino")
    case "entregado":
        print("tu pedido ha sido entregado")
    case _:
        print("estado indeterminado del pedido")

numero = ""
entrada = ""
'''
while not entrada.isdecimal():
    entrada = input("Introduzca un número:\t")
    try:
        numero = int(entrada)
    except Exception as e:
        print(f"Por favor, introduce un número válido, has introducido:{entrada}, de tipo {type(entrada)}")
'''


lista = [3,4,5,6,3,3,9]

ult_elem = lista.pop(-7)
lista.insert(4,"hola")
lista.remove(3)



print(lista)
del(lista[3])
print(lista)
print(ult_elem)

sub_lista = lista[:2]
print(sub_lista)


lista_pares = []


lista_dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

lista_reves = lista_dias[::-1]
print(lista_reves)
for i in range(0, 50001, 2):
    lista_pares.append(i)



lista_mult_3 = [x for x in range(3, 3001, 3)]


'''tablero = [[x for x in range(6)] for y in range(6)]
for fila in range(len(tablero)):
    if fila != 0:
            print("_" * (17*len(tablero)))
    for col in range(len(tablero[fila])):
        if col == 0:
            print("\t" + str(tablero[fila][col]), end="")
            print("\t|\t", end="")
        elif col != len(tablero) - 1:
            print(tablero[fila][col], end="")
            print("\t|\t", end="")
        else:
            print(tablero[fila][col])
'''
#print(lista_2)

lista_nueva = [x for x in range(1,10001, 2)]
menu = {"lunes": "Macarrones con tomatico", "martes": "Cocido madrileño", 1: "Arroz con pollo"}
# HashMap<String, String>
print(menu[1])
menu["miercoles"] = "Ensaladita"
print(menu)

if "jueves" in menu:
    print(menu["jueves"])
else:
    print("No hay algo pensado para el jueves")



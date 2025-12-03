import socket
import threading

jugadas_validas = ["piedra", "papel", "tijera"]

def calcular_ganador_turno(jug_1, jug_2):
    resultado_turno = 0
    if jug_1 == "piedra" and jug_2 == "papel":
        resultado_turno = 1
    elif jug_1 == "piedra" and jug_2 == "tijera":
        resultado_turno = -1
    elif jug_1 == "tijera" and jug_2 == "piedra":
        resultado_turno = 1
    elif jug_1 == "tijera" and jug_2 == "papel":
        resultado_turno = -1
    elif jug_1 == "papel" and jug_2 == "tijera":
        resultado_turno = 1
    elif jug_1 == "papel" and jug_2 == "piedra":
        resultado_turno = -1
    return resultado_turno

def juego(cli_1, dir_cli_1, cli_2, dir_cli_2):
    #inicio juego
    
    puntos = {"jug_1": 0, "jug_2": 0}
    fin_juego = False
    ganador = ""
    cli_1.send(f"El juego ha comenzado, estás jugando contra {dir_cli_2}, envía tu jugada".encode())
    cli_2.send(f"El juego ha comenzado, estás jugando contra {dir_cli_1}, envía tu jugada".encode())

    while not fin_juego:
        jugada_1 = cli_1.recv(1024)
        jugada_2 = cli_2.recv(1024)
        if not jugada_1 or not jugada_2:
            raise Exception("No he recibido jugada/s")
        
        jug_1_limpia = jugada_1.decode().strip().lower()
        jug_2_limpia = jugada_2.decode().strip().lower()

        if(jug_1_limpia not in jugadas_validas) or (jug_2_limpia not in jugadas_validas):
            raise Exception("La jugada recibida no es válida")
        
        # resultado turno empieza con el valor dado a empate
        # si es -1 ha ganado el turno el jug_1
        # si es 1 ha ganado el turno el jug_2

        resultado_turno = calcular_ganador_turno(jug_1_limpia, jug_2_limpia)
        
        

        if resultado_turno == -1: #tenemos que sumarle al primer jugador
            puntos["jug_1"] += 1
            if puntos["jug_1"] == 3:
                ganador = "Jugador_1"
        elif resultado_turno == 1:
            puntos["jug_2"] += 1
            if puntos["jug_2"] == 3:
                ganador = "Jugador_2"

        if ganador != "":
            fin_juego = True
            if ganador == "Jugador_1":
                cli_1.send(f"El rival ha jugado:{jug_2_limpia}.\nHas ganado la partida!".encode())
                cli_1.close()
                cli_2.send(f"El rival ha jugado:{jug_1_limpia}.\nHas perdido la partida!".encode())
                cli_2.close()
            else:
                cli_2.send(f"El rival ha jugado:{jug_1_limpia}.\nHas ganado la partida!".encode())
                cli_2.close()
                cli_1.send(f"El rival ha jugado:{jug_2_limpia}.\nHas perdido la partida!".encode())
                cli_1.close()
        else: # no se ha acabado la partida
            if resultado_turno == 0: # empate
                cli_1.send("Habéis jugado lo mismo, se sigue jugando!".encode())
                cli_2.send("Habéis jugado lo mismo, se sigue jugando!".encode())
            elif resultado_turno == -1: # ha ganado el turno el jugador_1
                cli_1.send(f"El rival ha jugado:{jug_2_limpia}.\nHas ganado el turno! Vais {puntos['jug_1']}-{puntos['jug_2']}".encode())
                cli_2.send(f"El rival ha jugado:{jug_1_limpia}.\nHas perdido el turno! Vais {puntos['jug_1']}-{puntos['jug_2']}".encode())
            else: # ha ganado el turno el jugador_2
                cli_1.send(f"El rival ha jugado:{jug_2_limpia}.\nHas perdido el turno! Vais {puntos['jug_1']}-{puntos['jug_2']}".encode())
                cli_2.send(f"El rival ha jugado:{jug_1_limpia}.\nHas ganado el turno! Vais {puntos['jug_1']}-{puntos['jug_2']}".encode())

dir_server = ("127.0.0.1", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(dir_server)

sock.listen()

while True:
    cliente_1, dir_cli_1 = sock.accept()
    cliente_2, dir_cli_2 = sock.accept()

    threading.Thread(target=juego, args=(cliente_1, dir_cli_1, cliente_2, dir_cli_2)).start()




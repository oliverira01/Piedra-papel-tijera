import random

def quien_gana(eleccion,ordenador):
    if eleccion == ordenador:
        print("Empate") 
        return "empate"
    elif eleccion == 0 and ordenador == 1:
        print("Gana el ordenador")
        return "cpu"
    elif eleccion == 0 and ordenador == 2:
        print("Ganaste")
        return "usuario"
    elif eleccion == 1 and ordenador == 0:
        print("Ganaste")
        return "usuario"
    elif eleccion == 2 and ordenador == 0:
        print("Gana el ordenador")
        return "cpu"
    elif eleccion == 1 and ordenador == 2:
        print("Gana el ordenador")
        return "cpu"
    elif eleccion == 2 and ordenador == 1:
        print("Ganaste")
        return "usuario"

def puntos(ganador, ganacpu, ganausuario, empate):
    if ganador == "cpu":
        ganacpu += 1
    elif ganador == "usuario":
        ganausuario += 1
    elif ganador == "empate":
        empate += 1
    else:
        print("Invalid")
    return ganacpu , ganausuario , empate

ganacpu = 0
ganausuario = 0
empate = 0

volver_jugar = "s"
while volver_jugar == "s":
    print("Vamos a jugar Piedra, Papel, Tijera")
    eleccion = int(input("Elije que quieres usar (0-->Piedra  1-->Papel  2-->Tijera):"))
    match eleccion:
            case 0:
                print("Sacaste Piedra")
            case 1:
                print("Sacaste Papel")
            case 2:
                print("Sacaste Tijera")
            case _:
                print("Accion no valida")

    ordenador = (random.randint(0, 2))
    match ordenador:
            case 0:
                print("Ordenador saca Piedra")
            case 1:
                print("Ordenador saca Papel")
            case 2:
                print("Ordenador saca Tijera")

    ganador = quien_gana(eleccion,ordenador)
    ganacpu , ganausuario , empate = puntos(ganador, ganacpu, ganausuario, empate) 
    print("Marcador:" , "Puntos usuario ->" , ganausuario , "Empates ->" , empate ,  "puntos ordenador ->" , ganacpu)
    if ganausuario == 3:
        break
    elif ganacpu == 3:
        break
    else:
        volver_jugar = input("¿Quieres volver a jugar? (s/n)")
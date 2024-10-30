import random

def quien_gana(eleccion,ordenador):
    if eleccion == ordenador:
        print("EMPATE")
    elif eleccion == 0 and ordenador == 1:
        print("Gana el ordenador")
    elif eleccion == 0 and ordenador == 2:
        print("Ganaste")
    elif eleccion == 1 and ordenador == 0:
        print("Ganaste")
    elif eleccion == 2 and ordenador == 0:
        print("Gana el ordenador")
    elif eleccion == 1 and ordenador == 2:
        print("Gana el ordenador")
    elif eleccion == 2 and ordenador == 1:
        print("Ganaste")

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

    quien_gana(eleccion,ordenador)
    volver_jugar = input("¿Quieres volver a jugar? (s/n)")


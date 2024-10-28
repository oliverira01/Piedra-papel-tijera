import random

print("Vamos a jugar Piedra, Papel, Tijera")
eleccion = int(input("Elije que quieres usar (0-->Piedra  1-->Papel  2-->Tijera):"))
match eleccion:
        case 0:
            print("Piedra")
        case 1:
            print("Papel")
        case 2:
            print("Tijera")
        case _:
            print("Accion no valida")

def ordenador():
    (random.randint(0, 2))

def quien_gana():
    if eleccion == ordenador():
        print("EMPATE")
    elif eleccion == 0 and ordenador() == 1:
        print("Gana Ordenador")
    
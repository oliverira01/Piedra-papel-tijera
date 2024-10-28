print("Vamos a jugar Piedra, Papel, Tijera")
eleccion = input("Elije que quieres usar (1-->Piedra  2-->Papel  3-->Tijera):")
match eleccion:
        case "1":
            print("Piedra")
        case "2":
            print("Papel")
        case "3":
            print("Tijera")
        case _:
            print("Accion no valida")







# Lista [] ; *args


def suma (numero_1, numero_2):
    return numero_1 + numero_2

def suma (numero_1, numero_2, numero_3):
    return numero_1 + numero_2 + numero_3

def suma (numero_1, numero_2, numero_3, numero_4):
    return numero_1 + numero_2 + numero_3 + numero_4

def suma (numero_1, numero_2, numero_3, numero_4, numero_5):
    return numero_1 + numero_2 + numero_3 + numero_4 + numero_5


# argumentos indeterminados

def suna (*args):  # ista []
    suma_total = 0
    for arg in args:
        print(f"[{arg}]")
        suma_total += arg
        
    print(f" La suma total : {suma_total}")

# Invocacion

suma(1,3,5,7,9)

#suma(1)  # Creando super funciones



# elevados al cuadrado

def eleva_al_cuadrado(*args):
    for index, arg in enumerate(args):
        args[index]  *=2
        
        
bandera = True
While bandera:
    print("Ingresa los datos a ser elevados al cuadrado")
    lista = input("Ingresa los datos separados por comas") # 1,2,3,4,5,6
    

        




# Ejercicio 1000
print("Hello, world!")  


# Ejercicio 1001
A = int(input())
B = int(input())
X = A + B
print(f"X = {X}")


# Ejercicio 1002
pi = 3.14159
radio = float(input())
area = pi * radio**2

print(f"A = {area:.4f}")


# Ejercicio 1003
A = int(input())
B = int(input())
SOMA = A + B
print(f"SOMA = {SOMA}")  


# Reto 1004
A = int(input())
B = int(input())

PROD = A * B
print(f"PROD = {PROD}")


# Estructura de control

menu = """
       ***************************************
       *  Menu principal de la aplicacion    *
       ***************************************
       
       Elija la opcion del reto que desea ejecutar
       1000: Hello World!
       1001: Suma Simple
       1002: Area Circulo
       1003: Suma 2 numeros
       1004: Producto de 2 numeros
       1005: 
       
       1037: Ejemplo
       0: Salir del programa
"""
bandera = True


while bandera:
    print(menu)
    opcion = int (input("Elija una opción: \n"))
    if opcion == 0:
        print("Hasta pronto!!")
        break
    elif opcion == 1000:
        #Ejercicio 1000
        print("Hello World!") 
    elif opcion == 1001:
        # Ejercicio 1001
        A = int(input("Ingrese #1 de la suma : \n"))
        B = int(input("Ingrese #2 de la suma : \n"))
        X = A + B
        print(f"X = {X}")
    elif opcion == 1002:
        # Ejercicio 1002
        pi = 3.14159
        radio = float(input("Ingrese el radio de la circunferencia: \n"))
        area = pi * radio**2

        print(f"A={area:.4f}")
    else:
        print("La opcion seleccionado no existe!!!")
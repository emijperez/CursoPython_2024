


def suma(numero_1, numero_2, numero_3):    # Definicion de los parametros de la funcion
    return numero_1 + numero_2 + numero_3

def resta(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicacion(numero_1, numero_2):
    return numero_1 * numero_2

def division(dividendo, divisor):
    return dividendo / divisor

# Despues de definir los parametros, invocamos las funciones
# Invocacion de funciones mediante argumentos de posicion

#suma(5, 4.0, 3.0)
print(f" El resultado de la suma es = {suma(5, 4.0, 3.0)}")

print(f" El resultado de la resta es = {resta(10, 8)}")

print(f" El resultado de la multiplicacion es = {multiplicacion(8, 9)}")

print(f" El resultado de la division es = {division(10, 2)}")
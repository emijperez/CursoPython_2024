
# Como definir una función

# Función sin parámetros

def saludos():
    print("Hola mundo desde una funcion sin argumentos")

# Funcion con parámetros

def saludos_nombre(nombre):
    print(f"Hola como estas : {nombre}")
     
# Invocaciones

saludos()  # Sin argumentos
nombre = "Darwin Caller"

saludos_nombre("Darwin Caller")   # Una invocacion con argumentos : Invocacion por posicion
saludos_nombre(nombre="Nicolas Calle") # Una invocacion con argumentos : Invocacion por nombre

# Una funcion que retorne datos
# Palabra reservada "return"
def suma(numero_1, numero_2):
    return numero_1 + numero_2

# Invocar la funcion suma

resultado = suma(10.2,62)
print(f"El resultado de la funcion suma = {resultado}")

print("Aprendiendo funciones con Python")

def resta(num1, num2):
    return num1 - num2

print(f"El resultado de la funcion resta = {resta(8,5)}")  # Invocacion por posicion

print(f"El resultado de la funcion resta = {resta(num1=80,num2=50)}") # Invocacion por nombre de variable

print(f"El resultado de la funcion resta = {resta(num2=150,num1=280)}") # Invocacion por nombre de variable


# Suma enteros y floats
print("****************************************************************")

print(f"El resultado de la funcion suma = {suma(10.20, 0.62):.2f}")


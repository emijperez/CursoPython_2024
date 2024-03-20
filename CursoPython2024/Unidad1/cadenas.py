

#Representacion de Strings

cadena_1 = "Hola"
cadena_2 = 'Mundo'
cadena_3 = """
    Esta 
    es un 
    ejemplo de cadena \n
    múltiples \t líneas
    \r code
"""

print(type(cadena_1))
print(type(cadena_2))
print(type(cadena_3))

print(cadena_1)
print(cadena_2)
print(cadena_3)

print(f"")


#Signo para concatenar cadenas va es signo (+)

cadena_a = "Darwin "
cadena_b = "Python "
cadena_c = "Hola Mundo  "
cadena_final = cadena_a + cadena_b + cadena_c
print(cadena_final)

print(f"El resultado de concatenar: {cadena_a}, {cadena_b}, {cadena_c} es = {cadena_final}" )

#Caracter para escapar simbolos dentro de cadenas
# '\'
# I`am Monty Python

print("I`am \"Monty Python\"")

print('I`am "Monty2 Python"')


#Cadena Vacia o Nulas
cadena_nula = ' '
cadena_nula = ""
cadena_nula = None  # Es utilizar esta forma

#Operaciones con Cadenas

# Operacion 1 : Concatenar (+)
# Operacion 2 : Multiplicar (*)

cadena_1 = "Hola Mundo"
cadena_2 = "Python 3 "

print(cadena_1 + cadena_2)
print(cadena_1*10)
print(cadena_2*5)

#Metodos de Cadenas

print(type(cadena_1))

print("******************** Metodos de la calse String ******************")
cadena_1 = "Hola Mundo"
print(cadena_1.upper())

cadena_1 = "hola mundo desde python"
print(cadena_1.capitalize())

cadena_1 = "hola mundo desde python"
print(cadena_1.replace('o', 'e').upper())


cadena_1 = "hola mundo desde python"
print(cadena_1.join(['OLA', 'prueba' , 'nombre']))

#           0124345678910
cadena_1 = " hola mundo desde python"  # La lista de caracteres: ['H','o','l','a'.....]
print(cadena_1.index('mundo'))

cadena_1 = "333"
print(cadena_1.isalnum())

print("------- ------")
cadena_1 =  'DC45'
print(cadena_1.isascii())

#Validaciones en cadenas
#Operdor in

cadena_1 = "holax"
cadena_2 = ("hola mundo holax") 

print("Validaciones de Cadenas")
print(cadena_1 in cadena_2)

print(cadena_1 not in cadena_2)


# Concepto de parametros por DEFECTO #
# Simplemete es aquel que tiene un valor inicial y cuya variable de este tipo es opcion el enviar su valor

def suma(numero_1, numero_2, numero_3=0):  
                               #/\/\/\/\#  ----> Definicion de los parametros de la funcion por defecto
    return numero_1 + numero_2 + numero_3

def resta(numero_1, numero_2, num3=1):
    return numero_1 - numero_2 - num3

# Invocacion
print(f"El resultado de la suma es = {suma(10,20,1000)}")

print(f"El resultado de la suma es = {suma(numero_2=10,numero_1=20)}")


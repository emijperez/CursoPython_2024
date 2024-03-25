

# Ambito de variables :
# variables globales
# variables locales

valor_local = 1000   # Definicion de una variable global fuera de una funcion x0FA25 ---> Sin identacion
bandera = True       # variable global
var_boolean = False

def suma(num_1, num_2):
    var_boolean = True   # Variables locales son las que estan dentro de la funcion
    valor_local = 400    # Memoria ---> 0x254545
    return num_1 + num_2

print(f"Suma = {suma(500, 200)}")

print(valor_local)
print(bandera)
print(var_boolean)






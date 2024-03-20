



def concatenar_n_cadenas(*args,separador='_'):
    cadena_final = ' '
    for arg in args:
        cadena_final += arg + separador
    return cadena_final

#Invocacion por tuplas ---> *args

print(f"Cadena final {concatenar_n_cadenas('Estoy','en','Quito','Ecuador',separador='**')}")


#Promedio de notas

def promedio_de_notas(*args):
    
    """Calcula el promedio de las notas de un alumno
    
    Returns:
        promedio:      """
    
    
    promedio = 0
    for arg in args:
        promedio += arg
    return promedio / len(args)

print("Promedio de notas")
print(f" El promedio final = {promedio_de_notas(10,5.5,8,10,9.5,7.8)}")


# {'k': valor}

# Crear un diccionario mediante el envio de argumentos clave=valor

def devolver_diccionario(**kwargs):
    
    
print(f" dic = {devolver_diccionario(num1=5.2,bandera=True,my_lista=[1,2,3],entero=10,my_tupla=(1,2,3),my_diccionario={'1':'A'})}")


# args ---> (True, 5.2, 1, 2, 10, 45, 78.8, 46) ----> Respuesta : (todos los pares)
# if num % 2 == 0 ---> Numero par

def obtener_numeros_pares():
    numeros_pares = []
    for arg in args:
        if arg % 2 == 0:
            numeros_pares.append(arg)
    return numeros_pares
print(f" ")


# cadena.upper()

def convertir_a_mayusculas(*args):
    lista_final = []
    for arg in args:
        lista_final.append(arg.upper())
    return lista_final

print(f" La conversion = {convertir_a_mayusculas('hola', 'mundo', 'pythons', '2024')}")



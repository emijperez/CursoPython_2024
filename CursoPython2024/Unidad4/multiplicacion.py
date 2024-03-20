
import time      # Importando modulos de python
import os
    
def generar_tablas_multiplicar(numero_tabla):
    
    for num in range(1,13):
        print(f"{numero_tabla} * {num} = {numero_tabla * num}")
        time.sleep(0.25)
        
        
def generar_tablas_multiplicar_defecto(numero_tabla,limite_tabla=12):
    
    for num in range(1,limite_tabla+1):
        print(f"{numero_tabla} * {num} = {numero_tabla * num}")
        time.sleep(0.25)
       

menu = """
       ***************************************
       *  Menu principal de la aplicacion    *
       ***************************************
       
       Elija la opcion del reto que desea ejecutar
       1: Tablas de multiplicar
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
    respuesta_usuario = int(input("Ingrese una opcion del menu para ejecutar: \n"))
    if respuesta_usuario == 0:    
        break
    elif respuesta_usuario == 1:
        numero_tabla = int(input("Ingresa el numero de la tabla que deseas generar: \n"))
        limite_tabla = int(input("Ingresa el linite de la secuencia de la tabla: \n"))
        if limite_tabla > 0:
        #generar_tablas_multiplicar(numero_tabla)
            generar_tablas_multiplicar_defecto(numero_tabla,limite_tabla)
        time.sleep(2)
        os.system("cls")
    else:
        print("La opcion seleccionada no existe!!")
        
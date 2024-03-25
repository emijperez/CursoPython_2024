





# Operacion Extender ----> append

def crear_fichero_with(nombre_fichero='Fichero_Append.txt'):
    """Crear un fichero, con la instruccion 'with', dandole la gestion y control a python

    Args:
        nombre_fichero (str, optional): _description_. Defaults to 'Fichero_texto.txt'.
    """    
    with open(nombre_fichero, 'w') as f:
        print(f"tipo dato : {type(f)}")
        print(f"Se creo con exito")

def llenar_fichero_append(nombre_fichero="Fichero_Append.txt"):
    fichero = open(nombre_fichero, 'a')
    for linea in range(1,251)
    fichero.write(f"Linea-{linea}")
    
        
crear_fichero_with()
llenar_fichero_append()
leer_ficehro_append()
modificar_fichero_append()
        